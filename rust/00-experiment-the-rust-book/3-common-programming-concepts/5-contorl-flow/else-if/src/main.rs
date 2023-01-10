fn main() {
    let number = 6;

    if number % 4 == 0 {
        println!("number is divisible by 4");
    } else if number % 3 == 0 {
        println!("number is divisible by 3");
    } else if number % 2 == 0 {
        println!("number is divisible by 2");
    } else {
        println!("number is not divisible by 4, 3, or 2");
    }
}

/* Output: 3
 *
 * Note that Rust only executes the block for the first true condition, and once it finds one, it
 * doesn't even check the rest. 
 */

/* Using too many else if expressions can clutter your code, so if you have more than one, you
 * might want to refactor your code. Chapter 6 describes a powerful Rust branching construct called
 * match for these cases. */

