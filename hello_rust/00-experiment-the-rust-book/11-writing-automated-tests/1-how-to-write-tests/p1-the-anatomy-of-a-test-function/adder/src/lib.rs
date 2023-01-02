// The Anatomy of a Test Function
// ==============================
//
// Af its ismplest, a test in Rust is a function that's annotated with the test attribute.
// Attributes are metadata about pieces of Rust code; one example is the derive attribute we used
// with structs in Chapter 5. To change a function into a test function, add #[test] on the line
// before fn. When you run your code with the cargo test command, Rust builds a test runner binary
// that runs the annotated functions and reports on wheter each test function passes or fails.
//
// Whenever we make a new library project with Cargo, a test module with a test function in it is
// automatically generated for us. This module gives you a template for writing your tests so you
// don't have to look up the exact structure and syntax every time you start a new project. You can
// add as many additional test functions and as many test modules as you want!
//
// We'll explore some aspects of how tests work by experimenting with the template test before we
// actually test any code. Tehn we'll write some real-world tests that call some code that we've
// written and assert that its behavior is correct.
//
// Let's create a new library project called adder that will add two numbers:
//
// $ cargo new adder --lib
//     Created library `adder` project
// $ cd adder
//
// The contents of the src/lib.rs file in your adder library should look like Listing 11-1

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
// 11-1: The test module and function generated automatically Cargo

// For now, let's ignore the top two lines and focus on the function. Not the #[test] annotation:
// this attribute indicates this is a test function, so the test runner knows to treat this
// function as a test. We might also have non-test functions in the tests module to help set up
// common scenarios or perform common operations, so we always need to indicate which functions are
// tests.
//
// The example function body uses the assert_eq! macro to assert that result, which contains the
// result of adding 2 and 2, equals 4. This assertion serves as an example of the fomat for a
// typical test. Let's run it to see that this test passes.
//
// The cargo test command runs all tests in our project, as shown in Listing 11-2.
//
// $ cargo test
//    Compiling adder v0.1.0 (file:///projects/adder)
//      Finished test [unoptimized + debuginfo] target(s) in 0.25s
//        Running unittests src/lib.rs (target/debug/deps/adder-9f1f3c4a2b2f4a4a)
//
//  running 1 test
//  test tests::it_works ... ok
//
//  test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out
//
//    Doc-tests adder
//
// running 0 tests
//
// test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out
//
// 11-2: The output from running teh automatically generated test

// Cargo compiled and ran the test. We see the line running 1 test. The next line shows the name of
// the generated test function, called it_works, and that the result of running that test is ok.
// The overall summary test result: ok. means that all the tests passed, and the portion that reads
// 1 passed; 0 failed totals the number of tests that passed or failed.
//
// It's possible to mark a test as ignored so it doesn't run in a particular instance; we'll cover
// that in the "Ignoring Some Tests Unless Specifically Requested" section later in this chapter.
// Because we haven't done that here, the summary shows 0 ignored. We can also pass an argument to
// the cargo test command to run only tests whose name matches a string; this is called filtering
// and we'll cover that in "Running a Subset of Tests by Name" section. We also haven't filtered
// the tests being run, so the end of the summary shows 0 filtered out.
//
// The 0 measured statistic is for benchmark tests that measure performance. Benchmark tests are,
// as of this writing, only available in nightly Rust. See the documentation aobut benchmark tests
// to learn more.
//
// The next part of the test output starting at Doc-tests adder is for the result of any
// documentation tests. We don't have any documentation tests yet, but Rust can compile any code
// examples that appear in our API documentation. This feature helps keep your docs and your code
// in sync! We'll discuss how to write documentation tests in the "Documentation Comments as Tests"
// section of Chapter 14. For now, we'll ignore the Doc-tests output.
//
// Let's start to customize the test to our own needs. First change the name of the it_works
// function to a different name, such as exploration, like so:
/*
#[cfg(test)]
mod tests {
    #[test]
    fn exploration() {
        assert_eq!(2 + 2, 4);
    }
}
*/
// Then run cargo test again. The output now shows exploration instead of it_work:

/*
$ cargo test
   Compiling adder v0.1.0 (file:///projects/adder)
    Finished test [unoptimized + debuginfo] target(s) in 0.59s
     Running unittests src/lib.rs (target/debug/deps/adder-92948b65e88960b4)

running 1 test
test tests::exploration ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

   Doc-tests adder

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s
*/

// Now we'll add another test but this time we'll make a test that fails! Tests fail when something
// in the test function panics. Each test is run in a new thread, and when the main thread sees
// that a test thread has died, the test is marked as failed. In Chapter 9, we talked about how the
// simplest way to panic is to call the panic! macro. Enter the new test as a function name
// another, so your src/lib.rs file looks like Listing 11-3.

#[cfg(test)]
mod tests {
    #[test]
    fn exploration() {
        assert_eq!(2 + 2, 4);
    }

    #[test]
    fn another() {
        panic!("Make this test fail");
    }
}
// 11-3: Adding a second test that will fail because we call the panic! macro

// Run the tests again using cargo test. The output should look like Listing 11-4, which shows that
// our exploration test passed and another failed.

/*
$ cargo test
   Compiling adder v0.1.0 (file:///projects/adder)
    Finished test [unoptimized + debuginfo] target(s) in 0.72s
     Running unittests src/lib.rs (target/debug/deps/adder-92948b65e88960b4)

running 2 tests
test tests::another ... FAILED
test tests::exploration ... ok

failures:

---- tests::another stdout ----
thread 'main' panicked at 'Make this test fail', src/lib.rs:10:9
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace


failures:
    tests::another

test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

error: test failed, to rerun pass '--lib'
*/

// 11-4: Test results when one test passes and one test fails

// Instead of ok, the line test tests::another shows FAILED. Two new sections appear between the
// individual results and the summary: the first displays the detailed reason for each test
// failure. In this case, we get the details that another failed because it panicked at 'Make this
// test fail' on line 10 in the src/lib.rs file. The next section lists just the names of all the
// failing tests, which is useful when there are lots of tests and lots of details failing test
// ouput. We can use the name of a failing test to run just that test to more easily debug it;
// we'll talk more about ways to run tests in the "Controlling How Tests Are Run" section.
//
// The summary line displays at the end: overall, our test result is FAILED. We had one test pass
// and one test fail.
//
// Now that you've seen what the test results look like in different scenarios, let's look at some
// macros other than panic! that are usefuld in tests.
