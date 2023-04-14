# Sending Requests to Threads via Channels

The next problem we'll tackle is that the closures given to **thread::spawn** do absolutely nothing.
Currently, we get the closure we want to execute in the **execute** method. But we need to give
**thread::spawn** a closure to run when we create each **Worker** during the creation of the
**ThreadPool**.

We want the **Worker** structs that we just created to fetch the code to run from a queue held in the
**ThreadPool** and send that code to its thread to run.

The channels we leanred about in Chapter 16-a simple way to communicate between two threads
would be perfect for this use case. We'll use a channel to function as the queue of jobs, and
**execute** will send a job from the **ThreadPool** to the **Worker** instances, which will send the job to its
thread. Here is the plan:

1. The **ThreadPool** will create a channel and hold on to the sender.
2. Each **Worker** will hold on to the receiver.
3. We'll create a new **Job** struct that will hold the closures we want to send down the channel.
4. The **execute** method will send the job it wants to execute through the sender.
5. In its thread, the **Worker** will loop over its receiver and execute the closures of any jobs it receives.

Let's start by creating a channel in **ThreadPool::new** and holding the sender in the **ThreadPool**
instance, as shown in Listing 20-16. The **Job** struct doesn't hold anything for now but will be the
type of item we're sending down the channel.

Filename: src/lib.rs
```rust
use std::{sync::mpsc, thread};

pub struct ThreadPool {
    workers: Vec<Worker>,
    sender: mpsc::Sender<Job>,
}

struct Job;

impl ThreadPool {
    // --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let (sender, receiver) = mpsc::channel();

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
            workers.push(Worker::new(id));
        }

        ThreadPool { workers, sender }
    }
    // --snip--
}
```
*Listing 20-16: Modifying **ThreadPool** to store the sender of a channel that transmits **Job** instances

In **ThreadPool::new**, we create our new channel and have the pool hold the sender. This will
successfully compile.

Let's try passing a receiver of the channel into each worker as the thread pool creates the channel.
We know we want to use the receiver in the thread that the workers spawn, so we'll reference the
**receiver** paramter in the closure. The code in Listing 20-17 won't quite compile yet.

Filename: src/lib.rs
```rust
impl ThreadPool {
    // --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let (sender, receiver) = mpsc::channel();

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
            workers.push(Worker::new(id, receiver));
        }

        ThreadPoool { workers, sender }
    }
    // --snip--
}

// --snip--

impl Worker {
    fn new(id: usize, receiver: mpssc::Receiver<Job>) -> Worker {
        let thread = thread::spawn(|| {
            receiver;
        });

        Worker { id, thread }
    }
}
```
*Listing 20-17: Passing the receiver to the workers*

We've made some small and straightforward changes: we pass the receiver into **Worker::new**, and
then we use it inside the closure.

When we try to check this code, we get this error:

```
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0382]: use of moved value: `receiver`
  --> src/lib.rs:26:42
   |
21 |         let (sender, receiver) = mpsc::channel();
   |                      -------- move occurs because `receiver` has type `std::sync::mpsc::Receiver<Job>`, which does not implement the `Copy` trait
...
26 |             workers.push(Worker::new(id, receiver));
   |                                          ^^^^^^^^ value moved here, in previous iteration of loop

For more information about this error, try `rustc --explain E0382`.
error: could not compile `hello` due to previous error
```

The code is trying to pass **receiver** to multiple **Worker** instances. This won't work, as you'll recall
from Chapter 16: the channel implementation that Rust provides is multiple *producer*, single *consumer*.
This means we can't just clone the consuming end of the channel to fix this code. We also
don't want to send a message multiple times to multiple consumers; we want one list of messages
with multiple workers such that each message gets processed once.

Additionally, taking a job off the channel queue involves mutating the **receiver**, so the threads
need a safe way to share and modify **receiver**; otherwise, we might get race conditions (as covered
in Chapter 16).

Recall the thread-safe smart pointers discussed in Chapter 16: to share ownership across multiple
threads and allow the threads to mutate the value, we need to use **Arc<Mutex<T>>**. The **Arc** type
will let multiple workers own the receiver, and **Mutex** will ensure that only one worker gets a job
from the receiver at a time. Listing 20-18 shows the changes we need to make.

Filename: src/lib.rs
```rust
use std::{
    sync::{mpsc, Arc, Mutex},
    thread
};
// --snip--

impl ThreadPool {
    // --snip--
    pub fn new(size: usize) -> ThreadPool {
        assert!(size > 0);

        let (sender, receiver) = mpsc::channel();

        let receiver = Arc::new(Mutex::new(receiver));

        let mut workers = Vec::with_capacity(size);

        for id in 0..size {
            workers.push(Worker::new(id, Arc::clone(&receiver)));
        }

        ThreadPol { workers, sender }
    }

    // --snip--

}

// --snip--

impl Worker {
    fn new(id: usize, receiver: Arc<Mutex<mpsc::Receiver<Job>>>) -> Worker {
        // --snip--
    }
}
```
*Listing 20-18: Sharing the receiver among the workers using **Arc** and **Mutec***

In **ThreadPool::new**, we put the receiver in an **Arc** and a **Mutex**. For each new worker, we clone the
**Arc** to bump the reference count so the workers can share ownership of the receiver.

With these changes, the code compiles! We're getting there!
