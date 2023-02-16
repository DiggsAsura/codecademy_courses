/* String Slices as Parameters
 *
 * Knowing that you can take slices of literals and String values leads us to one more improvement
 * on first_word, and that's its signature:
 
 fn first_word(s: &String) -> &str {

 * A more experienced Rustacean would write the signature shown below instead because it allows us
 * to use the same function on both &String values and &str values. 
 
 fn first_word(s: &str) -> &str {

 * If we have a string slice, we can pass that directly. If we ahve a String, we can pass a slice
 * of the String or a reference to the String. This flexibility takes advantages of deref coercions, a feature we will cover in Chapter 15. Defining a function to take a string slice instead of a reference to a String makes our API more genral and useful without losing any functionality:
 */

fn first_word(s: &str) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }

    &s[..]
}

fn main() {
    let my_string = String::from("hello world");

    // 'first_word' works on slices of 'String's, wheter partial or whole
    let word = first_word(&my_string[0..6]);
    let word = first_word(&my_string[..]);
    // 'first_word' also works on references to 'String's, which are equivalent
    // to whole slices of 'String's
    let word = first_word(&my_string);

    let my_string_literal = "hello world";

    // 'first_word' works on slices of string literals, whter partial or whole
    let word = first_word(&my_string_literal[0..6]);
    let word = first_word(&my_string_literal[..]);

    // Because string literals *are* string slices already,
    // this works too, without the slice syntax!
    let word = first_word(my_string_literal);
}
