// Adding Custom Failure Messages
// ===============================
//
// You can also add a custom message to be printed with the failure message as optional arguments
// to the assert!, assert_eq!, and assert_ne! macros. Any arguments specified after the required
// arguments are passed along to the format! macro (discussed in Chapter 8 in the "Concatenation
// with the + Operator or the format! Macro" section), so you can pass a format string that
// contains {} placehodlers and values to go in those placehodlers. Custom messages are useful for
// documenting what an assertion means; when a test fails, you'll have a better idea of what the
// problem is with the code.
//
// For example, let's say we have a function that greets people by name and we want to test that
// the name we pass into the function appears in the output:

pub fn greeting(name: &str) -> String {
//    format!("Hello {}!", name)
    String::from("Hello!")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn greeting_contains_name() {
        let result = greeting("Carol");
        assert!(
            result.contains("Carol"),
            "Greeting did not contain name, value was '{}'",
            result
        );
    }
}
// The requirements for this program haven't been agreed upon yet, and we're pretty sure the Hello
// text at the beginning of the greeting will change. We decided we don't want to have to update
// the test when the requirements change, so instead of checking for exact equality to the value
// returned from the greeting function, we'll just assert that the output contains the text of the
// input paramter.
//
// Now let's introduce a bug into this code by changing greeting to exclude name to see what the
// default test failure looks like:

// changed pub fn greeting

// This result just indicates that the assertion failed and which line the assertion is on. A more
// useful failure message would print the value from the greeting function. Let's add a custom
// failure message composed of a format string with a placeholder filled in with the actual value
// we got from the greeting function:

// changed the test to include message above

// We can see the value we actually got in the test output, which would help us debug what happend
// instead of what we were expecting to happen.



fn main() {}
