// Accessing or Modifying a Mutable Static Variable
// ==================================================
//
// In this book, we've not yet talked about global variables, which Rust does support that can be
// problematic with Rust's ownership rules. If two threads are accessing the same mutable global
// variable, it can cause a data race.
//
// In Rust, global variables are called static variables. Listing 19-9 shows an example declaration
// and use of a static variable with a string slice as a value.

static HELLO_WORLD: &str = "Hello, world!";

fn main() {
    println!("name is: {}", HELLO_WORLD);

    // static mut counter
    add_to_count(3);
    unsafe {
        println!("{}", COUNTER);
    }
}

// Listgin 19-9: Defining and using an immutable static variable

// Static variables are similar to constants, which we discurrsed in the "Differences Between
// Vriables and Constants" section in Chapter 3. The names of static variables are in
// SCREAMING_SNAKE_CASE by convention. Static variables can only store references with the 'static
// lifetime, which means the Rust compiler can figure out the lifetime and we aren't required to
// annotate it explicitly. Accessing an immutable static variable is safe.
//
// A subtle difference between constatns and immutable static variables is that values in a static
// variable have a fixed address in memory. Using the value will always access the same data.
// Constatns, on the other hand, are allowed to duplicate their data whenever they're used. Another
// difference is that static variables can be mutable. Accessing and modifying mutable static
// variables is unsafe. Listing 19-10 shows how to declare, access, and modify a mutable static
// variable named COUNTER.

static mut COUNTER: u32 = 0;

fn add_to_count(inc: u32) {
    unsafe {
        COUNTER += inc;
    }
}
// Listing 19-10: Reading from or writing to a mutable static variable is unsafe

// As with regular variables, we specify mutability using the mut keyword. Any code that reads or
// writes from COUNTER must be within an unsafe block. This code compiles and prints COUNTER: 3 as
// we would expect because it's single threaded. Having multiple threads access COUNTER would
// likely result in data races.
//
// With mutable data that is globally accessible, it's difficult to ensure there are no data races,
// which is why Rust considers mutable static variables to be unsafe. Where possible, it's
// preferable to use the concurrency techniques and thread-safe smart pointers we discussed in
// Chapter 16 so the compiler checks that data accessed from different threads is done safely.

