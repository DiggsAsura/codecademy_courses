fn main() {
    ex1();
}

/* Procedural Macros
 * ===================
 *
 * Procedural Macros are a more feature-complete approach to creating macros than a declarative
 * macro can provide. They appear in many places in the Rust langugage and allow us to generate a
 * lot of code with very little input. 
 *
 *
 * Kinds of Procedural Macros
 * ---------------------------
 *
 * There are three distinct kinds of procedural macros in Rust.
 *
 * - Function-like macros: function_like!()
 * - Attribute macros: #[attribute]
 * - Custom derive macros: #[derive()]
 *
 * Let's take a quick look at the differences between these. 
 *
 *
 * Function-like
 * ---------------
 *
 * Function-like procedural macros appear in our source code the same as declarative macros,
 * written as a function call with a ! postfix. */

fn ex1() {
    macro_for_fun!()
}

/* When calling these macros, there is little difference from calling declarative ones. However,
 * behind the scenes, a procedural macro has much more flexibility in terms of parsing our input
 * and what it can accomplish syntactically.
 *
 *
 * Attribute
 * ----------
 *
 * Attribute macros operate on the syntax of the item it is applied to. Here we are applying the
 * procedural attribute macro #[dance] to the Human struct. */

fn ex2() {
    #[dance]
    struct Human {
        legs: u8,
        arms: u8,
    }
}

/* Attribute macros can operate on more then just structs. In fact, they can be written to operate
 * on almost anything. */

fn ex3() {
    #![deny(warnings)]
    #[allow(unused_variables)]
    let variable = "unused";

    #[get("/<name>")]
    fn response(name: &str) -> String {
        name.to_string()
    }
}

/* In order to know what an attribute does, it is always best to read the documentation. */


/* Derive Macros
 * --------------
 *
 * We have encountered the #[derive(Trait)] macro many times throughout this course. Derive macros
 * will automatically generate trait immplementations for the type it is applied to. */
fn ex4() {
    // We probably want to do this on every type we make.
    #[derive(Debug)]
    struct Coordinate {
        x: i32,
        y: i32,
    }
}

/* The reason why Derive is used so often is that it's so incredibly useful for generating a lot of
 * code with just a few tokens. */


/* Creating Our Own
 * ------------------
 *
 * Procedural macros currently are required to be in their own crate, and utilize a very different
 * approach to parsing input than declarative macros.
 *
 * While creating procedural macros is out of the scope of this course, The Rust Book has a good
 * example of How to Write a Custom derive Macro: 
 * https://doc.rust-lang.org/book/ch19-06-macros.html#how-to-write-a-custom-derive-macro
 */


