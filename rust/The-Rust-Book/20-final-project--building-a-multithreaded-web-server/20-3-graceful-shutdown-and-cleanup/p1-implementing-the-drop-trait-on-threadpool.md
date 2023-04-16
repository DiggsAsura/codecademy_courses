# Implementing the Drop Trait on ThreadPool

Let's start with implementing **Drop** on our thread pool. When the pool is dropped, our threads
should all join to make sure they finish their work. Listing 20-22 shows a first attempt at a **Drop**
implementation; this code won't quite work yet.

Filename: src/lib.rs
```rust
impl Drop for ThreadPool {
    fn drop(&mut self) {
        for worker in &mut self.workers {
            println!("Shutting down worker {}", worker.id);

            worker.thread.join().unwrap();
        }
    }
}
```
*Listing 20-22: Joining each thread when the thread pool goes out of scope*

First, we loop through each of the thread pool **workers**. We use **&mut** for this because **self** is a
mutable reference, and we also need to be able to mutate **worker**. For each worker, we print a
message saying that this particular worker is shutting down, and then we call **join** on that worker's
thread. If the call to **join** fails, we use **unwrap** to make Rust panic and go into an ungraceful
shutdown.

Here is the error we get when we compile this code:

```
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0507]: cannot move out of `worker.thread` which is behind a mutable reference
  --> src/lib.rs:52:13
   |
52 |             worker.thread.join().unwrap();
   |             ^^^^^^^^^^^^^ ------ `worker.thread` moved due to this method call
   |             |
   |             move occurs because `worker.thread` has type `JoinHandle<()>`, which does not implement the `Copy` trait
   |
note: this function takes ownership of the receiver `self`, which moves `worker.thread`

For more information about this error, try `rustc --explain E0507`.
error: could not compile `hello` due to previous error
```
The error tells us we can't call **join** because we only have a mutable borrow of each **worker** and
**join** takes ownership of its argument. To solve this issue, we need to move the thread out of the
**Worker** instance that owns **thread** so **join** can consume the thread. We did this in Listing 17-15: if
**Worker** holds an **Option<thread::JoinHandle<()>>** instead, we can call the **take** method on the
**Option** to move the value out of the **Some** variant and leave a **None** variant in its place. In other
words, a **Worker** that is running will have a **Some** variant in **thread**, and when we want to clean up
a **Worker**, we'll replace **Some** with **None** so the **Worker** doesn't have a thread to run.

So we know we want to update the definition of **Worker** like this:

Filename: src/lib.rs
```rust
struct Worker {
    id: usize,
    thread: Option<thread::JoinHandle<()>>,
}
```

Now let's lean on the compiler to find the other places that need to change. Checking this code, we
get two errors:

```
$ cargo check
    Checking hello v0.1.0 (file:///projects/hello)
error[E0599]: no method named `join` found for enum `Option` in the current scope
  --> src/lib.rs:52:27
   |
52 |             worker.thread.join().unwrap();
   |                           ^^^^ method not found in `Option<JoinHandle<()>>`
   |
note: the method `join` exists on the type `JoinHandle<()>`
help: consider using `Option::expect` to unwrap the `JoinHandle<()>` value, panicking if the value is an `Option::None`
   |
52 |             worker.thread.expect("REASON").join().unwrap();
   |                          +++++++++++++++++

error[E0308]: mismatched types
  --> src/lib.rs:72:22
   |
72 |         Worker { id, thread }
   |                      ^^^^^^ expected enum `Option`, found struct `JoinHandle`
   |
   = note: expected enum `Option<JoinHandle<()>>`
            found struct `JoinHandle<_>`
help: try wrapping the expression in `Some`
   |
72 |         Worker { id, thread: Some(thread) }
   |                      +++++++++++++      +

Some errors have detailed explanations: E0308, E0599.
For more information about an error, try `rustc --explain E0308`.
error: could not compile `hello` due to 2 previous errors
```

Let's address the second error, which points to the code at the end of **Worker::new**; we need to
wrap the **thread** value in **Some** when we create a new **Worker**. Make the following changes to fix
this error:

Filename: src/lib.rs
```rust
impl Worker {
    fn new(id: usize, receiver: Arc<Mutex<mpsc::Receiver<Job>>>) -> Worker {
        // -- snip --
        Worker {
            id,
            thread: Some(thread),
        }
    }
}
```

The first error is in our **Drop** implementation. We mentioned earlier that we inteneded to call **take**
on the **Option** value to move **thread** out of **worker**. The following chaged will do so:

Filename: src/lib.rs
```rust
impl Drop for ThreadPool {
    fn drop(&mut self) {
        for worker in &mut self.workers {
            println!("Shutting down worker {}", worker.id);

            if let Some(thread) = worker.thread.take() {
                thread.join().unwrap();
            }
        }
    }
}
```
As discussed in Chapter 17, the **take** method on **Option** takes the **Some** variant out and leaves
**None** in its place. We're using **if let** to destructure the **Some** and get the thread; then we call
**join** on the thread. If a worker's thread is already **None**, we know that worker has already had its
thread cleanded up, so nothing happens in that case.
