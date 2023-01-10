// Testing Equality with the assert_eq! and assert_ne! Macros
// ==========================================================
//
// A common way to verify functionality is to test for equality between the result of the code
// under test and the value you expect the code to return. You could do this using the assert!
// macro and passing it an expression using the == operator. However, this is such a common test
// that the standard library provides a pair of macros - assert_eq! and assert_ne! - to perform
// this test more conveniently. These macros compare two arguments for equality or inequality,
// respectively. They'll also print the two values if the assertion fails, which makes it easier to
// see why the test failed; conversely, the assert! macro only indicates that it got a false value
// for the == expression, without printing the values that led to the false value.
//
// In Listing 11-7, we write a function named add_two that adds 2 to its parameter, then we test
// this function using the assert_eq! macro.

pub fn add_two(a: i32) -> i32 {
    a + 3
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_adds_two() {
        assert_eq!(4, add_two(2));
    }
}
// 11-7: Testing the function add_two using the assert_eq! macro

// We pass 4 as the argument to assert_eq!, which is equal to the result of calling add_two(2), the
// line for this test is test tests::it_adds_two ... ok, and the ok text indicates that our test
// passed!
//
// Let's introduce a bug into our code to see what assert_eq! looks like when it fails. Change th
// implementation of the add_two function to instead add 3 above.

// Run cargo test again and it fails.

// Our test caught the bug! The it_adds_two test failed, and the message tells us that the
// assertion that fails was assertion failed: '(left == right)' and what the left and right values
// are. This message helps us start debugging: the left argument was 4 but the right argument,
// where we had add_two(2) was 5. You can imagine this would be especially helpful when we have a
// lot of tests going on.
//
// Note that in some languages and test frameworks, the parameters to equality assertion functions
// are called expected and actual, and the order in which we specify the arguments matters.
// However, in Rust, they're called left and right, and the order in which we specify the value we
// expect and the value the code produces doesn't matter. We could write the assertion in this test
// as assert_eq!(add_two(2), 4), which would result in the same message.
//
// The assert_ne! macro will pass if the two values we give it are not equal and fail if they're
// equal. This macro is most useful for cases when we're not sure what a value will be, but we know
// that the value definetly shouldn't be. For example, if we're testing a function that is
// guaranteed to change its input in some way, but the way in which the input is changed depends on
// the day of the week that we run our tests, the best thing to assert might be that the output of
// the function is not equal to the input.
//
// Under the surface, the assert_eq! and assert_ne! macros use the operators == and !=,
// respectively. When the assertions fail, these macros print their arguments using debug
// formatting, which means the values being compared must implement the PartialEq and Debug traits.
// Asll primitive types and most of the standard library types implement these traits. For structs
// and enums that you define yourself, you'll need to implement PartialEq to assert equality of
// those types. You'll also need to implement Debug to print the valuse when the assertion fails.
// Because both traits are derivable traits, as mentioned in Listing 5-12 in Chapter 5, this is
// usually as straightforward as adding the #[derive(PartialEq, Debug)] annotation to your struct
// or enum definition. See Appendix C, "Derivable Traits" for more details about these and other
// derivable traits.
//
fn main() {}
