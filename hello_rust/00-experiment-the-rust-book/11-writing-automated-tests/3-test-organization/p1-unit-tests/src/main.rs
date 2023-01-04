// Unit Tests
// =========================
//
// The purpose of unit tests is to test each unit of code in isolation from the rest of the code to
// quickly pinpoint where code is and isn't working as expected. You'll put unit tests in the src
// directory in each file with the code that they're testing. The convenient is to create a module
// named tests in each file to contain the test functions and to annotate the module with
// cfg(test).
//
//
// The Tests Module and #[cfg(test)]
// ---------------------------------
//
// The #[cfg(test)] annotation on the test module tells Rust to compile and run the test code only
// when you run cargo test, not when you run cargo build. This saves compile time when you only
// want to build the library and saves space in the resulting compiled artifact because the tests
// are not included. You'll see that because integration tests go in the same files as the code,
// you'll use #[cfg(test)] to specify that they shouldn't be included in the compiled result.
//
// Recall that when we generated the new adder project in the first section on this chapter, Cargo
// generated this code for us:

/*
#[cfg(test)]
mod tests {
    #[test]
    fn it_works() {
        let result = 2 + 2;
        assert_eq!(result, 4);
    }
}
*/

// This code is the automatically generated test module. The attribute cfg stands for
// configuration and tells Rust that the following item should only be included given a certain
// configuration option. In this case, the configuration option is test, which is proivded by Rust
// for compiling and running tests. By using the cfg attribute, Cargo compiles our test code only
// if we actively run the tests with cargo test. This include any helper functions that might be
// within this module, in addition to the functions annotated with #[test].
//
//
// Testing Private functions
// -------------------------
//
// There's debate within the testing community about wheter or not private functions should be
// tested directly, and other languages make it difficult or impossible to test private functions.
// Regardless of which testing ideology you adhere to, Rust's privacy rules do allow you to test
// private functions. Consider the code in Listing 11-12 with the private function internal_adder.

pub fn add_two(a: i32) -> i32 {
    internal_adder(a, 2)
}

fn internal_adder(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn internal() {
        assert_eq!(4, internal_adder(2, 2));
    }
}
// 11-12: Testing private functions

// Note that the internal_adder function is not marked as pub. Tests are just Rust code, and the
// tests module is just another module. As we discussed in the "Paths for Referring to an Item in
// The Module Tree" section, items in child modules can use the item in their ancestor modules. In
// this test, we bring all of the test module's parent's items into scope with use super::*, and
// then the test can call internal_adder. If you don't think private functions should be tested,
// there's nothing in Rust that will compel you to do so.

