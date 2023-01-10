/* Loop Labels to Disambiguate Between Multiple Loops
 *
 * If you have loops within loops, break and continue apply to the innermost loop at that point.
 * You can optionally specify a -loop label- on a loop that we can then use with break or contine
 * to specify that those keywords apply to the labeled loop instead of the innermost loop. Loop
 * labels must begin with a single quote. Here's an example with two nested loops: */

fn main() {
    let mut count = 0;
    'counting_up: loop {
        println!("count = {count}");
        let mut remaining = 10;

        loop {
            println!("remaining = {remaining}");
            if remaining == 9 {
                break;
            }
            if count == 2 {
                break 'counting_up;     // This just sounds somewhat genious :D
            }
            remaining -= 1;
        }

        count += 1;
    }
    println!("End count = {count}");
}

/* The outer loop has the label 'counting_up, and it will count up from 0 to 2. The inner loop
 * without label counts down from 10 to 9. The first break that doesn't specify a label will exit
 * the inner loop only. The break 'counting_up; statement will exit the outer loop. */


