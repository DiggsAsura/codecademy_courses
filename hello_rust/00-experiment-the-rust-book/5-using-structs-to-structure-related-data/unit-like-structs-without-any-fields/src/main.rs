/* Unit-Like Structs Without Any Fields
 *
 * You can also define structs that don't have any fields! These are called unit-like structs
 * because they behave similarly to (), the unit type that we have mantioned in the Tuple Type
 * section. Unit-like structs can be useful when you need to implement a trait on some type but
 * don't have any data that you want to store in the type itself. We'll discuss traits in Chapter
 * 10. Here's an example of declaring and instantiating a unit struct named AlwaysEqual: */

struct AlwaysEqual;

fn main() {
    let subject = AlwaysEqual;
}

/* To define AlwaysEqual, we use the struct keyword, the name we want, then a semicolon. No need
 * for curly brackets or parantheses! Then we can get an sintance of AlwaysEqual in the subject
 * variable in a similar way: using the name we defined, without any curly brackets or parantheses.
 * Imagine that later we'll implement behavior for this type such that every instance of
 * AlwaysEqual is always equal to every instance of any other type, perhaps to have a known result
 * for testing purposes. We wouldn't need any data to implement that behavior! You'll see in
 * Chapter 10 how to define traits and implement them on any type, including unit-like structs. */

