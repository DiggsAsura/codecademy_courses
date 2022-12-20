// Re-exporting Names with pub use
//
// When we bring a name into scope with the use keyword, the name available in the
// new scope is private. To enable the code that calls our code to refer to that
// name as if it had been defined in that code's scope, we can combine pub and use.
// This technique is called re-exporting because we're bringing an item into
// scope but also making that item available for others to bring into their scope.
//
// Listing 7-17 shows the code in Listing 7-11 with use in the root module changed
// to pub use.
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

pub use crate::front_of_house::hosting;

pub fn eat_at_resturant() {
    hosting::add_to_waitlist();
}
// Making a name available for any code to use from a new scope with use

// Before this change, external code would have to call the add_to_waitlist
// function by using the path resturant::front_of_house::hosting::add_to_waitlist().
// Now that this pub use has re-exported the hosting module from the root module,
// external code can now use the path resturant::hosting::add_to_waitlist() instead.
//
// Re-exporting is useful when the internal structure of your code is different from
// how programmers calling your code would think about the domain. For example, in this
// resturant metaphor, the people running the resturant think about "front of house"
// and "back of house." But customers visiting a resturant probably won't think about
// the parts of the resturant in those terms. With pub use, we can write our code
// with one structure but expose a different structure. Doing so makes our library
// well organized for programmers working on the library and programmers calling
// the library. We'll look at another example of pub use and how it affects your
// crate's documentation in the "Exporting a Convenient Public API with pub use"
// section of Chapter 14.

