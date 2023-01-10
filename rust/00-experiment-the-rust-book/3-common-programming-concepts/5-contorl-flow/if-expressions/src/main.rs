/* if Expreesions
 *
 * An if expression allows you to branch your code depending on conditions. You provide a condition
 * and then state, "if this condition is met, run this block of code. If the condition is not met,
 * do not run this block of code."
 *
 * -- The reason I write this, is to see if I can understand why it's called an if Expression, not
 * an if Statement - based on the expression/statement lesson earlier. I don't see it though -
 * unsless it's just because of the { curly brackets } */

fn main() {
    let number = 3;

    if number < 5 {
        println!("condition was true");
    } else {
        println!("condition was false");
    }

    ex2();
}

/* Blocks of code associated with the conditions in if expressions are sometimes called arms (def
 * done a lot with match). */

/* else expression is optional */

/* It's also worth noting that the condition in this code must be a bool. If condition isnt a bool,
 * we'll get an error. For example, try running the following code will error:
 *
 * let number = 3;
 *
 * if number {
 *     println!("number was three");
 * }
 *
 *
 * The error will indicate that Rust expected a bool but got an integer. Unlike languages such as
 * Ruby and JavaScript, Rust will not automatically try to convert non-Boolean types to a Boolean.
 * You must explicit and always provide if with a Boolean as its condition. If we want the if code
 * block to run only when a number is not equal to 0, for example, we can change the if expression
 * to the following:
 */

fn ex2() {
    let number = 3;
    if number != 0 {
        println!("number was something other than zero");
    }
}

