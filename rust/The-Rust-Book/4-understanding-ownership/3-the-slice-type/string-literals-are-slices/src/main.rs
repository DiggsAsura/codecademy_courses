/* String Literals are Slices
 *
 * Recall that we talked about string literals being stored inside the binary. Now that we know
 * about slices, we can properly understand string literals:
 *
let s = "Hello, world!";
 * 
 * The type of s here is &str: it's slice pointing to that specific point of the binary. This is
 * also why string literals are immutable; &str is an immutable reference. 
 *
 */

fn main() {
    let s = "Hello, world!";
    println!("{s}");
}
