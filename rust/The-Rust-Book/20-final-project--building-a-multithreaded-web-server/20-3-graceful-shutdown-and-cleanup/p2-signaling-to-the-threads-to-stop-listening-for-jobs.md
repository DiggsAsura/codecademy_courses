# Signaling to the Threads to Stop Listening for Jobs

With all the changes we've made, our code compiles without any warnings. However, the bad news
is this code doesn't function the way we want it to yet. The key is the logic in the closures run by the
threads of the **Worker** instances: at the moment, we call **join**, but that won't shut down the
threads because they **loop** forever looking for jobs. If we try to drop our **ThreadPool** with our
current implementation of **drop**, the main thread will block forever waiting for the first thread to
finish.

To fix this problem, we'll need a change in the **ThreadPool** **drop** implementation and then a change
in the **Worker** loop.

First, we'll change the **ThreadPool drop** implementation to explicitly drop the **sender** before
waiting for the threads to finish. Listing 20-23 shows the changes to **ThreadPool** to explicitly drop
**sender**. We use the same **Option** and **take** technique as we did with the thread to be able to
move **sender** out of **ThreadPool**:

Filename:  src/lib.rs
```rust
pub struct ThreadPool {
    workers: Vec<Worker>,
    sender: Option<mpsc::Sender<Job>>,
}
// --snip--
impl ThreadPool {
    pub fn new(size: useize) -> ThreadPool {
        // --snip--

        ThreadPool {
            workers,
            sender: Some(sender),
        }
    }

    pub fn execute<F>(&self, f: F)
    where
        F: FnOnce() + Send + 'static,
    {
        let job = Box::new(f);

        self.sender.as_ref().unwrap().send(job).unwrap();
    }
}

impl Drop for ThreaedPool {
    fn drop(&mut self) {
        drop(self.sender.take());

        for worker in &mut self.workers {
            println!("Shutting down worker {}", worker.id);

            if let Some(thread) = worker.thread.take() {
                thread.join().unwrap();
            }
        }
    }
}
```
*Listing 20-23: Explicitly drop **sender** before joining the worker threads*

Dropping **sender closes the channel, which indicates no more messages will be sent. When that
happens, all the calls to **recv** that the workers do in the infinite loop will return an error. In Listing
20-24, we change the **Worker** loop to gracefully exit the loop in that case, which means the threads
will finish when the **ThreadPool drop** implementation calls **join** on them.

Filename: src/lib.rs
```rust
impl Worker {
    fn new(id: usize, receiver: Arc<Mutex<mpsc::Reciver<Job>>>) -> Worker {
        let thread = thread::spawn(move || loop {
            let message = receiver.lock().unwrap().recv();

            match message {
                Ok(job) => {
                    println!("Worker {id} got a job; executing.");

                    job();
                }
                Err(_) => {
                    println!("Worker {id} disconnected; shutting down.");
                    break;
                }
            }
        });

        Worker {
            id,
            thread: Some(thread),
        }
    }
}
```
*Listing 20-24: Explicitly break out of the loop when **recv** returns an error*

To see this code in action, let's modify **main** to accept only two requests before gracefully shutting
down the server, as shown in Listing 20-25.

Filename: src/main.rs
```rust
fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();
    let pool = ThreadPool::new(4);

    for stream in listener.incoming().take(2) {
        let stream = stream.unwrap();

        pool.execute(|| {
            handle_connection(stream);
        });
    }

    println!("Shutting down.");
}
```
*Listing 20-25: Shut down the server after serving two requests by exiting the loop*

You wouldn't want a real-world web server to shut down after serving only two requests. This code
just demonstrates that the graceful shutdown and cleanup is in working order.

The **take** method is defined in the **Iterator** trait and limits the iteration to the first two items at
most. The **ThreadPool** will go out of scope at the end of **main**, and the **drop** implementation will
run.

Start the server with **cargo run**, and make three requests. The third request should error, and in
your terminal you should see output similar to this:

```
$ cargo run
   Compiling hello v0.1.0 (file:///projects/hello)
    Finished dev [unoptimized + debuginfo] target(s) in 1.0s
     Running `target/debug/hello`
Worker 0 got a job; executing.
Shutting down.
Shutting down worker 0
Worker 3 got a job; executing.
Worker 1 disconnected; shutting down.
Worker 2 disconnected; shutting down.
Worker 3 disconnected; shutting down.
Worker 0 disconnected; shutting down.
Shutting down worker 1
Shutting down worker 2
Shutting down worker 3
```

You might see a different ordering of workers and messages printed. We can see how this code
works from the messages: workers 0 and 3 got the first two requests. The server stopped accepting
connections after the second connection, and the **Drop** implementation on **ThreadPool** starts
executing before worker 3 even starts its job. Dropping the **sender** disconnects all the workers and
tells them to shut down. The workers each print a message when they disconnect, and then the
thread pool calls **join** to wait for each worker thread to finish.

Notice one interesting aspect of this particular execution: the **ThreadPool** dropped the **sender**, and
before any worker received an error, we tried to join worker 0. Worker 0 had not yet gotten an error
from **recv**, so the main thread blocked waiting for worker 0 to finish. In the meantime, worker 3
received a job and then all threads received an error. When worker 0 finished, the main thread
waited for the rest of the workers to finish. At that point, they had all exited their loops and stopped.

Congrats! We've now clompleted our project; we have a basic web server that uses a thread pool to
respond asynchronously. We're able to perform a graceful shutdown of the server, which cleans up
all the threads in the pool.

Here's the full code for reference:

Filename: src/main.rs
```rust
use final::ThreadPool;
use std::fs;
use std::io::prelude::*;
use std::net::TcpListener;
use std::net::TcpStream;
use std::thread;
use std::time::Duration;

fn main() {
    let listener = TcpListener::bind("127.0.0.1:7878").unwrap();
    let pool = ThreadPool::new(4);

    for stream in listener.incoming().take(2) {
        let stream = stream.unwrap();

        pool.execute(|| {
            handle_connection(stream);
        });
    }

    println!("Shutting down.");
}

fn handle_connection(mut stream: TcpStream) {
    let mut buffer = [0; 1024];
    stream.read(&mut buffer).unwrap();

    let get = b"GET / HTTP/1.1\r\n";
    let sleep = b"GET /sleep HTTP/1.1\r\n";

    let (status_line, filename) = if buffer.starts_with(get) {
        ("HTTP/1.1 200 OK", "hello.html")
    } else if buffer.starts_with(sleep) {
        thread::sleep(Duration::from_secs(5));
        ("HTTP/1.1 200 OK", "hello.html")
    } else {
        ("HTTP/1.1 404 NOT FOUND", "404.html")
    };

    let contents = fs::read_to_string(filename).unwrap();

    let response = format!(
        "{}\r\nContent-Length: {}\r\n\r\n{}",
        status_line,
        contents.len(),
        contents
    );

    stream.write_all(response.as_bytes()).unwrap();
    stream.flush().unwrap();
}
```

Filename: src/lib.rs
```rust
use std::{
    sync::{mpsc, Arc, Mutex},
    thread,
};

pub struct ThreadPool {
    workers: Vec<Worker>,
    sender: Option<mpsc::Sender<Job>>,
}

type Job = Box<dyn FnOnce() + Send + 'static>;

impl ThreadPool {
    /// Create a new ThreadPool.
    ///
    /// The size is the number of threads in the pool.
    ///
    /// # Panics
    ///
    /// The 'new' function will panic if the size is zero.
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let (sender, receiver) = mpsc::channel();

        let receiver = Arc::new(Mutex::new(receiver));

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
            workers.push(Worker::new(id, Arc::clone(&receiver)));
        }

        ThreadPool {
            workers,
            sender: Some(sender),
        }
    }

    pub fn execute<F>(&self, f: F)
    where
        F: FnOnce() + Send + 'static,
    {
        let job = Box::new(f);

        self.sender.as_ref(),.unwrap().send(job).unwrap();
    }
}

impl Drop for ThreadPool {
    fn drop(&mut self) {
        drop(self.sender.take());

        for worker in &mut self.workers {
            println!("Shutting down worker {}", worker.id);

            if let Some(thread) = worker.thread.take() {
                thread.join().unwrap();
            }
        }
    }
}

struct Worker {
    id: usize,
    thread: Option<thread::JoinHandle<()>>,
}

impl Worker {
    fn new(id: usize, receiver: Arc<Mutex<mpsc::Receiver<Job>>>) -> Worker {
        let thread = thread::spawn(move || loop {
            let message = receiver.lock().unwrap().recv();

            match message {
                Ok(job) => {
                    println!("Worker {id} got a job; executing.");

                    job();
                }
                Err(_) => {
                    println!("Worker {id} disconnected; shutting down.");
                    break;
                }
            }
        });

        Worker {
            id,
            thread: Some(thread),
        }
    }
}
```
We could do more here! if you want to continue enhancing this project, here are some ideas:

* Add more documentation to **ThreadPool** and its public methods.
* Add tests of the library's functionality.
* Change calls to **unwrap** to more robust error handling.
* Use **ThreadPool** to perform some task other than serving web requests.
* Find a thread pool crate on **crates.io** and implement a similar web server using the crate
  instead. Then compare its API and robustness to the thread pool we implemented.

