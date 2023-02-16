/* Return Values and Scope
 * ---------------------------
 *
 * Returning values can also transfer ownership. Listing 4-4 shows an example of a function that
 * returns some value, with similar annotations as those in Listing 4-3 (last commit).
 */

fn main() {
    let s1 = gives_ownership();         // gives_ownership moves its return value into s1

    let s2 = String::from("hello");     // s2 comes into scope

    let s3 = takes_and_gives_back(s2);  // s2 is moved into takes_and_gives_back, which also moves
                                        // its return value into s3
    


    listing_4_5();
}       // here, s3 goes out of scope and is dropped. s2 was moved, so nothing happens. s1 goes out
        // of scope and is dropped.

fn gives_ownership() -> String {                // gives_ownership will move its return value into
                                                // the function that calls it.

    let some_string = String::from("yours");    // some_string comes into scope

    some_string                                 // some_string is returned and moves out to the
                                                // calling function
}

// This function takes a String and returns one
fn takes_and_gives_back(a_string: String) -> String {   // a_string comes into scope

    a_string    //  a_string is returned and moves out to the calling function
}

/* The ownership of a variable follows the same pattern every time: assigning a value to another
 * variable moves it. When a variable that includes data on the heap goes out of scope, the value
 * will be cleaned up by drop, unless ownership of the data has been moved to another variable. 
 *
 * While this works, taking ownership and then returning ownership with every fucntion is a bit
 * tedious. What if we want to let a function use a value but not take ownership? It's quite
 * annoyting that anything we pass in also neesd to be passed back if we want to use it again, in
 * addition to any data resulting from the body of the function that we might want to return as
 * well.
 *
 * Rust does let us return multiple values using a tuple, as shown:
 */

fn listing_4_5() {
    let s1 = String::from("hello");

    let (s2, len) = calculate_length(s1);

    println!("The length of {} is {}.", s2, len);
}

fn calculate_length(s: String) -> (String, usize) {
    let length = s.len(); // len() returns the length of a String

    (s, length)
}

/* But this is too much ceremony and a lot of work for a concept that should be common. Luckily for
 * us, Rust has a feature for using a valus without transferring ownership, called references.
 */
