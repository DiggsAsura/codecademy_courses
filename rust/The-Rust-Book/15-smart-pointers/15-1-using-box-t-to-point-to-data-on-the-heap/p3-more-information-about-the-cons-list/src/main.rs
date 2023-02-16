// More Information About the Cons List
// =====================================
//
// A cons list is a data structure that comes from the Lisp programming language and its dialcts
// is made up of nested pairs, and is the Lisp version of a linked list. Its name comes from the
// cons function (short for "construct function") in Lisp that constructs a new pair from ist two
// arguments. By calling cons on a pair consisting of a value and another pair, we can construct
// cons lists made up of recursive pairs.
//
// For example, where's a pseudocode representation of a cons list containing the list 1, 2, 3 with
// each pair in parantheses:
//
//
// (1, (2, (3, Nil)))
//
//
// Each item in a cons list contains two elements: the value of the current item and the next item.
// The last item in the list contains only a value called Nil without a next item. A cons list is
// produced by recursively calling the cons function. The canonical name to denote the base case of
// the recursion is Nil. Note that this is not the same as the "null" or "nil" concept in Chapter
// 6, which is an invalid or absent value.
//
// The cons list isn't a commonly used data structure in Rust. Most of the time when you have a
// list of items in Rust, Vec<T> is a better choice to use. Other, more complex recursive data
// types are useful in various situations, but by starting with the cons list in this chapter, we
// can explore how boxes let us define a recursive data type without much distraction.
//
// Listing 15-2 contains an enum definition for a cons list. Note that this code won't compile yet
// because the List type doesn't have a known size, which we'll demonstrate.

enum List {
    Cons(i32, List),
    Nil,
}

// Listing 15-2: The first attempt at defining an enum to represent a cons list data structure of
// i32 values

// -----------------------------------------------------------------------------
// Note: We're implementing a cons list that holds only i32 values for the purpose of this example.
// We could have implemented it using generics, as we discussed in Chapter 10, to define a cons
// list type that could store values of any type.
// -----------------------------------------------------------------------------
//
// Using the List type to store the list 1, 2, 3 would look like the code in Listing 15-3:

use crate::List::{Cons, Nil};

fn main() {
    let list = Cons(1, Cons(2, Cons(3, Nil)));
}

// Listing 15-3: Using the List enum to store the list 1, 2, 3

// The first Cons value holds 1 and another List value. This List value is another Cons value that
// holds 2 and another List value. This List value is one more Cons value that holds 3 and a List
// value, which is finally Nil, the non-recursive variant that signals the end of the list.
//
// If we try to compile this code, we get the error shown in Listing 15-4:



/*
$ cargo run
   Compiling cons-list v0.1.0 (file:///projects/cons-list)
error[E0072]: recursive type `List` has infinite size
 --> src/main.rs:1:1
  |
1 | enum List {
  | ^^^^^^^^^ recursive type has infinite size
2 |     Cons(i32, List),
  |               ---- recursive without indirection
  |
help: insert some indirection (e.g., a `Box`, `Rc`, or `&`) to make `List` representable
  |
2 |     Cons(i32, Box<List>),
  |               ++++    +

error[E0391]: cycle detected when computing drop-check constraints for `List`
 --> src/main.rs:1:1
  |
1 | enum List {
  | ^^^^^^^^^
  |
  = note: ...which immediately requires computing drop-check constraints for `List` again
  = note: cycle used when computing dropck types for `Canonical { max_universe: U0, variables: [], value: ParamEnvAnd { param_env: ParamEnv { caller_bounds: [], reveal: UserFacing, constness: NotConst }, value: List } }`

Some errors have detailed explanations: E0072, E0391.
For more information about an error, try `rustc --explain E0072`.
error: could not compile `cons-list` due to 2 previous errors
*/

// 15-4: The error we get when attempting to define a recursive enum


// The error shows this type "has infinite size". The reason is that we've defined List with a
// variant that is recursive: it holds another value of itself directly. As a result, Rust can't
// figure out how much space it neesd to store a List value. Let's break down why we get this
// error. First, we'll look at how Rust decides how much space it needs to store a value of a
// non-recurisve type.
// -----------------------------------------------------------------------------
// -----------------------------------------------------------------------------
//
//
//
