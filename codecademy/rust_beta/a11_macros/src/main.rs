fn main() {
    ex2();
    ex1();
}

// MACROS
// ======
//
// Rust's macro system is a way of manipulating and generating source code. Macros allow
// us to do things that would otherwise not be possible in the normal language structure
// or require a large amount of code repetition.
//
//
// What are Macros?
// -----------------
//
// Macros are procedures that expand and generate raw source code before the rustc compiler
// begins its compilation step. We can spot macros in a Rust program in two different
// places:

fn ex1() {
    // Attributes are macros
    #[derive(Debug)]
    struct Wow;

    let wow = Wow;

    // Calls ending with '!' are macros
    println!("{wow:?} that is convenient!");
}

// In this example, the #[derive()] macro will generate all the source code necessary for
// Wow to be able to print debug out. The println!() macros allows us to format and print a
// string with a convenient interpolation syntax.
//
// Macros are a core part of the Rust language and can be very powerful tools for creating
// intuitive programmer interfaces for your library.


// FUNCTION-LIKE MACROS
// =====================
//
// Function-like macros look like normal function calls whose name ends with a !.
// One of the most commonly used macros in Rust is println!() which prints a line of text
// to stdout. 
//
// let warm = "auburn";
// let cool = "cerulean";
// println!("the sky is {cool} and {warm});
//
// You may notice that we are using a special syntax to interpolate our variables. 
//
// Unlike functions, the input of the body of a macro call is arbitary. The macro author
// has complete control over the syntactical bits of the language down to individual tokens.
//
// When calling function-like macros, we can denote the body of the macro with (), [] or {}
// interchangeably.

fn ex2() {
    // Macros utilizing '[]' are conventionally used for collections.
    let clouds = vec![12, 97, 24];

    // 'rustfmt' will not format macros that utilize '{}'
    let today = println! {
        " Look up
            toward the sky,
        it's a beautiful day."
    };
}
