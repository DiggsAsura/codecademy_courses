// All The Places Patterns Can Be Used
// ====================================
//
// Patterns pop up in a number of places in Rust, and you've been using them a lot without
// realizing it! This section discuss all the places where patterns are valid.
//
//
// match Arms
// ----------
//
// As discussed in Chapter 6, we use patterns in the arms of match expressions. Formally, match
// expressions are defined as the keyword match, a value to match on, and one or more match arms
// that consists of a pattern and an expression to run if the value matches that arm's pattern,
// like this:
//
//
// match VALUE {
//    PATTERN => EXPRESSION,
//    PATTERN => EXPRESSION,
//    PATTERN => EXPRESSION,
// }
//
//
// For example, here's the match expression from Listing 6-5 that matches on an Option<i32> value
// in the variable x:

fn ex1() {
    let x = Some(5);

    match x {
        None => None,
        Some(i) => Some(i + 1),
    };
}

// The patterns in this match expression are the None and Some(i) on the left of each arrow.
//
// One requirement for match expressions is that they need to be exhaustive in the sense that all
// possibilities for the value in the match expression must be accounted for. One way to ensure
// you've covered every possibility is to have a catchall pattern for the last arm: for example, a
// variable name matching any value can never fail and thus covers every remaining case.
//
// The particular pattern _ will match anything, but it never binds to a variable, so it's often
// used in the last match arm. The _ pattern can be useful when you want to ignore any value not
// specified, for example. We'll cover the _ pattern in more detail in the "Ignoring Values in a
// Pattern" section later in this chapter.



// Conditional if let Expressions
// ------------------------------
//
// In Chapter 6 we discussed how to use if let expressions mainly as a shorter way to write the
// equivalent of a match that only matches one case. Optionally, if let can have a corresponding
// else containing code to run if the pattern in the if let doesn't match.
//
// Listing 18-1 shows that it's also possible to mix and match if let, else if, and else if let
// expressions. Doing so gives us more flexibility than a match expression in which we can express
// only one value to compare with the patterns. Also, Rust doesn't require that the conditions in a
// series of if let, else if, else if let arms relate to each other.
//
// The code in Listing 18-1 determines what color to make your background based on a series of
// checks for several conditions. For this example, we've created variables with hardcoded values
// that a real program might receive from user input.

fn ex2() {
    let favorite_color: Option<&str> = Some("Greenish");
    let is_tuesday = false;
    let age: Result<u8, _> = "34".parse();

    if let Some(color) = favorite_color {
        println!("Using your favorite color, {color}, as the background");
    } else if is_tuesday {
        println!("Tuesday is green day!");
    } else if let Ok(age) = age {
        if age > 30 {
            println!("Using purple as the background color");
        } else {
            println!("Using orange as the background color");
        }
    } else {
        println!("Using blue as the background color");
    }
}

// Listing 18-1: Mixing if let, else if, else if let, and else

// If the user specifies a favorite color, that color is used as the background. If no favorite
// color is specified and today is Tuesday, the background color is green. Otherwise, if the user
// specifies their age as a sgring and we can parse it as a number successfully, the color is
// either purple or orange depending on the value of the number. If none of these conditions apply,
// the background color is blue.
//
// This conditional structure lets us support complex requirements. With the hardcoded values we
// have here, this example will print Using purple as the background color.
//
// You can see that if let can also introduce shadowed variables in the same way taht match arms
// can: the line if let Ok(age) = age introduces a new shadowed age variable that contains the
// value inside the Ok variant. This means we need to place the if age > 30 condition within that
// block: we can't combine these two conditions into if let Ok(age) = age && age > 30. The
// shadowed age we want to compare to 30 isn't valid until the new scope starts with the curly
// brackets.
//
// The downside of using if let expressions is that the compiler doesn't check for exhaustiveness,
// whereas with match expressions it does. If we omitted the last else block and therefor missed
// handling some cases, the compiler would not alert us to the possible logic bug.


// while let Conditional Loops
// ---------------------------
//
// Similar in construction to if let, the while let conditional loop allows a while loop to run for
// as long as a pattern continues to match. In Listing 18-2 we code a while let loop that uses a
// vector as a stack and prints the values in the vector in the opposite order in which they were
// pushed.

fn ex3() {
    let mut stack = Vec::new();

    stack.push(1);
    stack.push(2);
    stack.push(3);

    while let Some(top) = stack.pop() {
        println!("{}", top);
    }
}
// Listing 18-2: Using a while let loop to print values for as long as stack.pop() returns Some

// This example prints 3, 2, 1. The pop method takes the last element out of the vector and returns
// Some(value). If the vector is empty, pop returns None. The while loop continues running the code
// in its block as long as pop returns Some. When pop returns None, the loop stops. We can use
// while let to pop every element off our stack.



// for Loops
// ---------
//
// In a for loop, the value that directly follows the keyword for is a pattern. For example, in for
// x in y the x is the pattern. Listing 18-3 demonstrates how to use a pattern in a for loop to
// destructure, or break apart, a tuple as part of the for loop.

fn ex4() {
    let v = vec!['a', 'b', 'c'];

    for (index, value) in v.iter().enumerate().map(|(i, v)| (v, i+1)) {
        println!("{} is at index {}", value, index);
    }
}
// Listing 18-3: Using a pattern in a for loop to destructure a tuple

// We adapt an iterator using the enumerate method so it produces a value and the index for that
// value, placed into a tuple. The first value produced is the tuple (0, 'a'). When this value is
// matched to the pattern (index, value), index will be 0 and value will be 'a', printing the first
// line of the output.

fn main() {
    ex1();
    ex2();
    ex3();
    ex4();
}
