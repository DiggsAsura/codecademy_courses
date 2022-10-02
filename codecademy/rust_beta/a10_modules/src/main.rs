fn main() {
    ex3();
    ex2();    
}

// MODULES
// ========
//
// Once a codebase gets large, it becomes helpful to separate our code into distinct
// sections. Rust has a module system that provides user-defined namespacing within
// our codebase. 
//
// mod
// ----
//
// We can define a module using the mod keyword. A module has its own distinct scope
// and visibility. 
//
// Here we have defined a module named cake with an is_favorite() function inside it:

fn ex1() {
    mod cake {
        pub fn is_favorite(name: &str) -> bool {
            name == "Coconut"
        }
    }

// Once we have declared a module, its content can be accessed by utilizing path 
// syntax. A path is created by chaining any number of nested modules together with
// the :: operator.
//
// Now, let's utilize our is_favorite() function by accessing it by its path:

    let guess = cake::is_favorite("Marble");
}

// Utilizing paths intentionaly in our code is one way of increasing our code's
// readability.
//
//
// Nesting Modules
// ================
//
// Modules can be nested indefintely: 

fn ex2() {
    mod cake {
        pub mod flavors {
            pub const COCONUT: &str = "Coconut";

            pub mod toppings {
                pub const SPRINKLES: &str = "Sprinkles";
            }
        }
    }

    println!("{}", cake::flavors::COCONUT);
    println!("{}", cake::flavors::toppings::SPRINKLES);
}


// IMPORTING ITEMS
// =================
//
// We can import any module or contained item into the current scope with the use
// keyword followed by the path to the item we wish to import.
//
// The item being imported must be declared as public with the pub keyword. All items
// in Rust are private by default.

fn ex3() {
    mod cake {
        pub mod flavors {
            pub const COCONUT: &str = "Coconut";
        }
    }

    // A module must be 'pub' to access it by name.
    use cake::flavors;

    println!("{}", flavors::COCONUT);
}


// EXPORTING ITEMS
// =================
//
// When our crate is a library, making an item public with pub will expose that item
// to users of our library. Rust also allows us to limit where an item is accessible
// when we make it public.
//
// If we have a function that we want to make public internally within our crate but 
// not to users of our library, we can use pub(crate):

fn ex4() {
    pub(crate) fn print_lemon() {
        println!("Lemon");
    }
}

// The public nature of this item now only extends to the crate it is defined in. Other
// designations include the parent module, with pub(super), or we can designate a 
// specific module with the in keyword, pub(in path::to::module).

    // This stuff is for now not something for me to use lol. I do make some sense of
    // it but can't see any usecase for me yet. 


// SEPARATE FILES
// ================
//
// Once a single file is not sufficient for holding all our code, we can move 
// modules into their own separate files. When we add a source file to our crate's
// src/ directory, we can treat that file's content as a module that can be 
// imported. 
//
// To put our cake module into a separate file, we would:
//
// 1. Create the file "src/cake.rs" and move our code into it.
//
// 2. Define the file as a module by adding mod cake; to our main.rs file
//
// mod cake;
// fn main() {
//     let guess = "Lady Baltimore";
//
//     if cake::is_favorite(guess) {
//          println!("That's my favorite cake!");
//      } else {
//          println!("Not my favorite, but still delicious.");
//      }
// }

// When using separate files, we can nest our files within folders that have the 
// same name as our module: 
//
// src/
// -- main.rs
// -- colors.rs
// -- colors/
// ---- hex.rs
//
// A file with the name mod.rs within a module's folder can take the place of a 
// named file:
//
// src/
// -- main.rs
// -- colors/
// ---- mod.rs
// ---- hex.rs
//


// crate::, super::, self::
// =========================
//
// When we need to access a module that is not a direct child of the current
// module, Rust provides us with keyword to quickly navigate our module tree.
//
// * To access modules from the root of our project, we can use crate::
// * To access the relative parent module, we can use super::
// * To access the current module, we can also use self::

fn ex5() {
    pub const FLOUNDER: &'static str = "flounder";

    fn main() {
        mod ocean {
            pub const ATLANTIC: &'static str = "Atlantic";

            mod fish {
                fn print_flounder() {
                    use crate::FLOUNDER;
                    use super::ATLANTIC;

                    println!("A {FLOUNDER} in the {ATLANTIC}");
                }
            }
        }
    }
}  // will not compile btw


// EXTERNAL CRATES
// =================
//
// After adding a dependency to our Cargo.toml, we can import it by name:

fn ex6() {
    use rand; // will fail without editing Cargo.toml

    let random_bool = rand::random();
}

// RENAMING IMPORTS
// ==================
//
// We can also rename any import within our codebase with the as keyword. This is
// useful for naming conflicts and making our code more readable.
//
// use i32 as Integer;
// let number: Integer = 137;
//


