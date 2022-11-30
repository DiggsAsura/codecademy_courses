// Dangling References
//
// In languages with pointers, it's easy to erroneously create a dangling pointer -- a pointer that
// references a location in memory that may have been given to someone else -- by freeing some
// memory while preserving a pointer to that memory. In Rust, by contrast, the compiler guarantees
// that references will never be dangling references: if you have a reference to some data, the
// compiler will ensure that the data will not go out of scope before the reference to the data
// does. 
//
// Let's try to create a dangling reference to see how Rust prevents them with a compile-time
// error:

/*
fn main() {
    let reference_to_nothing = dangle();
}

fn dangle() -> &String {
    let s = String::from("hello");
    &s
}
*/

// So this failes becuase &s is reference to s, which is created inside the dangle() function. It
// will go out of scope and dropped at the end of the functio body, so will the reference. 
//
// The compiler will tell us that 
// "this function's return type contains a borrowed value, but there is no value for it to be
// borrowed from"
//
// The fix in this case is to not use a reference &s

fn dangle() -> String {
    let s = String::from("Hello");
    s
}

fn main() {
    let reference = dangle();
}

