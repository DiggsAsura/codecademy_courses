/* Creating Idiomatic use Paths
 *
 * In the earlier example, you might have wondered why we specified use
 * crate::front_of_house::hosting and then called hosting::add_to_waitlist in
 * eat_at_resturant rahter than specifying the use path all the way
 * out to dhe add_to_waitlist function to achieve the same reuslt: */

mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

use crate::front_of_house::hosting::add_to_waitlist;

pub fn eat_at_resturant() {
    add_to_waitlist();
    add_to_waitlist();
    add_to_waitlist();
}

// Although both Listing 7-11 and 7-13 accomplish the same task, Listing 7-11
// is the idiomatic way to bring a function into scope with use. Bringing the
// function's parent into scope with use means we have to specify the parent module
// when calling the function. Specifying the parent module when calling the function
// makes it clear that the function isn't locally defined while still minimizing
// repetition of the full path. The code in Listint 7-13 is unclear as to where
// add_to_waitlist is defined.
//
// On the other hand, when bringing in structs, enums, and other items with use,
// it's idiomatic to specify the full path. Listing 7-14 shows the idiomatic way to
// bring the standard library's HashMap struct into the scope of a binary crate.

use std::collections::HashMap;

fn main() {
    let mut map = HashMap::new();
    map.insert(1, 2);
}
// 7-14
//
// There's no strong reason behind this idiom: it's just the convention that has
// emerged, and folks have gotten used to reading and writing Rust code this way.
//
// The exception to this idiom is if we're bringing two items with the same name
// into scope with use statements, because Rust doesn't allow that. 7-15 shows
// how to bring two Result types into scope that have the same name but different
// parent module and how to refer to them.

use std::fmt;
use std::io;

fn function1() -> fmt::Result {
    // --snip--
}

fn function2() -> io::Result<()> {
    // --snip--
}
// 7-15

// As you can see, using the parent modules distinguishes the two Result
// types. If instead we specified use std::fmt::Result and use std::io::Result,
// we'd have two Result types in the same scope and Rust woudn't know whih
// one we meant when we used Result.
