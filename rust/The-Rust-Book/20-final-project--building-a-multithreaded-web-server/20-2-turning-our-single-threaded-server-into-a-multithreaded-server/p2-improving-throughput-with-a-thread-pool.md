# Improving Throughput with a Thread Pool

A *thread pool* is a group of spawned threads that are waiting and ready to handle a task. When the
program receives a new task, it assigns one of the threads in the pool to the task, and that thread
will process the task. The remaining threads in the pool are available to handle any other tasks that
come in while the first thread is processing. When the first thread is done processing its task, it's
returned to the pool of idle threads, ready to handle a new task.  A thread pool allows you to process
connections concurrently, increasing the throughput of your server.

We'll limit the number of threads in the pool to a small number to protect us from Denial of Service
(DoS) attacks; if we had our program create a new thread for each request as it came in, someone
making 10 million requests to our server could create havoc by using up all our server's resources
and grinding the processing of requests to a halt.

Rather than spawning unlimited threads, then, we'll have a fixed number of threads waiting in the
pool. Requests that come in are sent to the pool for processing. The pool will maintain a queue of
incoming requests. Each of the threads in the pool will pop off a request form this queue, handle the
request, and then ask the queue for another request. With this design, we can process up to **N**
requests concurrently, where **N** is the number of threads. If each thread is responding to a long-
running request, subsequent requests can still back up in the queue, but we've increased the
number of long-running requests we can handle before reaching that point.

This technique is just one of many ways to improve the throughput of a web server. Other options
you might explore are the *fork/join model*, the *single-threaded async I/O model*, or the *multi-threaded*
*async I/O model*. If you're interested in this topic, you can read more about other solutions and try to
implement them; with a low-level language like Rust, all of these options are possible.

Before we begin implementing a thread pool, let's talk about what using the pool should look like.
When you're trying to design code, writing the client interface first can help guide your design. Write
the API of the code so it's strucured in the way you want to call it; then implement the functionality
within that structure rather than implementing the functionality and then designing the public API.

Similar to how we used test-driven development in the project in Chapter 12, we'll use compiler-
driven development here. We'll write the code that calls the functions we want, and then we'll look at
errors from the compiler to determine what we should change next to get the code to work. Before
we do that, however, we'll explore the technique we're not going to use as a starting point.
