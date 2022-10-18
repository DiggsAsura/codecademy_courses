fn main() {
    ex1();
}

/* Tooling
 * ========
 *
 * Most programming languages require more than just a compiler to manage all of the moving parts
 * of the development process. With things such as external dependencies, documentation, and even
 * managing different versions of the compiler itself, it's sensible to have tools to help with
 * these aspects. 
 *
 * Luckily, the creators of Rust understood the importance of tooling and developeped rustup and
 * cargo to help make development painless. These tools are one of the many reasons Rust receives
 * so much praise and love from the programming community. 
 *
 *
 * Rustup
 * -------
 *
 * rustup allows us to update and manage different versions of the rustc compiler. When a new
 * version of Rust is released, we can update our compiler with the shell command rustup update.
 *
 * By default, we are supplied with the "stable" toolchain, but if you are looking to experiment
 * with unstable features, there are also "beta" and "nightly" toolchains.
 * To try out nightly features, we can switch toolchains with the command 'rustup default nightly'. 
 *
 * For information about all of rustup's functionality, try the command rustup --help.
 *
 *
 * Cargo
 * ------
 *
 * cargo is Rust's jack-of-all tools. It can help us manage external dependencies, run tests,
 * configure compiler settings and even install Rust binaries to our system. All of these features
 * exist as subcommands to the cargo binary.
 *
 * Lets take a look at the most commonly used subcommands.
 *
 * new
 * ----
 *
 * We can create package with the cargo new command. Libraries can be indicated with the --lib
 * flag.
 *
 *  # Create a new binary crate
 *  cargo new my_binary
 *
 *  # Create a new library crate
 *  cargo new --lib my_library
 *
 *
 * build and run
 * --------------
 *
 * We can ask Cargo to compile our crate with the command cargo build. 
 *
 * # Build binary/library
 * cargo build
 *
 *
 * If our crate is a binary executable, we can run the binary upon successful compilation with
 * cargo run. 
 *
 * # Run binary
 * cargo run
 *
 *
 *
 * fmt
 * ----
 *
 * Rust has a convention for how code should be formatted. We can have cargo format our entire
 * crate to meet these conventions with the cargo fmt command. 
 *
* Internally, this calls the command rustfmt, which we can also be used to format a special file. 
*
* # Format our 'main.rs' file
* furstfmt src/main.rs
*
*
* doc
* ----
*
* Cargo has an automated system for generating HTML-based documentation for your crate with the
* cargo doc command. We can generate and open our crate's documentation with cargo doc --open.
*
* For more information about how documentation is generated, check out the documentation article.
*
*
* test
* -----
*
* Rust has an entire system built into the language dedicated for tests. We can run the tests in
* our crate with the cargo test command.
*
* For more information about testing check out The Rust Book 
* https://doc.rust-lang.org/stable/book/ch11-01-writing-tests.html?highlight=test#the-anatomy-of-a-test-function
*
*
* Other tools
* -------------
*
* The Rust community has created even more helpful tools which act as subcommands to cargo. 
*
* Once you are comfortable writing in Rust, look through the crates.io article and check out these
* great community-made subcommands
*
* cargo edit
* cargo watch
* cargo expand
* cargo make
* cargo geiger
* cargo crev
*/


