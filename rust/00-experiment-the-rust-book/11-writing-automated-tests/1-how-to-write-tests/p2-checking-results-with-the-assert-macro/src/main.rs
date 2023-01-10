// Checking Results with the assert! macro
// =======================================
//
// The assert! macro, provided by the standard library, is useful when you want to ensure that some
// condition in a test evaluates to true. We give the assert! macro an argument that evaluates to a
// Boolean. If the value is true, nothing happens and the test passes. If the value is false, the
// assert! macro calls panic! to cause the test to fail. Using the assert! macro helps us check
// that our code is functioning the way we intend.
//
// In Chapter 5, Listing 5-15, we used a Rectangle struct and a can_hold method, which are repeated
// here in Listing 11-5. Let's put this code in the src/lib.rs (well a mod here then) then write
// some tests for it using the assert! macro.

#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}

// 11-5: Using the Rectangle struct and its can_hold method from Chapter 5

// The can_hold method returns a Boolean, which means it's a perfect use case for the assert!
// macro. In Listing 11-6, we write a test that exercises the can_hold method by creating a
// Rectangle instance that has a width of 8 and a height of 7 and asserting that it can hold
// another Rectangle insstance that has a width of 5 and a height of 1.

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn larger_can_hold_smaller() {
        let larger = Rectangle { width: 8, height: 7 };
        let smaller = Rectangle { width: 5, height: 1 };

        assert!(larger.can_hold(&smaller));
    }

    #[test]
    fn smaller_cannot_hold_larger() {
        let larger = Rectangle { width: 8, height: 7 };
        let smaller = Rectangle { width: 5, height: 1 };

        assert!(!smaller.can_hold(&larger));
    }
}
// 11-6: A test for can_hold that checks wheter a larger rectangle can indeed hold a smaller
// rectangle.

// Note that we've added a new line inside the tests module: use super::*;. The tests module is a
// regular module that follows the usual visibilitiy rules we covered in Chapter 7 in the "Paths
// for Referring to an Item in the Module Tree" section. Because the tests module is an inner
// module, we need to bring the code under test in the outer module into the scope of the inner
// module. We use a a glob here so anything we define in the outer module is available to this
// tests module.
//
// We've named our test larger_can_hold_smaller, and we've created the two Rectangle instances that
// we need. Then we called the assert! macro and passed it the result of calling
// larger.can_hold(&smaller). This expression is supposed to return true, so our test should pass.

/*
 * $ cargo test
   Compiling rectangle v0.1.0 (file:///projects/rectangle)
    Finished test [unoptimized + debuginfo] target(s) in 0.66s
     Running unittests src/lib.rs (target/debug/deps/rectangle-6584c4561e48942e)

running 1 test
test tests::larger_can_hold_smaller ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

   Doc-tests rectangle

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

*/

// It does pass! Let's add another test, this time asserting that a smaller rectangle cannot hold a
// larger rectangle. (check above)

// Because the correct result of the can_hold function in this case is false, we need to negate the
// result before we pass it to the assert! macro. As a result, our test will pass if can_hold
// returns false.
//
// Two tests that pass! Now let's see what happens to our test result when we introduce a bug in
// our code. We'll change the implementation of the can_hold method by replacing the greater-than
// sign with a less-than sign when it compares the widths:

/*
impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width < other.width && self.height < other.height
    )
)
*/

// Running the tests now produce the following:

/*
$ cargo test
   Compiling rectangle v0.1.0 (file:///projects/rectangle)
    Finished test [unoptimized + debuginfo] target(s) in 0.66s
     Running unittests src/lib.rs (target/debug/deps/rectangle-6584c4561e48942e)

running 2 tests
test tests::larger_can_hold_smaller ... FAILED
test tests::smaller_cannot_hold_larger ... ok

failures:

---- tests::larger_can_hold_smaller stdout ----
thread 'main' panicked at 'assertion failed: larger.can_hold(&smaller)', src/lib.rs:28:9
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace


failures:
    tests::larger_can_hold_smaller

test result: FAILED. 1 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

error: test failed, to rerun pass '--lib'
*/

// Our tests caught the bug! Because larger.width is 8 and smaller.width is 5, the comparison of
// the widths in can_hold now returns false: 8 is not less than 5.
fn main() {}

