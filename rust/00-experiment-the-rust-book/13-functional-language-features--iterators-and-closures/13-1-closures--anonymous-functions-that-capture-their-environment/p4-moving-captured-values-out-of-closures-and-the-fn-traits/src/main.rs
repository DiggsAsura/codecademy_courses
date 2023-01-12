// Moving Captured Values Out of Clusures and the Fn Traits
// ========================================================
//
// Once a closure has captured a reference or captured ownership of a value from the environment
// where the closure is defined (thus affecting what, if anything, is moved into the closure), the
// code in the body of the closure defines what happens to the references or values when the
// closure is evaluated later (thus affecthing what, if anything, is moved out of the closure). A
// closure body can do any of the following: move a captured value out of the closure, mutate the
// captured value, neither move onor mutate the value, or capture nothing from the environment to
// begin with.
//
// The way a closure captures and handles values from the environment affects which traits the
// closure implements, and traits are how functions and structs can specify what kinds of closures
// they can use. Closures will automatically implement one, two, or all three of these Fn traits,
// in an additive fashion, depening on how the closure's body handles the values:
//
// 1. FnOnce applices to closures that can be called once. All closures implement at least this
//    trait, because all closures can be called. A closure that moves captured values out of its
//    body will only implement FnOnce and none of the other Fn traits, because it can only be
//    called once.
//
// 2. FnMut applies to closures that don't move captured values out of their body, but that might
//    mutate the captured values. These closures can be called more than once.
//
// 3. Fn applies to closures that don't move captured values out of their body and that don't
//    mutate captured values, as well as closures that capture nothing from their environment.
//    These closures can be called more than once without mutating their environment, which is
//    important in cases such as calling a closure multiple times concurrently.
//
// Let's look at the definition of the unwrap_or_else method on Option<T> that we used in Listing
// 13-1:

/*
impl<T> Option<T> {
    pub fn unwrap_or_else<F>(self, f: F) -> T
    where
        F: FnOnce() -> T
    {
        match self {
            Some(x) => x,
            None => f(),
        }
    }
}
*/

// Recall that T is the generic type repreenting the type of the value in the Some variant of an
// Option. That type T is also the return type of the unwrap_or_else function: code that calls
// unwrap_or_else on an Option<String>, for example will get a String.
//
// Next, notice that the unrwap_or_else function has the additional generic type parameter F. The F
// type is the type of the parameter named f, which is the closure we provide when calling
// unwrap_or_else.
//
// The trait bound specified on the generic type F is FnOnce() -> T, which means F must be able to
// be called once, take no arguments, and reutnr a T. Using FnOnce in the trait bound expresses the
// constraint that unwrap_or_else is only going to call f at most one time. In the body of
// unwrap_or_else, we can see that if the Option is Some, f won't be called. If the Option is None,
// f will be called once. Because all closures implement FnOnce, unwrap_or_else accepts the most
// different kinds of closures and is as flexible as it can be.
//
// ---
// Note: Functions can implement all three of the Fn traits too. If what we want to do doesn't
// require capturing a value from the environment, we can use the name of a function rather than a
// closure where we need something that implements one of the Fn traits. For example, on an
// Option<Vec<T>> value, we could call unwrap_or_else(Vec::new) to get a new, empty vector if the
// value is None.
// ---
//
// Now let's look at the standard library method sort_by_key defined on slices, to see how that
// differs from unwrap_or_else and why sort_by_key uses FnMut instead of FnOnce for the trait
// bound. The closure gets one argument in the form of a reference to the current item in the slice
// being considered, and return a value of type K that can be ordered. This function is useful when
// you want to sort a slice by a particular attribute of each item. In Listing 13-7, wehave a list
// of Rectangle instances and we use sort_by_key to order them by their width attribute from low to
// high:

#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let mut list = [
        Rectangle { width: 10, height: 1 },
        Rectangle { width: 5, height: 5 },
        Rectangle { width: 7, height: 12 },
    ];

    list.sort_by_key(|r| r.width);
    println!("{:#?}", list);


    ex3();
}
// 13-7: Using sort_by_key to order recatngles by width

// This code sorts the Rectangles in the list by their width. The closure we pass to sort_by_key
// takes one parameter, which is a reference to a Rectangle instance. The closure body is just the
// width field of the Rectangle instance, which is a u32.

// The reason sort_by_key is defined to take an FnMut closure is that it calls the closure multiple
// times: once for each item in the slice. The closure |r| r.width doesn't capture, mutate, or move
// anything out from its environment, so it meets the trait bound requirements.
//
// In contrast, Listing 13-8 shows an example of a closure that implements just the FnOnce trait,
// because it moves a value out of the environemtn. The compiler won't let us use this closure with
// sort_by_key:

/*
#[derive(Debug)]
struct Rectangle2 {
    width: u32,
    height: u32,
}

fn ex2() {
    let mut list = [
        Rectangle2 { width: 10, height: 1 },
        Rectangle2 { width: 5, height: 5 },
        Rectangle2 { width: 7, height: 12 },
    ];

    let mut sort_operations = vec![];
    let value = String::from("by key called");

    list.sort_by_key(|r| {
        sort_operations.push(value);
        r.width
    }); // error: use of moved value: `value`
}
// 13-8: Attempting to use an FnOnce closure with sort_by_key
*/

// This is a contrived, convoluted way (that doesn't work) to try and count the number of times
// sort_by_key gets called when sorting list. This code attempts to do this counting by pushing
// value - a String from the closure's environment - in to the sort_operations vector. The closure
// captures value then moves value out of the closure by transferring ownership of value to the
// sort_operations vector. This closure can cbe called once; trying to call it a second time
// wouldn't work because value would no longer be in the environment to be pushed into
// sort_operations again! Therefore, this closure only implements FnOnce. When we try to compile
// this code, we get this error that value can't be moved out of the closure because the closure
// must implement FnMut:

/*
$ cargo run
   Compiling rectangles v0.1.0 (file:///projects/rectangles)
error[E0507]: cannot move out of `value`, a captured variable in an `FnMut` closure
  --> src/main.rs:18:30
   |
15 |       let value = String::from("by key called");
   |           ----- captured outer variable
16 |
17 |       list.sort_by_key(|r| {
   |  ______________________-
18 | |         sort_operations.push(value);
   | |                              ^^^^^ move occurs because `value` has type `String`, which does not implement the `Copy` trait
19 | |         r.width
20 | |     });
   | |_____- captured by this `FnMut` closure

For more information about this error, try `rustc --explain E0507`.
error: could not compile `rectangles` due to previous error
*/

// The error points to the line in the closure body that moves value out of the environemtn. To fix
// this, we need to change the closure body so that it doesn't move values out of the environment.
// To cound the number of times sorty_by_key is called, keeping a counter in the environment and
// incrementing its value in the closure body is a more straightforward way to calculate that. The
// closure in Listing 13-9 works with sort_by_key because it is only capturing a mutable reference
// to the num_sort_operations counter and can therefore be called more than once:

#[derive(Debug)]
struct Rectangle3 {
    width: u32,
    height: u32,
}

fn ex3() {
    let mut list = [
        Rectangle3 { width: 10, height: 1 },
        Rectangle3 { width: 5, height: 5 },
        Rectangle3 { width: 7, height: 12 },
    ];

    let mut num_sort_operations = 0;
    list.sort_by_key(|r| {
        num_sort_operations += 1;
        r.width
    });
    println!("{:#?}, sorted in {num_sort_operations} operations", list);
}
// Listing 13-9: Using FnMut closure with sort_by_key is allowed

// The Fn traits are important when defining or using functions or types that makes use of
// closures. In the next section, we'll discuss iterators. Many iterator methods take closure
// arguments, so keep these closure details in mind as we continue!
