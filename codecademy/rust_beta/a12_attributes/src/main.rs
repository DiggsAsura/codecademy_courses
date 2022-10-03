// Attributes
// ===========
//
// Attributes in Rust are macros that allow us to do special things with
// the language such as set the compilation options, conditionally 
// compile pieces of code, ignore lints, and denote tests and benchmarks.
//
// Attributes can be declared inside the scope of item it is being applied
// to, known as inner attributes, or before the item it is being applied to,
// known as outer attributes. 
//
//
// Inner Attributes
// ------------------
//
// We can declare an inner attribute with #![attribute] placed as the first
// item declared in its scope. Inner attributes can be used in external
// blocks, functions, implementations, and modules. 
//
// We can forego all compiler warnings throughout our entire codebase 
// during development by placing #![allow(warnings)] at the top of our
// main.rs file:

#![allow(warnings)]
fn main() {
    let unused_variable = "no warnings here";
}

// In this example, if we had placed our attribute at the top of a specific
// module file rather than our main.rs file, the attribute would only
// apply to that module and all child items.

fn no_warnings() {
    #![allow(warnings)]
    let unused_variable = "no warnings here";
}

fn warnings() {
    let another_unused_variable = "we get a warning here"; // but we wont 
                                                           // in this
                                                           // isolated 
                                                           // case since
                                                           // i used it
                                                           // at the top
                                                           // too.
}


// Outer Attributes
// ------------------
//
// We can declare an outer attribute on any item by placing #[attribute]
// before the item we would like it applied to. 
//
// These are some commonly encountered attributes:

// Defining a test.
#[test]
pub fn is_true() {
    assert!(true, "successful test")
}

// Providing a deprecation warning for users of your library.
#[deprecated(since = "0.2.0", note = "replaced by 'is_true'")]
pub fn isnt_not_true() {
    println!("The compiler will warn when using this function.");
}

// Optional compilation based on target architecture.
#[cfg(target_os = "linux")]
pub fn distro_name(name: &str) {
    println!("Your linux distribution is: {name}");
}


// Attribute Syntax
// -----------------
//
// You may have noticed that the attributes we have seen so far have 
// different syntaxes within their brackets. Here are some common input
// patterns we will find in attribute macros:

// Named
#[no_std]

// Named with values
#[must_use = "This function should be used."]

// Named with list of identifiers or paths.
#[forbid(unsafe, warnings)]

// Named with list of key values.
#[cfg_attr(target_os = "linux", path = "os/linux.rs")]



// Derive
// -------
//
// The most commonly encountered attribute used in Rust is the #[derive(Trait)]
// attribute which allows us to automatically implement a trait for a type. 
//
// Here we can derive the Debug and Clone trait on our Chair struct because its
// field's type, u32 and bool, already implement them.

fn ex() {
    #[derive(Debug, Clone)]
    struct Chair {
        legs: u32,
        wooden: bool,
    }

    let chair = Chair {
        legs: 4,
        wooden: true,
    };

    // Now we can print the debug output of our 'Chair' type:
    println!("{chair:#?}");
}

// Debug is an extremely useful trait for development purposes. Other useful traits
// from the std library to derive include:
// * PartialEq,
// * Eq,
// * Copy,
// * Clone.


// Available Attributes
// ----------------------
//
// There are too many attributes built into the language to be able to discuss them
// all. A comprehensive list can be found here:
// https://doc.rust-lang.org/reference/attributes.html
//
// Remember since attributes are procedural macros, we are not limited to the 
// ones provided by the language. We can use procedural macros created by others
// and even make our own.
//
// For inspiration on how useful macros can be to the quality of life of programmers,
// here is an example of a procedural macro from the rocket crate:

// This will match an HTTP request and utilize the function as its response:

#[get("/")]
fn hello() -> &'static str {
    "Welcome to this website!"
}



// This chapter a bit above my head some of it but might make sense as I go. 
