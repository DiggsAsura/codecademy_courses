// Using the Newtype Pattern to Implement External Traits on External Types
// ========================================================================
//
// In Chapter 10 in the "Implementing a Trait on a Type" section, we mentioned the orphan rulle
// that states we're only allowed to implement a trait on a type if either the trait or the type
// are local to our crate. It's possible to get around this restriction using the newtype pattern,
// which involves creating a new type in a tuple struct. (We covered tuple structs in the "Using
// Tuple Structs without Named Fields to Create Different T-ypes" section of Chapter 5.) The tuple
// struct will have one field and be a thin wrapper around the type we want to implement a trait
// for. Then the wrapper type is local to our crate, and we can implement the trait on the wrapper.
// Newtype is a term that originates from the Haskell programming language. There is no runtime
// performance penalty for using this pattern, and the wrapper type is elided at compile time.
//
// As an example, let's say we want to implement Display on Vec<T>, which the orphan rule prvents
// us from doing directly because the Display trait and the Vec<T> type are defined outside our
// crate. We can make a Wrapper struct that holds an instance of Vec<T>; then we can implement
// Display on Wrapper and use the Vec<T> value, as shown in Listing 19-23:

use std::fmt;

struct Wrapper(Vec<String>);

impl fmt::Display for Wrapper {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "[{}]", self.0.join(", "))
    }
}

fn main() {
    let w = Wrapper(vec![String::from("hello"), String::from("world")]);
    println!("w = {}", w);
}
// Listing 19-23: Creating a Wrapper type around Vec<String> to implement Display

// The implementation of Display uses self.0 to access the inner Vec<T>, because Wrapper is a tuple
// struct and Vec<T> is the item and index 0 in the tuple. Then we can use the functionality of the
// Display type on Wrapper.
//
// The downside of using this technique is that Wrapper is a new type, so it doesn't have the
// methods of the value it's holding. We would have to implement all the methods of Vec<T> directly
// on Wrapper such that the methods delegate to self.0, which would allowus to treat Wrapper
// exactly like a Vec<T>. If we wanted the new type to have every method the inner type has,
// implementing the Deref trait (discussed in C-hapter 15 in the "Treating Smart Pointers Like
// Regular References with the DEref Trait" section) on the Wrapper to return the inner type would
// be a solution. If we don't want the Wrapper type to have all the methods of the inner type-for
// example, to restrict the Wrapper typ's behavior-we would have to implement just the methods we
// do want manually.
//
// This newtype pattern is also useful even when traits are not involved. Let's switch focus and
// look at some advanced ways to interact with Rust's type system.
