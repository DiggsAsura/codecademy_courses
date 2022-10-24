/* Tuples
 * =======
 *
 * Tuples can be destructured in a match as follows: */

fn main() {
    let triple = (3, -2, 4);

    println!("Tell me about {:?}", triple);
    // Match can be used to destructure the tuple
    match triple {
        // Destructuring the second and third elements
        (0, y, z) => println!("First is '0', 'y' is {:?}, and 'z' is {:?}", y, z),
        (1, ..) => println!("First is '1' and the rest doesn't matter"),
        (.., 2) => println!("Last is '2' and the rest doesn't matter"),
        (3, .., 4) => println!("First is '3', last is '4', and the rest doesn't matter"),
        // '..' can be used to ignore the rest of the tuple
        _ => println!("It doesn't matter what they are"),
        // '_' means don't bind the value to  a variable
    }

}
