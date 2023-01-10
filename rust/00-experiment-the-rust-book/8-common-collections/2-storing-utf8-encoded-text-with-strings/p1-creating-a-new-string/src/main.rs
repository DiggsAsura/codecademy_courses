// Creating a New String
//
// Many of the same operations available with Vec<T> are available with String as well,
// because String is actually implemented as a wrapper around a vector of bytes with some
// extra guarantees, restrictions, and capabilities. And example of a function that
// works the same way with Vec<T> and String is the new function to create an insteance,
// shown in Listing 8-11:

fn main() {
    let mut s = String::new();
}
// 8-11: Creating a new, empty String

// This line creates a new empty string called s, which we can then load data into. Often,
// we'll have some initial data that we want to start the string with. For that, we use the
// to_string method, which is available on any type that implements the Display trait,
// as string literals do. Listing 8-12 shows two examples.
fn listing_8_12() {
    let data = "initial contents";
    let s= data.to_string();

    // the method also works on a literal directly:
    let s = "initial contents".to_string();
}
// 8-12: Using the to_string method to create a String from a string literal

// This code creates a string containing initial contents.
//
// We can also use the function String::from to create a String from a string literal.
// The code in Listing 8-13  is equivalent to the code in listing 8-12 that uses to_string.
fn listing_8_13() {
    let s = String::from("initial contents");
}
// 8-13: Using the String::from function to create a String from string literal

// Because strings are used for so many things, we can use many different generic APIs
// for strings, providing us with a lot of options. Some of them can seem redundant, but
// they all have their place! In this case, String::from and to_string do the same thing, so
// which you choose is a matter of style and readability.
//
// Remember that strings are UTF-8 encoded, so we can include any properly encoded data
// in them, as shown in Listing 8-14.

fn listing_8_14() {
    let hello = String::from("السلام عليكم");
    let hello = String::from("Dobrý den");
    let hello = String::from("Hello");
    let hello = String::from("שָׁלוֹם");
    let hello = String::from("नमस्ते");
    let hello = String::from("こんにちは");
    let hello = String::from("안녕하세요");
    let hello = String::from("你好");
    let hello = String::from("Olá");
    let hello = String::from("Здравствуйте");
    let hello = String::from("Hola");
}

// 8-14: Storing greetings in different languages in strings

// All of these are valid String values.
