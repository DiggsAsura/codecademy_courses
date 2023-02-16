/* Flow of Control
 * =================
 *
 * An essential part of any programming language are ways to modify control flow: if/else, for, and
 * others. Let's talk about them in Rust. */

fn main() {
    let hello_vec = vec!["hello", "world"];

    for word in hello_vec {
        println!("{word}");
    }
}
