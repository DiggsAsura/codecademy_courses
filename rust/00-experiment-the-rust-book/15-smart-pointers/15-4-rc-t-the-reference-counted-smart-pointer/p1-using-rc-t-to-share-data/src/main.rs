// Using Rc<T> to Share Data
// =========================
//
// Let's return to our cons list example in Listing 15-5 Recall that we defined it using Box<T>.
// This time, we'll create two lists that both share ownership of a third list. Conceptually, this
// looks similar to Figure 15-3:
//
// https://rust-book.cs.brown.edu/img/trpl15-03.svg
//
// Figure 15-3: Two lists, b and c, sharing ownership of a third list, a:

// We'll create list a that contains 5 and then 10. Then we'll make two more lists: b that starts
// with 3 and c that starts with 4. Both b and c lists will then continue on the first a list
// containing 5 and 10. In other words, both lists will share the first list containing 5 and 10.
//
// Trying to implement this scenario using our definition of List with Box<T> won't work, as shown
// in Listing 15-17:
/*
enum List {
    Cons(i32, Box<List>),
    Nil,
}

use crate::List::{Cons, Nil};

fn main() {
    let a = Cons(5, Box::new(Cons(10, Box::new(Nil))));
    let b = Cons(3, Box::new(a));
    let c = Cons(4, Box::new(a));
}
*/
// 15-17: Demonstrating we're not allowed to have two lists using Box<T> that try to share
// ownership of a third list

// When we compile this code, we get this error:

/*
$ cargo run
   Compiling cons-list v0.1.0 (file:///projects/cons-list)
error[E0382]: use of moved value: `a`
  --> src/main.rs:11:30
   |
9  |     let a = Cons(5, Box::new(Cons(10, Box::new(Nil))));
   |         - move occurs because `a` has type `List`, which does not implement the `Copy` trait
10 |     let b = Cons(3, Box::new(a));
   |                              - value moved here
11 |     let c = Cons(4, Box::new(a));
   |                              ^ value used here after move

For more information about this error, try `rustc --explain E0382`.
error: could not compile `cons-list` due to previous error
*/

// The Cons variants own the data they hold, so when we create the b list, a is moved into b and b
// owns a. Then, when we try to use a again when creating c, we're not allowed to because a has
// been moved.
//
// We could change the definition of Cons to hold references instead, but then we would have to
// specify lifetime parameters. By specifying lifetime parameters, we would be specifying that
// every element in the list will live at least as long as the entire list. This is the case for
// the elements and lists in Listing 15-17, but not in every scenario.
//
// Instead, we'll change our definition of List to use Rc<T> in place of Box<T>, as shown in
// Listing 15-18. Each cons variant will now hold a value and an Rc<T> pointing to a List. When we
// create b, instead of taking ownership of a, we'll clone the Rc<List> that a is holding, thereby
// increasing the numbers of references from one to two and letting a and b share ownership of the
// data in that Rc<List>. We'll also clone a when creating c, increasing the number of references
// from two to three. Every time we call Rc::clone, the reference count to the data within the
// Rc<List> will increase, and the data won't be cleaned up unless there are zero references to it.

enum List {
    Cons(i32, Rc<List>),
    Nil,
}

use crate::List::{Cons, Nil};
use std::rc::Rc;

fn main() {
    let a = Rc::new(Cons(5, Rc::new(Cons(10, Rc::new(Nil)))));
    let b = Cons(3, Rc::clone(&a));
    let c = Cons(4, Rc::clone(&a));
}

// 15-18: A definitino of List that uses Rc<T>

// We need to add a use statement to bring Rc<T> into scope because it's not in the prelude. In
// main, we create the list holding 5 and 10 and store it in a new Rc<List> in a. Then when we
// create b and c, we call the Rc::clone function and pass a reference to the Rc<List> in a as an
// argument.
//
// We could have called a.clone() rather than Rc::clone(&a), but Rust's convention is to use
// Rc::clone in this case. The implementation of Rc::clone doesn't make a deep copy of all the data
// like most types' implementations of clone do. The call to Rc::clone only increments the
// reference count, which doesn't take much time. Deep copies of data can take a lot of time. By
// using Rc::clone for reference counting, we can visually distinguish between the deep-copy kinds
// of clones and the kinds of clones that increase the reference count. When looking for
// performance problems in the code, we only need to consider the deep-copy clones and can
// disregard calls to Rc::clone.
