fn main() {
    ex1();
    ex2();
    ex3();
}

/* Declarative Macros
 * ===================
 *
 * The most straightforward way of creating our own macros is with macro_rules!. Macros made with
 * this special macro are known as Declarative Macros and they are a quick way for us to start
 * manipulating our source code. 
 *
 * The downside to using declarative macros is that they can be hard to debug. Even through the
 * Rust compiler is very sphisticated, we sometimes end up with erroneous errors caused by a small
 * type in a macro body. 
 *
 *
 * macro_rules!
 * -------------
 *
 * Declerative macros allow us to make the syntatic fragments of the Rust language as input and
 * then return raw source code. A big bonus of declarative macros is that they allow arbitrary
 * repetition of code.
 *
 * A macro_rules! declaration takes the following form: */

fn ex1() {
    macro_rules! make_it {
        () => {
            // Everything placed in here will be generated in source code when the macro is called. 
            print!('r')
        }
    }
    /* Here we have begun making a macro with the name make_it!. We will handle all our input
     * within() and all our output within {}.
     *
     * Let's begin making our macro print a character to stdout. ( print!('r') ) 
     *
     * A macro that takes no input is still very useful for importing large amounts of code, but
     * macros are much more powerful when we have input, so let's add some. */
}

/* Input
 * ------
 *
 * When working with macros, parameters are referred to as Metavariables, and their respective
 * types are called fragment-specifiers.
 *
 * We declare our metavariables in a similar manner as funciton parameters. However, metavariables
 * must start with $, and there can be no spaces between the metavariables, its fragment-specifier,
 * and the separating :.
 */

fn ex2() {
    macro_rules! make_it {
        ($happen:expr) => {
            println!("{}", $happen)
        }
    }

    make_it!("we did it!");
    make_it!(usize::MAX);
}

/* Here we have let our macro accept any expression which we can represent with the metavariable
 * $happen and passing it to println!(). 
 *
 * Some commonly used fragment-specifiers other than expr include ident for identifiers, stmt for
 * statements, ty for types, and literal for literals. A complete list of fragment-specifiers can
 * be found in The Rust Reference
 * https://doc.rust-lang.org/reference/macros-by-example.html
 */


/* Repetition
 * -----------
 *
 * The best part about macros is how easy it is to repeat fragments of code. We can repeat code by
 * enclosing it within $() followed by either a *, +, or ?. 
 *
 *  - * will accept any number of repetitions, including none.
 *  - + will accept any number of repetitions, bue requires at least one.
 *  - ? will accept one or no repetitions.
 *
 * Let's spice up our make_it! macro with some repetition. */

fn ex3() {
    macro_rules! make_it {
        ( $var:ident => $($count:expr),+) => {
            $($var.push($count);)+
        }
    }

    let mut count = vec![];

    make_it![count => u8::MIN, 1, 2];

    println!("{count:?}");

    /* Now we can push() a comma separated list of expressions into an existing variable. 
     *
     * By adding the , to create $(),+ in our input, we are stating that the repeated items are
     * delimited by ,. We can use any single token as a delimiter that is valid in the context of
     * nearby metavariables. */
}

/* Exporting
 * -----------
 *
 * Macros can be exported and used anywhere in our crate with the #[macro_export] attribute. This
 * also makes the macro visible to other crates when importing our crate as dependency. */

fn e4() {
    macro_rules! make_it {
        ( $var:ident => $($count:expr),+) => {
            $($var.push($count);)+
        }
    }

    /* Alternatively, we can also export all macros contained within a module with the #macro_use
     * attribute */

//    #[macro_use]
//    mod macros;

    /* Macros from external crates can be imported like any other item, but we can also utilize
     * #[macro_use] to do so.
     *
     * The examples of declarative macros we have used in this article are basic, but the concepts
     * are far reaching and can accomplish powerful things. 
     *
     * (I'm not sure if I interpret this as easy though lol)
     */
}
