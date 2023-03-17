// Destructuring Structs and Tuples
// ===============================
//
// We can mix, math and nest destructuring patterns in even more complex ways. The following
// example shows a complicated destructure where we nest structs and tuples inside a tuple and
// destructure all the primitive values out:

struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let ((feet, inches), Point { x, y }) = ((3, 10), Point { x: 3, y: -110 });

    println!("feet: {}, inches: {}", feet, inches);
    println!("x: {}, y: {}", x, y);
}

// This code lets us break complex types into their component parts so we can use the values we're
// interested in separately.
//
// Destructuing with patterns is a convenient way to use pieces of values, such as the value from
// each field in a struct, separately from each other.
