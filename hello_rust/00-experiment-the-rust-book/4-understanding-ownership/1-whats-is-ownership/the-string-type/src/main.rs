/* The String Type
 *
 * To illustrate the rules of ownership, we need a data type that is more complex than those we
 * covered in the "Data Types" section of Chapter 3. The types covered previously are all a known
 * size, can be stored on on the stack and popped off the stack when their scope is over, and can
 * be quickly and trivially copied to make a new, independent instance if another part of code
 * needs to use the same value in a different scope. But we want to look at data that is stored on
 * the heap and explore how Rust knows when to clean up that data, and the String type is a great
 * example.
 *
 * We'll concentrate on the parts of String that relate to ownership. These aspects also apply to
 * other complex data types, wheter they are provided by the standard library or created by you.
 * We'll discuss String in more depth in Chapter 8.
 *
 * We've already seen string literals, where a string value is hardcoded into our program. String
 * literals are convenient, but they aren't suitable for every situation in which we may want to
 * use text. One reason is that the're immutable. Another is that not every string value can be
 * known when we write our code: for example, what if we want to take user input and store it? For
 * these situations, Rust has a second string type, String. This type manages data allocated on the
 * heap and as such is able to store an amount of text that is unknown to us at compile time. You
 * can create a String from a string literal using the from function, like so: */

fn main() {
    let s = String::from("hello");
    println!("{s}");        // made a String from and &str

    /* The double colon :: operator allows us to namespace this particular from function under the
     * String type rather than using some sort of name like string_from. We'll discuss this syntax
     * more in the "Method Syntax" section of Chapter 5 and when we talk about namespacing with
     * modules in "Paths for Referring to an Item in the Module Tree" in Chapter 7.
     *
     * This kind of string -can- be mutated: */

    {
        let mut s = String::from("hello");
        s.push_str(", world!");                 //push_str() appends a literal to a String
        println!("{}", s);                      // This will print 'hello, world!'
    }

    /* So, what's the difference here? Why can String be mutated but literals cannot? The
     * difference is how these two types deal with memory. */
}
