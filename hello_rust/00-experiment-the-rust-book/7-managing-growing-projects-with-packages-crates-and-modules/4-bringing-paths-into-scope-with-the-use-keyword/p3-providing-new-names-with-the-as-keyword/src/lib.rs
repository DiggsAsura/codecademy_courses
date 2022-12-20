// Providing New Names with the as Keyword
//
// There's another solution to the problem of bringing two types of the same
// name into scope with use: after the path, we can specify as a new local
// name, or alias, for the type. Listing 7-16 shows another way to write the code
// in Listing 7-15 by renaming one of the two Result types using as.

// Listing 7-16:
use std::fmt::Result;
use std::io::Result as IoResult;

fn function1() -> Result {
    // --snip--
}

fn function2() -> IoResult<()> {
    // --snip--
}
// Renaming a type when it's brought into scoe with the as Keyword

// In the second use statement, we chose the new name IoResult for the std::io::Result
// type, which won't conflict with the Result from std::fmt that we've also brought into
// scope. Listing 7-15 and Listing 7-16 are considered idiomatic, so
// the choice is up to you!

