/* Ways Variables and Data Interact: Clone
 * -----------------------------------------
 *
 * If we -do- want to deeply copy the heap data of the String, not just the stack data, we can use
 * a commont method called clone. We'll discuss method syntax in Chapter 5, but because methods are
 * a common feature in many programming languages, you've probably seen them before.
 *
 * Here's an example of the clone method in action:
 *
 */

fn main() {
    // Clone method in action
    {
        let s1 = String::from("hello");
        let s2 = s1.clone();

        println!("s1 = {}, s2 = {}", s1, s2);
    }
    /* This works just fine and explicitly produces the behavoir shown in figure 4-3 (where S1 and
     * S2 have separate heap data), where the heap data -does- get copied. 
     *
     * When you see a call to clone, you know that some arbitrary code is being executed and that
     * code may be expensive. It's a visual indicator that something different is going on. */


/* Stack-Only Data: Copy
 * ------------------------
 *
 * There's another wrinkle we hvaen't talked about yet. This code using integers - part of which
 * was shown in listing 4-2 - works and is valid: */
    {
        let x = 5;
        let y = x;
    
        println!("x = {}, y = {}", x, y);
    }
    /* But this code seems to contradict what we just learned: we don't have to call clone, but x
     * is still valid and was not moved into y.
     *
     * The reason is that types such as integers that have a known size at compile time are stored
     * entirely on the stack, so copies of the actual values are quick to make. That means there's
     * no reason we would want to prevent x from being valid after we create the variable y. In
     * other words, there's no difference between deep and shallow copying here, so calling clone
     * wouldn't do anything different from the usual shallow copying and we can leave it out.
     * (also int's impelemtn the Copy trait, while String does not).
     *
     * Rust has a special annotation called the Copy trait that we can place on types that are
     * stored on the stack, as integers are (we'll talk more about traits in Chapter 10). If a type
     * implements the Copy trait, variables that use it do not move, but rather are trivially
     * copied, making them still valid after assignment to another variable. 
     *
     * Rust won't let us annotate a type with Copy if the type, or any of its part, has implemented
     * the Drop trait. If the type needs something special to happen when the value goes out of
     * scope and we add the Copy annotation to that type, we'll get a compile-time error. To learn
     * about how to add the Copy annotation to your type to implement the trait, see "Derivable
     * Traits" in Appendix C.
     *
     * So what types implement the Copy trait? You can check the documentation for the given type
     * to be sure, but as a general rule, any group of simple scalar values can implement Copy, and
     * nothing that requires allocation or is some from of resource can implement Copy. Here are
     * some of the types that implement Copy:
     *
     *  - All the integer types, such as u32
     *  - The Boolean type, bool, with values true and false
     *  - All the floating point types, such as f64
     *  - The character type, char
     *  - Tuples, if they only contain types that also implement Copy. For example, (i32, i32)
     *  implements Copy, but (i32, String) does not. */

    // Does &str implement copy?
    {
        let s1: &str = "hello";
        let s2 = s1;
        let s3 = s1.to_owned() + s2;

        println!("{s1}, {s2}, {s3}");
    }

}
