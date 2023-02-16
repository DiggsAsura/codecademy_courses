/* Conditional Loops with while
 *
 * A program will often need to evaluate a condition within a loop. While the condition is true,
 * the loop runs. When the condition ceases to be true, the program calls break, stopping the loop.
 * It's possible to implement behavior like this using a combination of loop, if, else, and break;
 * you could try that now in a program if you'd like (think i just did that in the previous
 * commit). However, this pattern is so common that Rust has a built-in language construct for it,
 * called while loop. Ane example looping from three, counting down each time, and then after the
 * loop, print a message and exit. */
fn main() {
    let mut number = 3;

    while number != 0 {
        println!("{number}!");

        number -= 1;
        std::thread::sleep_ms(1000);
    }

    println!("LIFTOFF!!!");
}

/* This construct eliminates a lot of nesting that would be necessary if you used loop, if, else,
 * and break, and it's clearer. While a conditions holds true, the code runs; otherwise, it exits
 * the loop. */

