// Methods for Iterating Over Strings
//
// The best way to operate on pieces of strings is to be explicit about wheter
// you want characters or bytes. For individual Unicode scalar values, use the chars method.
// Calling chars on "Зд" separates out and returns two values of type char, and you can
// iterate over the result to access each element:
fn main() {
    for c in "Зд".chars() {
        println!("{}", c);
    }

    ex2();
}

// Alternatively, the bytes method returns each raw byte, which might be appropriate for your
// domain:
fn ex2() {
    for b in "Зд".bytes() {
        println!("{}", b);
    }
}

// But be sure to remember that valid Unicode scalar values may be made up of more than
// 1 byte.
//
// Getting grapheme clusters from strings as with the Devanagari script is complex, so this
// functionality is not provided by the standard library. Crates are available on crates.io
// if this is the functionality you need.
