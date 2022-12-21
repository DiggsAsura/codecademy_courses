// Updating a Vector
//
// To create a vector and then add elements to it, we can use the push method, as shown in
// Listing 8-3.

fn main() {
    let mut v = Vec::new();

    v.push(5);
    v.push(6);
    v.push(7);
    v.push(8);
}
// 8-3: Using the push method to add values to a vector

// As with any variable, if we want to be able to change its value, we need to make
// it mutable using the mut keyword, as discussed in Chapter 3. The numbers we place
// indise are all of type i32, and Rust infers this from the data, so we don't need the
// Vec<i32> annotation.
