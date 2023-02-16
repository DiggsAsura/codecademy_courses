/* Functions with Return Values
 * -----------------------------
 *
 * In Rust, the return value of the function is synonymous with the value of the final expression
 * in the block of the body of a function. You can return early from a function using the return
 * keyword and specifying a value, but most functions return the last expression implicitly. Here's
 * an example of a function that returns a value: */

fn five() -> i32 {
    5                   // Expression, with no semicolon; With semicolon, it would be a statement
}

fn plus_one(x: i32) -> i32 {
    x + 1
}

fn main() {
    let x = five();
    println!("The value of x is: {x}");

    let y = plus_one(5);
    println!("The value of y is: {y}");
}

/* using a semicolon at the end of the last expression, will result in a error if you specifided a
 * -> return_type. */

