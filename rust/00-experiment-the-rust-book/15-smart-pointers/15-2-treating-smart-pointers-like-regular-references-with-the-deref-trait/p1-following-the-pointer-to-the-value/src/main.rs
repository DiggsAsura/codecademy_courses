// Following the Pointer to the Value
// ==================================
//
// A regular reference is a type of pointer, and one way to think of a pointer is an arrow to a
// value stored somewhere else. In Listing 15-6, we create a reference to an i32 value and then use
// the dereference operator to follow the reference to the value:

fn main() {
    let x = 5;
    let y = &x;

    assert_eq!(5, x);
    assert_eq!(5, *y); // need to * references. If not the compiler WILL NOT tell me to do it.

    println!("x = {}", x);
    println!("y = {}", y);
}

// 15-6: Using the dereference operator to follow a reference to an in i32 value

// The variable x holds an i32 value 5. We set y to eqyal a reference to x. We can assert that x is
// equal to 5. However, if we want to make an assertion about the value in y, we have to use *y to
// follow the reference to the value it's poinint to (hence dereference) so the compiler can
// compare the actual value. Once we dereference y, we have access to the integer value y is
// pointing to that we can compare with 5.
//
// If we tried to write assert_eq(5, y); instead, we would get this compilation error:


/*
$ cargo run
   Compiling deref-example v0.1.0 (file:///projects/deref-example)
error[E0277]: can't compare `{integer}` with `&{integer}`
 --> src/main.rs:6:5
  |
6 |     assert_eq!(5, y);
  |     ^^^^^^^^^^^^^^^^ no implementation for `{integer} == &{integer}`
  |
  = help: the trait `PartialEq<&{integer}>` is not implemented for `{integer}`
  = help: the following other types implement trait `PartialEq<Rhs>`:
            f32
            f64
            i128
            i16
            i32
            i64
            i8
            isize
          and 6 others
  = note: this error originates in the macro `assert_eq` (in Nightly builds, run with -Z macro-backtrace for more info)

For more information about this error, try `rustc --explain E0277`.
error: could not compile `deref-example` due to previous error
*/

// Comparing a number and a reference to a number isn't allowed because they're different types. We
// must use the dereference operator to follow the reference to the value it's pointing to.
