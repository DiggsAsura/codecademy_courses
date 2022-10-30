/* dead_code
 * ===========
 *
 * The compiler proivdes a dead_code lint (https://en.wikipedia.org/wiki/Lint_%28software%29) that
 * will warn about unused functions. An attribute can be used to disable the lint. */

fn used_function() {}

// #[allow(dead_code)] is an attrubute that disables the 'dead_code' lint
#[allow(dead_code)]
fn unused_function() {}

#[allow(dead_code)]
fn noisy_unused_function() {}
// FIXME^Ad an attribute to suppress the warning

fn main() {
    used_function();
}

/* Note that in real programs, you should eliminate dead code. In these examples we'll allow dead
 * code in some places because of the interactive nature of the examples. */
