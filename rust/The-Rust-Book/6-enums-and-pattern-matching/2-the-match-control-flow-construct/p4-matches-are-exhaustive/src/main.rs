/* Matches are Exhaustive
 *
 * There's one other aspect of match we need to discuss: the arms' patterns must cover all
 * possibilities. Consider this version of our plus_one function, which has a bug and won't
 * compile:
 *
 *  fn plus_one(x: Option<i32>) -> Option<i32> {
 *    match x { 
 *        Some(i) => Some(i + 1),
 *    }
 *  }
 *
 * We didn't handle the None case, so this code will cause a bug. Luckily, it's a bug Rust knows
 * how to catch. If we try to compile this code, we'll get this error:
 *
 * $ cargo run
   Compiling enums v0.1.0 (file:///projects/enums)
error[E0004]: non-exhaustive patterns: `None` not covered
   --> src/main.rs:3:15
    |
3   |         match x {
    |               ^ pattern `None` not covered
    |
note: `Option<i32>` defined here
    = note: the matched value is of type `Option<i32>`
help: ensure that all possible cases are being handled by adding a match arm with a wildcard pattern or an explicit pattern as shown
    |
4   ~             Some(i) => Some(i + 1),
5   ~             None => todo!(),
    |

For more information about this error, try `rustc --explain E0004`.
error: could not compile `enums` due to previous error
*/

/* Rust knows that we didn't cover every possible case and even knows which pattern we forgot!
 * Mtaches in Rust are exhaustive: we must exhaust every last possibility in order for the code to
 * be valid. Especially in the case of Option<T>, when Rust prevents us from forgetting to
 * explicitly handle the None case, it protects us from assuming that we have a value when we might
 * have null, thus making the billion-dollar mistake discussed earlier impossible. */

fn main() {
    println!("Hello, world!");
}
