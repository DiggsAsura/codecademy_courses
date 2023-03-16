// Multiple Patterns
// =================
//
// In match expressions, you can match multiple patterns using the | syntax, which is the pattern
// or operator. For example, in the following code we match the value of x against the match arms,
// the first fo which has an or option, meaning if the value of x matches either of the values in
// the arm, the arm's code will run:

fn main() {
    let x = 1;

    match x {
        1 | 2   => println!("one or two"),
        3       => println!("three"),
        _       => println!("anything"),
    };
}

// This code prints one or two.
