pub fn add_two(a: i32) -> i32 {
    a + 2
}

fn internal_adder(a: i32, b: i32) -> i32 {
    a + b
}

fn main() {}

// Integration Tests
// =================
//
// In Rust, integration tests are entirely external to your library. They use your library in the
// same way any other code would, which means they can only call functions that are part of your
// library's public API. Their purpose is to test wheter many parts of your library work together
// correctly. Units of code that work correctly on their own could have problems when integrated,
// so test coverage of the integrated code is important as well. To create integration tests, you
// first need a tests directory.
//
//
// The tests Directory
// -------------------
//
// We create a tests directory at the top level of our project directory, next to src. Cargo knows
// to look for integration test files in this directory. We can then make as many test files as we
// want, and Cargo will compile each of the files as an individual crate.
//
// Let's create an integration test. With the code in Listing 11-12 still in the src/main.rs file,
// make a test directory and create a new file named tests/integration_test.rs. Your directory
// structure should look like this:
//
// adder
// ├── Cargo.lock
// ├── Cargo.toml
// ├── src
// │   └── main.rs
// └── tests
//    └── integration_test.rs
//
// Enter the cdoe in Listing 11-13 into the tests/integration_test.rs file.
//

/*
use adder;

#[test]
fn it_adds_two() {
    assert_eq!(4, adder::add_two(2));
}
*/

// 11-13: An integration test of a function in the adder crate

// Each file in the tests directory is a separate crate, so we need to bring our library into each
// test crate's scope. For that reason we add use adder at the top of the code, which we didn't
// need in the unit tests.
//
// We don't need to annotate any code in tests/integration_test.rs with #[cfg(test)]. Cargo treats
// the tests directory spacially and compiles files in this directory only when we run cargo test.
// Run cargo test now:
//
// output
//
// The three sections of output includes the unit tests, the integration test, and the doc tests.
// Note that if any test in a section fails, the following sections will not be run. For example,
// if a unit test fails, there won't be any output for integration and doc tests because those
// tests will only be fun if all unit tests are passing.
//
// The first section for the unit tests is the same as we've been seeing: one line for each unit
// test (one named internal that we added in Listing 11-12) and then a summary line for the unit
// tests.
//
// The integration tests section starts with the line Running tests/integration_test.rs. Next,
// there is a line for each test function in that integration test and a summary line for the
// result of the integration test just becore the Doc-tests adder section starts.
//
// Each integration test file has its own section, so if we add more files in the tests directory,
// there will be more integration test sections.
//
// We can still run a particular integration test function by specifying the test functino's name
// as an argument to cargo test. To run all the tests in a particular integration test file, use
// the --test argument of cargo test followed by the name of the file:
//
// $ cargo test --test integration_test
//
// This command runs only the tests in the tests/integration_test.rs file.
//
//
// Submodules in Integration Tests
// -------------------------------
//
// As you add more integration tests, you might want to make more files in the tests directory to
// help organize them; for example, you can group the test functions by the functionality they're
// testing. As mentioned earlier, each file in the tests directory is compiled as its own separate
// crate, which is useful for crating separate scopes to more closely imitate the way end users
// will be using your crate. However, this means files in the tests directory don't share the same
// behavior as files in src do, as you leaned in C-hapter 7 regarding how to separate code into
// modules and files.
//
// The different behavior of tests directory files is most noticeable when you have a set of helper
// functions to use in multiple integration test files and you try to follow the steps in the
// "Separating Modules into Dofferent Files" section of Chapter 7 to extract them into a commoon
// module. For example, if we crate tests/common.rs and place a function named setup in it, we can
// add some code to setup that we want to call from multiple test functions in multiple test files:

// Filename: tests/common.rs
//
// pub fn setup() {
// }
//
// When we run the tests again, we'll see a new section in the test output for the common.rs file,
// even though this file doen't contain any test function nor did we call the setup function from
// anywhere.

/*
$ cargo test
   Compiling adder v0.1.0 (file:///projects/adder)
    Finished test [unoptimized + debuginfo] target(s) in 0.89s
     Running unittests src/lib.rs (target/debug/deps/adder-92948b65e88960b4)

running 1 test
test tests::internal ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/common.rs (target/debug/deps/common-92948b65e88960b4)

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

     Running tests/integration_test.rs (target/debug/deps/integration_test-92948b65e88960b4)

running 1 test
test it_adds_two ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

   Doc-tests adder

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

*/

// Having common appear in the test results with running 0 tests displayed for it is not what we
// wanted. We just wanted to share some code with the other integration test files.
//
// To avoid having common appear in the test output, instead of creating test/common.rs, we'll
// create tests/common/mod.rs. The project directory now looks like this:
//
// adder
// ├── Cargo.lock
// ├── Cargo.toml
// ├── src
// │   └── lib.rs
// └── tests
//    └── common
//        └── mod.rs
//    └── integration_test.rs

// This is the older naming convention that Rust also understands that we mentioned in the
// "Alternate File Paths" section of Chapter 7. Naming the files this way tells Rust not to treat
// the common module as an integration test file. When we move the setup function code into
// tests/common/mod.rs and delete the tests/common.rs file, the section in the test output will no
// longer appear. Fiels in subdirectories of the tests directory don't get compiled as separate
// crates or have sections in the test output.
//
// After we've created tests/common/mod.rs, we can use it from any of the integration test files as
// a module. Here's an example of calling the setup function from the it_adds_two test in
// tests/integration_test.rs
//
//Note that the mod common; declaration is the same as the module declaration we demonstrated in
//Listing 7-21. Then in the test function, we can call the common::setup() function.
//
//
// Integration Tests for Binary Crates
// -----------------------------------
//
// If our project is a binary crate that only contains a src/main.rs file and doesn't have a
// src/lib.rs file, we can't create integration tests in the tests directory and bring functions
// defined in the src/main.rs file into scope with a use statement. Only library crates expose
// functions that other crates can use; binary crates are meant to be run on their own.
//
// This is one of the reasons Rust projects that provide a binary have a straightforward
// src/main.rs file that calls logic that lives in the src/lib.rs file. Using that structure,
// integration tests can test the library crate with use to make the important functionality
// available. If the important functionality works, the small amount of code in the src/main.rs
// file will work as well, and that small amount of code doesn't need to be tested.
