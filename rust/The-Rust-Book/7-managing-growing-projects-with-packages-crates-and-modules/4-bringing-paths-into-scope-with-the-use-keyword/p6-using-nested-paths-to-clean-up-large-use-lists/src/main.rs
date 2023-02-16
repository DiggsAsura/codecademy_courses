// Using Nested paths to Clean Up Large use Lists

// If we're using multiple items defined in the same crate or same module, listing
// each item on its own line can take up a lot of vertical space in our files.
// For example, these two use statments we had in the Guessing Game in Listing 2-4
// bring items from std into scope:
//use std::cmp::Ordering;
//use std::io;

// Instead, we can use nested paths to bring the same items into scope in one line.
// We do this by specifying the common part of the path, followed by two colons,
// and then curly brackets around a list of the parts of the paths that differ, as shown
// in Listing 7-18.
use std::{cmp::Ordering, io};
// Specifying a nested path to bring multiple items with the same prefix into scope.

// In bigger programs, bringing many items into scope from the same crate or module
// using nested paths can reduce the number of separate use statements needed by a lot!
// We can use a nested path at any level in a path, which is useful when combining
// two use statements that share a subpath. For example 7-19 shows two use statements:
// one that brings std::io into scope and one that brings std::io::Write into scope.
use std::io;
use std::io::Write;
// Two use statements where one is a subpath of the otehr

// The common part of these two paths is std::io, and that's the complete first path.
// To merge these paths into one use statement, we can use self in the nested path,
// as shown in Listing 7-20.
use std::io::{self, Write};
// Combining the paths in Listing 7-19 into one use statement.
//
// The line brings std::io and std::io::Write into scope.
fn main() {
    println!("Hello, world!");
}
