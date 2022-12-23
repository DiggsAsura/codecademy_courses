// Indexing into Strings
//
// In many other programming languages, accessing individual characters is a string by
// referencing them by index is a valid and common operation. However, if you try to access
// parts of a String using indexing syntax in Rust, you'll get an error. Consider
// the invalid code in Listing 8-19.
fn main() {
    let s1 = String::from("hello");
    //let h = s1[0];
}
// 8-19: Attempting to use indexing syntax with a String

// This code will not compile because Rust strings don't support indexing. If you need to
// access individual characters in a string, use the chars method to return an iterator over
// the characters of the string. The next code example shows how to use the chars method to
// access the first character of a string.
//
// The error and the note tell the story: Rust strings don't support indexing. But why not?
// To answer that question, we need to discuss how Rust stores strings in memory.
//
//
// Internal Representation
//
// A string is a wrapper over Vec<u8>. Let's look at some of our properly encoded UTF-8
// example strings from Listing 8-14. First, this one:
//
// let hello = String::from("Hola");
//
// In this case, len will be 4, which means the vector storing the string "Hola" is 4 bytes long.
// Each of these letters takes 1 bytes when encoded in UTF-8. The following line, however,
// may surprise you. (Note that this string begins with the captital Cryllic letter Ze, not
// the Arabic number 3.)
//
// let hello = String::from("Здравствуйте");
//
// Asked how long this string is, you might say 12. In fact, Rust's answer is 24: that's
// the number of bytes it takes to encode "Здравствуйте" in UTF-8, because each Unicode
// scalar value in that string takes 2 bytes of storage. Therefore, an index into the string's
// bytes will not always correlate to a valid Unicode scalar value. To demonstrate,
// consider this invalid Rust code:
//
// let hello = "Здравствуйте";
// let answer = &hello[0];
//
// You already know that answer will not be З, the first letter. When encoded in UTF-8, the
// first byte of 3 is 208 and the second is 151, so it would seem that anser should in fact
// be 208, but 208 is not a valid character on its ovwn. Returning 208 is likely not what
// a user would want if they asked for the first letter of this string; however, that's the
// only data that Rust has at byte index 0. Users generally don't want the byte value returned,
// even if the string contains only Latin letters: if &"hello"[0] were valid code that returned
// the byte value, it would return 104, not h.
//
// The answer, then, is that to avoid returning an unexpected value and causing bugs
// that might not be discovered immediately, Rust doesn't compile this code at all and prevents
// misunderstandings early in the development process.
//
//
// Bytes and Scalar Values and Grapheme Clusters! Oh My!
//
// Another point about UTF-8 is that there are actually three relevant ways to look at
// strings from Rust's perspective: as bytes, scalar values, and grapheme clusters (the
// closest thing to what we would call letters).
//
// If we look at the Hindi word नमस्ते written in the Devanagari script, it is stored as a
// vector of u8 values that look like this:
//
// [224, 164, 168, 224, 164, 174, 224, 164, 184, 224, 165, 141, 224, 164, 164, 224, 165, 135]
//
// That's 18 bytes and is how computers ultimately store this data. If we look at them as Unicode
// scalar values, which are what Rust's char type is, those bytes look like this:
//
// ['न', 'म', 'स', '्', 'त', 'े']
//
// There are six char values here, but the fourth and sixth are not letters: they're
// diacritics that don't make sense on their own. Finally, if we look at them as grapheme
// clusters, we'd get what a person would call the four letters that make up the Hindi word:
//
// ["न", "म", "स्", "ते"]
//
// Rust provides different ways of interpreting the raw string data that computers store
// so that each program can choose the interpretation it needs, no matter what human language
// the data is in.
//
// A final reason Rust doesn't allow us to index into a String to get a character is that
// indexing operations are expected to always take constatnt time (0(1)). But it isn't
// possible to guarantee that performance with a String, because Rust would have to walk through
// the contents from the beginning to the index to determine how many valid characters there
// were.
