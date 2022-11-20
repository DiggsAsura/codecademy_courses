/* Raw identifiers
 * ================
 *
 * Rust, like many programming languages, has the concept of "keywords". These identifiers mean
 * something to the language, and so you cannot use them in places like variable names, function
 * names, and other places. Raw idengifiers let you use keywords where they would not normally be
 * allowed. This is particulary useful when Rust introduce new keywords, and a library using an
 * older edition of Rust has a variable or function with the same name as a keyword introduced in a
 * newer edition.
 *
 * For example, consider a crate foo compiled with the 2015 edition of Rust that exports a function
 * named try. This keyword is reserved for a new feature in the 2018 edition, so without raw
 * identifiers, we would have no way to name the funciton. */

mod foo {
    pub fn r#try() {
        println!("Hello World!");
    }
}

fn main() {
    foo::r#try();
}

