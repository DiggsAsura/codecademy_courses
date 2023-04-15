# Implementing the execute Method

Let's finally implement the **execute** method on **ThreadPool**. We'll also change **Job** from a struct to
a type alias for a trait object that holds the type of closure that **execute** receives. As discussed in the
"Creating Type Synonyms with Type Aliases" section of Chapter 19, type aliases allow us to make
long types shorter for eas of use. Look at Listing 20-19.

Filename: src/lib.rs
```rust
// --snip--

type Job = Box<dyn FnOnce() + Send + 'static>;

impl ThreadPool {
    // --snip--

    pub fn execute<F>(&self, f: F)
    where
        F: FnOnce() + Send + 'static,
    {
        let job = Box::new(f);

        self.sender.send(job.unwrap();
    }
}

// --snip--
```
*Listing 20-19: Creating a **Job** alias for a **Box** that holds each closure and then sending the job down the channel*

After creating a new **Job instance using the closure we get in **execute**, we send that job down the
sending end of the channel. We're calling **unwrap** on **send** for the case that sending fails. This might
happen if, for example, we stop all our threads from executing, meaning the receiving end has
stopped receiving new messages. At the moment, we can't stop our threads from executing: our
threads continue executing as long as the pool exists. The reason we use **unwrap** is that we kno
the failure case won't happen, but the compiler doesn't know that.

But we're not quite done yet! In the worker, our closure being passed to **thread::spawn** still only
*references* the receiving end of the channel. Instead, we need the closure to loop forever, asking the
receiving end of the channel for a job and running the job when it gets one. Let's make the change
shown in Listing 20-20 to **Worker::new**.

Filename: src/lib.rs
```rust
// --snip--

impl Worker {
    fn new(id: usize, receiver: Arc<Mutex<mpsc::Receiver<Job>>>) -> Worker {
        let thread = thread::spawn(move || loop {
            let job = receiver.lock().unwrap().recv().unwrap();

            println!("Worker {id} got a job; executing.");

            job();
        });

        Worker { id, thread }
    }
}
```
*Listing 20-20: Receiving and executing the jobs in the worker's thread*

Here, we first call **lock** on the **receiver** to acquire the mutex, and then we call **unwrap** to panic on
any errors. Acquiring a lock might fail if the mutex is in a *poisoned* state, which can happen if some
other thread panicked while holding the lock rather than releaseing the lock. In this situation, calling
**unwrap** to have this thread panic is the correct action to take. Feel free to change this **unwrap** to an
**expect** with an error message that is meaningful to you.

If we get the lock on the mutex, we call **recv** to receive a **Job** from the channel. A final **unwrap**
moves past any errors here as well, which might occur if the thread holding the sender has shut
down, similar to how the **send** method returns **Err** if the receiver shuts down.

The call to **recv** blocks, so if there is no job yet, the current thread will wait until a job becomes
available. The **Mutex<T>** ensures that only one **Worker** thread at a time is trying to request a job.

Our thread pool is now in a working state! Give it a **cargo run** and make some requests:

```
$ cargo run
   Compiling hello v0.1.0 (file:///projects/hello)
warning: field is never read: `workers`
 --> src/lib.rs:7:5
  |
7 |     workers: Vec<Worker>,
  |     ^^^^^^^^^^^^^^^^^^^^
  |
  = note: `#[warn(dead_code)]` on by default

warning: field is never read: `id`
  --> src/lib.rs:48:5
   |
48 |     id: usize,
   |     ^^^^^^^^^

warning: field is never read: `thread`
  --> src/lib.rs:49:5
   |
49 |     thread: thread::JoinHandle<()>,
   |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

warning: `hello` (lib) generated 3 warnings
    Finished dev [unoptimized + debuginfo] target(s) in 1.40s
     Running `target/debug/hello`
Worker 0 got a job; executing.
Worker 2 got a job; executing.
Worker 1 got a job; executing.
Worker 3 got a job; executing.
Worker 0 got a job; executing.
Worker 2 got a job; executing.
Worker 1 got a job; executing.
Worker 3 got a job; executing.
Worker 0 got a job; executing.
Worker 2 got a job; executing.
```

Success! We now have a thread pool that executes connections asynchronously. There are never
more than four threads created, so our system won't get overloaded if the server receives a lot of
requests. If we make a request to /slep, the server will be able to serve other requests by having another thread
run them:

```
Note: if you open /sleep in multiple browser windows simultaneously, they might load one at a
time in 5 second intervals. Some web browsers execute multiple instances of the same request
sequentially for caching reasons. This limitation is not caused by our web server.
```

After learning about the **while let** loop in Chapter 18, you might be wondering why we didn't write
the worker thread code as shown in Listing 20-21.

Filename: src/lib.rs
```rust
// --snip--

impl Worker {
    fn new(id: usize, receiver: Arc<Mutex<mpsc::Receiver<Job>>>) -> Worker {
        let thread = thread::spawn(move || {
            while let Ok(job) = receiver.lock().unwrap().recv() {
                println!("Worker {id} got a job; executing.");

                job();
            }
        });

        Worker { id, thread }
    }
}
```
*Listing 20-21: An alternative implementation of **Worker::new** using **while let***

This code compiles and runs but doesn't result in the desired threading behavior: a slow request will
still cause other requests to wait to be processed. The reason is somewhat subtle: the **Mutex** struct
has no public **unlock** method because the ownership of the lock is based on the lifetime of the
**MutexGuard<T>** within the **LockResult<MutexGuard<T>>** that the **lock** method returns. At compile
time, the borrow checker can then enforce the rule that a resource guarded by a **Mutex** cannot be
accused unless we hold the lock. However, this implementation can also result in the lock being
held longer than intended if we aren't mindful of the lifetime of the **MutexGuard<T>**.

The code in Listing 20-20 that uses **let job = receiver.lock().unwrap().recv().unwrap();** works
because with **let**, any temporary values used in the expression on the right hand side of the equals
sign are immediately dropped when the **let** statement ends. However, **while let** (and **if let**
and **match**) does not drop temporary values until the end of the associated block. In Listing 20-21,
the lock remains held for the duration of the call to **job()**, meaning other workers cannot receive
jobs.
