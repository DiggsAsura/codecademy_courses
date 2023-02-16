// Exporting a Convenient Public API with pub
// ==================================================
//
// The structure of your public API is a major consideration when publishing a crate. People who
// use your crate are less familiar with the structure than you are and might have difficulty
// finding the pieces they want to use if your crate has a large module hierarchy.
//
// In Chapter 7, we covered how to make items public using the pub keyword, and bring itmes into a
// scope with the use keyword. However, the structure that mekes sense to you while you're
// developing a crate might not be very convenient for your users. You might want to organize your
// structs in a hierarchy containing multiple levels, but then people who want to use a type you've
// defined deep in the hierarchy might have trouble finding out that type exists. They might also
// be annoyed at having to enter use my_crate::some_module::another_module::UsefulType; rather than
// use my_crate::UsefulType;
//
// The good new is that if the structure isn't convenient for others to use from another library,
// you don't have to rearrange your internal organization: instead, you can re-export itmes to make
// a public structure that's different from your private struture by using pub use. Re-exporting
// takes a public item in one location and makes it public in another location, as if it where
// defined in the other location instead.
//
// For example, say we made a library named art for modeling artistic concepts. Within this library
// are two modules: a kinds module containing two enums named PrimaryColor and SecondaryColor and
// a utils module containing a function named mix, as shown in Listing 14-3;
//
// Filename: src/lib.rs
// check that file
//
// This will generate a new doc page. Try it with $ cargo doc --open
//
//
// Note that the PrimaryColor and SecondaryColor types aren't listed on the front page, nor is the
// mix function. We have to click kinds and utils to see them.
//
// Another crate that depnds on this library would need use statements that bring the itmes from
// art into scope, specifying the module structure that's currently defined. Listing 14-4 shows an
// exmpale of a crate that uses the PrimaryColor and mix items from the art crate:
//
// Filename: src/main.rs (here)

use art::kinds::PrimaryColor;
use art::utils::mix;

fn main() {
    let red = PrimaryColor::Red;
    let yellow = PrimaryColor::Yellow;
    mix(red, yellow);
}

// Listing-14-4: A crate using the art crate's items with its internal structure exported

// The author of the code in Listing 14-4, which uses the art crate, had to figure out that
// PrimaryColor is in the kinds module and mix is in the utils module. T-he module structure of the
// art crate is more relevant to developers working on the art crate than to those using it. The
// internal structure doesn't contain any useful information from someone trying to understand how
// to use the art crate, but rather cause confusion because developers who use it have to figure
// out where to look, and must specify the module names in the use statements.
//
// To remove the internal organization from the public API, we can modify the art crate code in
// Listing 14-3 to add pub use statements to re-export the items at the top level, as shown in
// Listing 14-5:
//
// Filename src/lib.rs (check it)
//
//
// The API documentation that cargo doc generates for this crate will now list and link re-exports
// on the front page, as shown in Firgure 14-4, making the PrimaryColor and SecondaryColor types
// and the mix function easier to find.
//
// https://doc.rust-lang.org/book/img/trpl14-04.png
// Figure 14-4: The front page of the documentation for art that lists the re-exports

// The art crate users can still see and use the internal structure from Listing 14-3 as
// demonstrated in Listgin 14-4, or they can use the more convenient structure in Listgin 14-5, as
// shown in Listing 14-6:
//
// Filename: src/main.rs (here)

use art::mix;
use art::PrimaryColor;

fn main2() {
    // --snip--
}
// Listing 14-6: A program using the re-exported items from the art crate.

// In cases where there are many nested modules, re-exporting the types at the top level with pub
// use can make a significant difference in the experience of people who use the crate. Another
// common use of pub use is to re-export definitions of a dependency in the current crate to make
// that crate's definitions part of your crate's public API.
//
// Creating a useful public API structure is more of an art than sience, and you can iterate to
// find the API that works best for your users. Choosing pub use gives you flexibility in how you
// structure your crate internally and decouples that internal strucutre from what you present to
// your users. Look at some of the code of crates you've installed to see if their internal
// structure differs from their public API.
