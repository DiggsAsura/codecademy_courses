fn main() {
    ex1();
}

/* crates.io
 * ==========
 *
 * Thanks to Cargo, we are not limited to the std library. When we import crate, such as serde in
 * our manifest file, these libraries are pulled from a registry of source code located at
 * crates.io.
 *
 *
 * Finding Crates
 * ---------------
 *
 * When we are looking for a crate with particular functionality, we can search through all
 * available crates directly at the crates.io website. Crates are indexed by name, keywords, and
 * descriptions as declared in the manifest. 
 *
 * To test this out, let's pretend that we thought of a great idea for a command line application.
 * We can start out by searching the term "cli" which will then supply us with a multitude of
 * libraries such as clap that we can use to help us build  our command-line applications.
 *
 * Each crate has its own page with download statistics, links to the active repository, and links
 * to the documentation. Cargo has its own subcommand 'search' which allows us to search through
 * the registry with the command line, 'cargo search serde'.
 *
 *
 * Publishing a Crate
 * -------------------
 *
 * When we have created a binary or library that we wish to share with others, we can choose to
 * publish our own crate to crates.io.
 *
 * There are a few things to keep in mind when publishing a crate. 
 *
 *  - Remove all sensitive information from within your source code before publishing.
 *
 *  - It is recommended to follow semantic versioning. j
 *
 *  - The - and _ character are interchangeable within crate names.
 *
 *  - You cannot publish a crate that has dependencies linked to a git repository.
 *
 *  - Providing useful descriptions and documentation will help people find and utilize your crate. 
 *
 *
 * Once you have written a crate that you feel confident in sharing, make sure the name of your
 * crate is available, and then run the 'cargo publish' command to publish your crate to the ages. 
 *
 *
 * Security Implications
 * ----------------------
 *
 * Even though Rust as a language provides a great deal of inherent safety, external libraries are
 * not inherently safe. Any piece of source code can be malicious, so to keep your code safe, it is
 * wise to keep dependencies to a minimum and trust the crates you use. 
 *
 * If you are choosing to import a new crate that is not yet popular, take a quick look at the
 * dependencies and source code of the crate. This is a great way to make sure your code is safe
 * and also a great way to learn!
 *
 * There are also tools such as 'cargo crev' which are attempmts to build a web of trust regarding
 * crate usage.
 */

fn ex1() {
    println!("Ups nothing here");
}
