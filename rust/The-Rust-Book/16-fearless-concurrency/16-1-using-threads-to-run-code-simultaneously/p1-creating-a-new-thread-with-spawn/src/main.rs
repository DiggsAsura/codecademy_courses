// Creating a New Thread with spawn
// =================================
//
// To create a new thread, we call the thread::spawn function and pass it a closure (we talked
// about closures in Chapter 13) containing the code we want to run in the new thread. The example
// in Listing 16-1 prints some text from a main thread and other text from a new thread:

use std::thread;
use std::time::Duration;

fn main() {
    thread::spawn(|| {
        for i in 1..100 {
            println!("hi number {i} from the spawned thread!");
            thread::sleep(Duration::from_millis(100));
        }
    });

    for i in 1..5 {
        println!("hi number {i} from the main thread!");
        thread::sleep(Duration::from_millis(1000));
    }
}

// Listing 16-1: Creating a new thread to print one thing while the main thread prints something
// else

// Note that when the main thread of a Rust program completes, all spawned thread are shut down,
// whether or not they have finished running. T-he output from this program might be a little
// different every time, but it will look similar to the following:


/*
hi number 1 from the main thread!
hi number 1 from the spawned thread!
hi number 2 from the main thread!
hi number 2 from the spawned thread!
hi number 3 from the main thread!
hi number 3 from the spawned thread!
hi number 4 from the main thread!
hi number 4 from the spawned thread!
hi number 5 from the spawned thread!
*/


// The calls to thread::sleep force a thread to stop its execution for a short duration, allowing a
// different thread to run. The threads will probably take turns, but that isn't guaranteed: it
// depends on how your operating system schedules the threads. In this run, the main thread printed
// first, even through the print statement from the spawned thread appears first in the code. And
// even though we told the spawned thread to print until i is 9, it only got to 5 before the main
// thread shut down.
//
// If you run this code and only see output from the main thread, or don't see any overlap, try
// increaing the numbers in the ranges to create more oppertunities for the operating system to
// switch between the threads.
