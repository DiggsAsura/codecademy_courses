/* The match Control Flow Construct
 *
 * Coin into coin machine example: 
 */

enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter,
}

fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => 1,
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter => 25,
    }
}

fn main() {
    let coin = Coin::Quarter;
    let value = value_in_cents(coin);
    println!("Value of coin is: {}", value);

    let coin = Coin::Penny;
    let lucky = value_in_cents2(Coin::Penny);
    println!("{}", lucky);
}

/* Let's break down the match in the value_in_cents function. First, we list the match keyword
 * followed by an expression, which in this case is the value coin. This seems very similar to an
 * expression used with if, but there's a big difference: with if, the expression needs to return a
 * Boolean value, but here, it can return any type. The type of coin in this example is the Coin
 * enum that we defined on the first line.
 *
 * Next are the match arms. An eam has two parts: a pattern and some code. The first arm here has a
 * pattern that is the value Coin::Penny and then the => operator that separates the pattern and
 * the code to run. The code in this case is just the value 1. Each arm is separated from the next
 * with a comma. 
 *

 match this {
    -----------Expression -------------,
    pattern => ------------------------,
    ------- => code to run/return value,
    pattern => code to run/return value,
    _ => code to run/return value,
}

*
* When the match expression executes, it compares the resulting value against the pattern of each
* arm, in order. If a pattern matches the value, the code associated with the pattern is executed.
* If the pattern doesn't match the value, execution continues to the next arm, much as in a
* coin-sorting maching. We can have as many arms as we need: this example had 4 arms.
*
* The code associated with each arm is an expression, and the resulting value of the expression in
* the matching arm is the value that gets returned from the entire match expression.
*
* We don't typically use curly brackets if the match arm code is short, as in the previous example
* where each arm just returns a value. If you want to run mutiple lines of code in a match arm, you
* must use curly brackets, and the comma following the arm is the optional. For example, the
* following code prints "Lucky penny!" every time the method is called with a Coin::Penny, but
* still returns the last value of the bloclk 1: */

fn value_in_cents2(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => {
            println!("Lucky penny!");
            1
        },
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter => 25,
    }
}

