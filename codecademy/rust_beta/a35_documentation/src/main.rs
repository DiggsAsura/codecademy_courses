fn main() {
    ex1();
}

/* Documentation
 * ===============
 *
 * A good codebase involves more than just good code. If you have ever contributed to open-source
 * software or collaborated with other programmers, you may have noticed how crucial documentation
 * can be. If our library is well documented and structured, we help make the lives of fellow
 * contributors and users of our library that much better.
 *
 *
 * Comments
 * ---------
 *
 * The quickest way to annotate code in Rust is to make a comment with //.
 * Anything on a line proceeding // will be ignored by the compiler.
 */

fn ex1() {
    // this is in the southern hemisphere
    let latitude = -22.8746892;

    fn travel() {
        // TODO: We need to finish this before the 1.0 release
    }
}

/* These comments are good for making small annotations in our codebase but are only viewable in
 * the source code directly. */


/* Doc Comments
 * --------------
 *
 * Comments which are meant to provide documentation describing functions, types, traits and
 * modules are referred to as doc comments. There are both inner doc comments (//!) and outer doc
 * comments (///).
 */

//! If we are in main.rs, this comment will be shown in the index of our documentation.

/// This comment describes the 'Land' trait.
/// It is used to gather pertinent environmental conditions from a geographic location.
pub trait Land {
    /// Returns the average yearly rainfall in 'cm'.
    fn avg_rainfall(&self) -> u32;
    /// Returns the name of hardinthe ess zone the land resides in.
    fn hardiness_zone(&self) -> String;
}

/* We can also provide markdown formatting within our doc comments to style our text when utilizing
 * the command 'cargo doc'.
 *
 *
 * cago doc
 * ----------
 *
 * Cargo provides the doc subcommand which will compile our code, read all doc comments, and then
 * translate them into a website for you to more easily navigate your source code. By running the
 * 'cargo doc --open' command in our project directory, Cargo will compile and open our HTML-based
 * documentation for us. 
 *
 * All of the documentation for the std_library and decomuntation found at docs.rs is built using
 * this command. 
 *
 *
 * Writing Good Documentation
 * ----------------------------
 *
 * Writing code like anything in life. If it's organized and sensible, life is much easier. If you
 * take shortcuts that you then forget and call your toaster a cat, you might confuse some people. 
 *
 * There are conventions which are useful to follow. We should also remember that what makes sense
 * to one person might still be unclear to another. We should try to write documentation to help
 * bridge this gap.
 */

