/* Repetition with Loops
 *
 * Rust has three kinds of loops: loop, while, and for. 
 */

fn main() {
    let mut i: i128 = 0;
    loop { 
        println!("{i} again!");
        i += 1;
        if i == 101 {
            break;
        }
    }
}
