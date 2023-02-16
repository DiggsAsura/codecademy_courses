/* Variable Scope
 * ----------------
 *
 * As a first example of ownership, we'll look at the scope of some variables. A scope is the range
 * within a program for which an item is valid. Take the following variable: */
fn main() {
    let s = "hello";

/* The variable s refers to a -string literal-, where the value of the string is hardcoded into the
 * text of our program. The variable is valid from the point at which it's declared until the end
 * of the current scope.  */

    {                           // s is not valid here, its's not yet declared
        let s = "hello";        // s is valid from this point forward

        // do stuff with s
        println!("{s}");
    }                           // the scope is now over, and s is no longer valid
}

/* So:
 *  - When s comes into scope, it is valid
 *  - It remains valid until it goes out of scope
 *
 * At this point, the relationship between scopes and when variables are valid is similar to that
 * in other programming languages. Now we'll build on top of this understanding by introducing the
 * String type. */

