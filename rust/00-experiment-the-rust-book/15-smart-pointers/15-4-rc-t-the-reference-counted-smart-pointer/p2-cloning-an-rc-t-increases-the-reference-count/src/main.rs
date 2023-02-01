// Cloning an Rc<T> Increases the Reference Count
// ===============================================
//
// Let's change our working example in Listing 15-18 so we can see the reference counts changing as
// we create and drop references to the Rc<List> in a.
//
// In Listing 15-19, we'll change main so it has an inner scope around list c; then we can see how
// the reference count changes when c goes out of scope.

enum List {
    Cons(i32, Rc<List>),
    Nil,
}

use crate::List::{Cons, Nil};
use std::rc::Rc;

fn main() {
    let a = Rc::new(Cons(5, Rc::new(Cons(10, Rc::new(Nil)))));
    println!("count after creating a = {}", Rc::strong_count(&a));

    let b = Cons(3, Rc::clone(&a));
    println!("count after creating b = {}", Rc::strong_count(&a));

    {
        let c = Cons(4, Rc::clone(&a));
        println!("count after creating c = {}", Rc::strong_count(&a));
    }
    println!("count after c goes out of scope = {}", Rc::strong_count(&a));
}

// 15-19: Printing the reference count

// At each point in the program where the reference count changes, we print the reference count,
// which we get by calling the Rc::strong_count function. This function is named strong_count
// rather than count because the Rc<T> type also has a weak_count; we'll see what weak_count is
// used for in the "Preventing Reference Cycles: Turning an Rc<T> into a Weak<T>" section.
//
// This code prints the following:


/*
$ cargo run
   Compiling cons-list v0.1.0 (file:///projects/cons-list)
    Finished dev [unoptimized + debuginfo] target(s) in 0.45s
     Running `target/debug/cons-list`
count after creating a = 1
count after creating b = 2
count after creating c = 3
count after c goes out of scope = 2
*/

// We can see that the Rc<List> in a has an initial reference count of 1; then each time we call
// clone, the count goes up by 1. When c goes out of scope, the count goes down by 1. We don't have
// to call a function to decrease the reference count like we have to call Rc::clone to increase
// the reference count: the implementation of the Drop trait decreases the reference count
// automatically when an Rc<T> value goes out of scope.
//
// What we can't see in this example is what when b and then a go out of scope at the end of main,
// the count is then 0, and the Rc<List> is cleaned up completely. Using Rc<T> allows a single
// value to have multiple owners, and the count ensures that the value remains valid as long as any
// of the owners still exists.
//
// Via immutable references, Rc<T> allows you to share data between multiple parts of your program
// for reading only. If Rc<T> allowed you to have multiple mutable references too, you might
// violate one of the borrowing rules discussed in Chapter 4: multiple mutable borrows to the same
// place can cause data races and inconsistencies. But bing able to mutate data is very useful! In
// the next section, we'll discuss the interior mutability pattern and the RefCell<T> type that you
// can use in conjunction with an Rc<T> to work with this immutability restriction.
