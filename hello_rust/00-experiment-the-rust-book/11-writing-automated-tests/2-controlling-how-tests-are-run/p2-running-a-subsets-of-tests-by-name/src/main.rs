// Running a Subset of Tests by Name
// ==================================
//
// Sometimes, running a full test suite can take a long time. If you're working on code in a
// particular area, you might want to run only the tests pertaining to that code. You can choose
// which tests to run by passing cargo test the name or names of the test(s) you want to run as an
// argument.
//
// To demonstrate how to run a subset of tests, we'll first create three tests for our add_two
// function, as shown in Listing 11-11, and choose which ones to run.

pub fn add_two(a: i32) -> i32 {
    a +2
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn add_two_and_two() {
        assert_eq!(4, add_two(2));
    }

    #[test]
    fn add_three_and_two() {
        assert_eq!(5, add_two(3));
    }

    #[test]
    fn one_hundred() {
        assert_eq!(102, add_two(100));
    }
}
// 11-11: Three tests with three different names

// If we run the tests without passing any arguments, as we saw earlier, all the tests will run in
// parallel.
//
//
// # Runnning Single Tests
//
// We can pass the name of any test function to cargo test to run only that test:
// $ cargo test one_hundred
//
// Only the test with the name one_hundred ran; the other two tests didn't match that name. The
// test output lets us know we had more tests that didn't run by displaying 2 filtered out at the
// end.
//
// We can't specify the names of multiple tests in this way; only the first value given to cargo
// test will be used. But there is a way to run multiple tests.
//
//
// # Filtering to Run Multiple Tests
//
// We can specify part of a test name, and any test whose name matches that value will be run. For
// example, because two of our tests' names contain add, we can run those wto by  running
// $ cargo test add
//
// This command ran all the tests with add in them and filtered out the test named one_hundred.
// Also note that the module in which a test appears become part of the test's name, so we can run
// all the tests in a module by filtering on the module's name.
