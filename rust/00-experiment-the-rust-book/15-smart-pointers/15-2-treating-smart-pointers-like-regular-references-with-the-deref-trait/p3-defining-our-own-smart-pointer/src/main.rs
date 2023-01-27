// Defining Our Own Smart Pointer
// ==============================
//
// Let's build a smart pointer similar to the Box<T> type provided by the standard library to
// experience how smart pointers behave differently from references by default. Then we'll look at
// how to add the ability to use the dereference operator.
//
// The Box<T> type is ultimately defined as a tuple struct with one element, so Listing 15-8
// defines a MyBox<T> type in the same way. We'll also define a new function to match the new
// function defined on Box<T>.

struct MyBox<T>(T);

impl<T> MyBox<T> {
    fn new(x: T) -> MyBox<T> {
        MyBox(x)
    }
}

// Listing 15-8: Defining a MyBox<T> type


// We define a struct named MyBox and declare a generic parameter T, because we want our type to
// hold values of any type. The MyBox type is a tuple struct with one element of type T. The
// MyBox::new function takes one parameter of type T and returns a MyBox instance that holds the
// value passed in.
//
// Let's try adding the main function in Listing 15-7 to Listing 15-8 and changing it to use the
// MyBox<T> type we've defined instead of Box<T>. The code in Listing 15-9 won't compile because
// Rust doesn't know how to dereference MyBox.

fn main() {
    let x = 5;
    let y = MyBox::new(x);

    assert_eq!(5, x);
    assert_eq!(5, *y);
}

// Listing 15-9: Attempting to use MyBox<T> in the same way we used references and Box<T>


// Here's the resulting compilation error:

/*
 * $ cargo run
   Compiling deref-example v0.1.0 (file:///projects/deref-example)
error[E0614]: type `MyBox<{integer}>` cannot be dereferenced
  --> src/main.rs:14:19
   |
14 |     assert_eq!(5, *y);
   |                   ^^

For more information about this error, try `rustc --explain E0614`.
error: could not compile `deref-example` due to previous error
*/

// Our MyBox<T> type can't be dereference because we haven't implemented that ability on our type.
// To enable dereferncing with the * operator, we implement the Deref trait.
