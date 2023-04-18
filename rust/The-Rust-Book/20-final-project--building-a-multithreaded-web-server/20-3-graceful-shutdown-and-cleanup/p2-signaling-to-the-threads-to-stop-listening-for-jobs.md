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


