# Developing the Library's Functionality with Test-Driven Development

Now that we've xtracted the logic into *src/lib.rs* and left the argument collecting and error handling
in *src/main.rs*, it's much easier to write tests for the core functionality of our code. We can call
functions directly with various arguments and check return values without having to call our binary
from the command line.

In this section, we'll add the searching loging to the **minigrep** program using the test-driven
develpment (TDD) process with the following steps:

    1. Write a test that fails and run it to make sure it fails for the reason you expect.
    2. Write or modify just enough code to make the new test pass.
    3. Refactor the code you just added or changed and make sure the tests continue to pass.
    4. Repeat from Step 1!

Though it's just one of many ways to write software, TDD can help drive code design. Writing the test
before you write the code that makes the test pass helps to maintain high test coverage throughout
the process.

We'll test drive the implementation of the funcitonality that will actually do the searching for the
query string in the file contents and produce a list of lines that match the query. We'll add this
functionality in a function called **search**.



## Writing a Failing Test

Because we don't need them anymore, let's remove the **println!** statements from *src/lib.rs* and
*src/main.rs* that we used to check the program's behavior. Then, in *src/lib.rs*, add **tests** module
with a test function, as we did in Chapter 11. The test function specifies the behavior we want the
**search** function to have: it will take a query and the text to search, and it will return only the
lines from the text that contain the query. Listing 12-15 shows this test, which won't compile yet.

*Filename: src/lib.rs* check the file
12-15: Creating a failing test for the **search** function we wish we had


This test searches for the string **duct**. The text we're searching is three lines, only one of which
contains **"duct"** (Note that the backslash after the opening double quite tells Rust not to put a
newline character at the beginning of the contents of this string literal). We assert that the value
returned from the **search** function contains only the line we expect.

We aren't yet able to run this test and watch it fail because the test doesn't even compile: the
**search** function doesn't exist yet! In accordance with TDD principles, we'll add just enough code to
get the test to compile and run by adding a definition of the **search** function that always returns an
empty vector, as shown in Listing 12-16. Then the test should compile and fail because an empty
vector desn't match a vector containing the line **"safe, fast, productive"**.


*Filename: src/lib.rs*
12-16: Defining just enough of the **search** function so our test will compile


Notice that we need to define an explicit lifetime **'a** in the signature of **search** and use that
lifetime with the **contents** argument and the return value. Recall Chapter 10 that the lifetime
parameters specify which argument lifetime is connected to the lifetime of the reutnr value. In this
case, we indicate that the returned vector should contain string slices that reference slices of the
argument **contents** (rather than the argument **query**).

In other words, we tell Rust that the data returned by the **search** function will live as long as the
data passed into the **search** function in the **contents** argument. Theis is important! The data
referenced *by* a slice needs to be valid for the reference to be valid; if the compiler assumes we're
making string slices of **query** rather than **contents**, it will do its safety chcecking incorrectly.

If we forget the lifetime annotations and try to compile this function, we'll get this error:


$ cargo build
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
error[E0106]: missing lifetime specifier
  --> src/lib.rs:28:51
   |
28 | pub fn search(query: &str, contents: &str) -> Vec<&str> {
   |                      ----            ----         ^ expected named lifetime parameter
   |
   = help: this function's return type contains a borrowed value, but the signature does not say whether it is borrowed from `query` or `contents`
help: consider introducing a named lifetime parameter
   |
28 | pub fn search<'a>(query: &'a str, contents: &'a str) -> Vec<&'a str> {
   |              ++++         ++                 ++              ++

For more information about this error, try `rustc --explain E0106`.
error: could not compile `minigrep` due to previous error



Rust can't possibly know which of the two arguments we need, so we need to tell it explicitly.
Because **contents** is the argument that contains all of our text and we want to return the parts of
that text that match, we know **contents** is the argument that should be connected to the return
value using the lifetime syntax.

Other programming languages don't require you to connect arguments to return values in the
signature, but this practice will get easier over time. You might want to compare this example with
the "Validating References with Lifetimes" section in Chapter 10.

Now let's run the test:


$ cargo test
   Compiling minigrep v0.1.0 (file:///projects/minigrep)
    Finished test [unoptimized + debuginfo] target(s) in 0.97s
     Running unittests src/lib.rs (target/debug/deps/minigrep-9cd200e5fac0fc94)

running 1 test
test tests::one_result ... FAILED

failures:

---- tests::one_result stdout ----
thread 'main' panicked at 'assertion failed: `(left == right)`
  left: `["safe, fast, productive."]`,
 right: `[]`', src/lib.rs:44:9
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace


failures:
    tests::one_result

test result: FAILED. 0 passed; 1 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s

error: test failed, to rerun pass '--lib'



Great, the test fails, exactly as we expected. Let's get the test to pass!



## Writing Code to Pass the Test

Currently, our test is failing because we always return an empty vector. To fix that and implement
**search**, our program needs to follow these steps:

    * Iterate thorugh each line of the contents.
    * Check wheter the line contains our query string.
    * If it does, add it to the list of values we're returning.
    * If it doesn't, do nothing.
    * Return the list of results that match.

Let's work through each step, starting with iterating through lines.


### Iterating Through Lines with the lines Method

Rust has a helpful method to handle line-by-line iteration of strings, conveniently named **lines**, that
works as shown in Listing 12-17. Note this won't compile yet.


*Filename: src/lib.rs* check the file
12-17: Iterating through each line in **contents**


The **lines** method returns an iterator. We'll talk about iterators in depth in Chapter 13, but recall
that you saw this way of using an iterator in Listing 3-5, where we used a **for** loop with an iterator
to run some code on each item in a collection.




