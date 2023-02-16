// Storing Lists of Values with Vectors
//
// The first collection type we'll look at is Vec<T>, also known as a vector. Vectors
// allow you to store more than one value in a single data structure that puts all the
// values next to each other in memory. Vectors can only store values of the same type.
// They are useful when you have a list of items, such as the lines of text in a file
// or the prices of items in a shopping cart.
//
//
// Creating a New Vector
//
// To create a new empty vector, we call the Vec::new function, as shown in Listing 8-1.
fn main() {
    let v: Vec<i32> = Vec::new();
}
// 8-1: Creating a new, empty vector to hold values of type i32.

// Note that we added a type annotation here. Because we aren't inserting any values
// into this vector, Rust doesn't know what kind of elements we intend to store. This is
// an important point. Vectors are implemented using generics; we'll cover how to use generics
// with your own types in Chapter 10. For now, know that the Vec<T> type provided by the
// standard library can hold any type. When we create a vector to hold a specific type, we
// can specify the type within angle brackets. In Listing 8-1, we've told Rust that the
// Vec<T> in v will hold elements of the i32 type.
//
// More often, you'll create a Vec<T> with initial values and Rust will infer the type
// of value you want to store, so you rarely need to do this type annotation. Rust
// conveniently provides the vec! macro, which will create a new vector that holds the
// values you give it. Listing 8-2 creates a new Vec<i32> that holds the values 1, 2,
// and 3. The integer type is i32 because that's the default integer type, as we
// discussed in the "Data Types" section of Chapter 3.

fn ex2() {
    let v = vec![1, 2, 3];
}
// 8-2: Creating a new vector containing values.

// Because we've given initial i32 values, Rust can infer that the type of v is
// Vec<i32>, and the type annotation isn't necessary. Next, we'll look at how to
// modify a vector.
