// Concise Control Flow with if let

/* The if let syntax lets you combine if and let into a less verbose way to handle values that
 * match one pattern while ignoring the rest. Consider the program here, that matches on an
 * Opttion<u8> value in the confix_max variable but only wants to execute code if the value is the
 * Some variant. */

fn main() {
    let config_max = Some(3u8);
    match config_max {
        Some(max) => println!("The maximum is configured to be {}", max),
        _ => (),
    }

    ex2();
    ex3();
    ex4();
}

/* If the values is Some, we print out the value in the Some variant by binding the value to the
 * variable max in the pattern. We don't want to do anything with the None value. To staisfy the
 * match expression, we have to add _ => () after processing just one variant, which is annoying
 * boilerplate code to add. 
 *
 * Instead, we could write this in a shorter way using if let. The following code behaves the same
 * as the match above: */

fn ex2() {
    let config_max = Some(5u8);
    if let Some(max) = config_max {
        println!("The maximum is configured to be {}", max);
    }
}

// to avoid boilerplate code. 

/* The syntax if let takes a pattern and an expression separated by an equal sign. It works in the
 * same way as a match, where the expression is given to the match and the pattern is its first
 * arm. In this case, the pattern is Some(max), and the max binds to the value inside the Some. 
 *
 * Using if let means less typing, less indentation and less bilerplate. However, you lose the
 * exhaustive checking that match enforces. Choosing between match and if let depends on what
 * you're doing in your particular situation and wheter gaining conciseness is an appropriate
 * trade-off for losing exhaustive checking.
 *
 * In other words, you can think of if let as a syntax sugar for a match that runs code when the
 * value matches one pattern and then ignores all other values.
 *
 * We can include an else with an if let. The block of code that goes with the else is the same as
 * the block of code that would go with the _ case in the match expression that is equivalent to
 * the if let and else. Recall the Coin enum definition previously, where the Quarter variant also
 * held a UsState value. If we wanted to count all non-quarter coins we see while also announcing
 * the state of the quarters, we could do that with a match expression like this: */

#[derive(Debug)] // so we can inspect the state in a minute
enum UsState {
    Alabama,
    Alaska,
    // --snip--
}

enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter(UsState),
}

fn ex3() {
    let mut count = 0;

    let coin = Coin::Quarter(UsState::Alaska);

    match coin {
        Coin::Quarter(state) => println!("State quarter from {:?}!", state),
        _ => count += 1,
    }
}

fn ex4() {
    let mut count = 0;

    let coin = Coin::Quarter(UsState::Alaska);

    if let Coin::Quarter(state) = coin {
        println!("State quarter from {:?}!", state);
    } else {
        count += 1;
    }
}

// If you have a situation in which your program has logic that is too verbose to express using a
// match, remember that if let is in your Rust toolbox as well. 

