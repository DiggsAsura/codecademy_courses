/* Capturing References or Moving Ownership
 * ==========================================
 *
 * Clusures can capture values from their environement in three ways, which directly map the three
 * ways a function can take a paramter: borrowing immutably, borrowing mutably, and taking
 * ownership. The closure will decide which of these to use based on what the body of the function
 * does with the captured values.
 *
 * In Listing 13-4, we define a closure that captures an immutable reference to the vector named
 * list because it only needs an immutable reference to print the value:
 */

fn main() {
    let list = vec![1, 2, 3];
    println!("Before defining closure: {:?}", list);

    let only_borrows = || println!("From closure: {:?}", list);

    println!("Before calling closure: {:?}", list);
    only_borrows();
    println!("After calling closure: {:?}", list);


    ex2();
    ex3();
}

// 13-4: Defining and calling a closure that captures an immutable reference

// This example also illustrates that a variable can bind to a closure definition, and we can later
// call the closure by using the variable name and parantheses as if the variable name were a
// function name.
//
// Because we can have multiple immutable references to "list" at the same time, "list" is till
// accessible from the code before the closure definition, after the closure definition but before
// the closure is called, and after the closure is called. This code compiles, runs and prints:

/*
$ cargo run
   Compiling closure-example v0.1.0 (file:///projects/closure-example)
    Finished dev [unoptimized + debuginfo] target(s) in 0.43s
     Running `target/debug/closure-example`
Before defining closure: [1, 2, 3]
Before calling closure: [1, 2, 3]
From closure: [1, 2, 3]
After calling closure: [1, 2, 3]
*/

// Next, in Listing 13-5, we change the closure body so that it adds an element to the list vector.
// The closure now captures a mutable reference:

fn ex2() {
    println!("\n\nExample 2\n");
    let mut list = vec![1, 2, 3];
    println!("Before defining closure: {:?}", list);

    let mut borrow_mutably = || list.push(7);

    borrow_mutably();
    println!("After calling closure: {:?}", list);
}
// 13-5: Defining and calling a closure that captures a mutable reference.

// Note that there's no longer a println! between the definition and the call of the
// borrows_mutably
// closure: when borrows_mutably is defined, it captures a mutable reference to list. We don't use
// the closure again after the closure is called, so the mutable borrow ends. Between the closure
// definition and the closure call, an immutable borrow to print isn't allowed because no other
// borrows are allowed when there'a  mutable borrow. Try adding a println! there to see what error
// message you get!
//
// If you want to force the closure to take ownership of the values it uses in the environment even
// though the body of the closure doesn't strictly need ownership, you can use the move keyword
// before the parmater list.
//
// This technique is mostly useful when pssing a closure to a new thread to move the data so that
// it's owned by the new thread. We'll discuss threads and why you would want to use them in detail
// in Chapter 16 when we talk about concurrency, but for now, let's briefly explore spawning a new
// thread using a closure that needs the move keyword. Listing 13-6 shows Listing 13-4 modified to
// print the vector in a new thread rather than in the main thread:

use std::thread;

fn ex3() {
    println!("\n\nExample 3\n");
    let list = vec![1, 2, 3];
    println!("Before defining closure: {:?}", list);


    thread::spawn(move || println!("From closure: {:?}", list))
        .join()
        .unwrap();
}
// 13-6: Using move to force the closure for the thread to take ownership of list

// We spawn a new thread, giving the thread a closure to run as an argument. The closure body
// prints out the list. In Listing 13-4, the closure only captured list using an immutable
// reference because that's the least amount of access to list needed to print it. In this example,
// even though the closure body still only needs an immutable reference, we need to specify that
// list should be moved into the closure by puting the move keyword at the beginning of the
// closure definition. The new thread might finish before the rest of the main thread finishes, or
// the main thread might finish first. If the main thread maintained ownership of list but ended
// before the new thread did and dropped list, the immutable reference in the thread would be
// invalid. Therefore, the compiler requires that list be moved into the closure given to the new
// thread so the reference will be valid. Try removing move keyword or using list in the main
// thread after the clsure is defined to see what compiler error you get!
