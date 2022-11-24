/* The Character Type
 *
 * char is the language's most primitive alphabetic type. 
 *
 * Note that we specify char literals with single quotes, as opposed to string literals, which use
 * double quotes. Rust's char type is four bytes in size and represents a Unicode Scalar Value,
 * which means it can represent a lot more than just ASCII. Unicode Scalar Value. Remember that. 
 *
 * Accented letters; Chinese, Japanese, and Korean characters; emoji; and zero-width spaces are all
 * valid char values in Rust. Unicode Scalar Values range from U+0000 to U+D7FF and U+E000 to
 * U+10FFFF inclusive. However, a "character" isn't really a concept of Unicode, so your human
 * intuition for what a "character" is may not match up with what a char is in Rust. More in Chap
 * 8. */

fn main() {
    let c = 'z';
    let z: char = 'ℤ';  // with explicit type annotation
    let heart_eyed_cat = '😻';
}
