// Refutability: Wheter a Pattern Might Fail to Match
// ==================================================
//
// Patterns com in two forms: refutable and irrefutable. Patterns that will match for any possible
// value passed are irrefutable. An example would be x in the statemetn let x = 5; because x
// matches anything and therefore cannot fail to match. Patterns that can fail to match for some
// possible value are refutable. An example would be Some(x) in the expression if let Some(x) =
// a_value because if the value in the a_value variable is None rather than Some, the Some(x)
// pattern will not match.
//
// Function parameters, let statements, and for loops can only accept irrefutable patterns, because
// the program cannot do anything meaningful when values don't match. The if let and while let
// expressions accept refutable and irrefutable patterns, but the compiler wanrs against
// irrefutable patterns because by definitino they're intended to handle possible failure: the
// functionality of a conditional is in its ability to perform differently depending on success or
// failure.
//
// In general, you shouldn't have to worry about the distinction between refutable and irrefutable
// patterns; however, you do need to be familiar with the concept of refutability so you can
// respond when you see it in an error message. In those cases, you'll need to change either the
// pattern or the construct you're using the pattern with, depending on the intended behavior of
// the code.
//
// Let's look at an example of what happens when we try to use a refutable pattern where Rust
// requires an irrefutable pattern and vica versa. Listing 18-8 shows a let statement, but for the
// pattern we've specified Some(x), a refutable pattern. As you might expect, this code will not
// compile.

// let Some(x) = some_option_value;

// Listing 18-8: Attempting to use a refutable pattern with let

// If some_option_value was a None value, it would fail to match the pattern Some(x), meaning the
// pattern is refutable. However, the let statement can only accept an irrefutable pattern because
// there is nothing valid the code can do with a None value. At compile time, Rust will complain
// that we've tried to use a refutable pattern where an irrefutable pattern is required.
//
// Because we didn't cover (and couldn't cover!) every valid value with the pattern Some(x), Rust
// rightfully produces a compiler error.
//
// If we have a refutable pattern where an irrefutable pattern is needed, we can fix it by changing
// the code that uses the pattern: instead of using let, we can use if let. Then if the pattern
// doesn't match, the code will just skip the code in the curly brackets, giving it a way to
// continue validly. Listing 18-9 whows how to fix the code in Listing 18-8:

fn ex1() {
    if let Some(x) = Some(5) {
        println!("{}", x);
    }
}
// Listing 18-9: Using if let and a block with refutable patterns instead of let

// We've given the code an out! This code is perfectly valid, although it means we cannot use an
// irrefutable pattern without receiving an error. If we give if let a pattern that will always
// match, such as x, as shown in Listing 18-10, the compiler will give a warning:

fn ex2() {
    if let x = 5 {
        println!("{}", x);
    }
}
// Listing 18-10: Attempting to use an irrefutable pattern with if let

// Rust complains that it doesn't make sense to use if let with an irrefutable pattern.
//
// For this reason, match arms must use refutable patterns, except for the last arm, which should
// match any remaining values with an irrefutable pattern. Rust allows us to use an irrefutable
// pattern in a match with only one arm, but this syntax isn't particulary useful and could be
// replaced with a simpler let statement.
//
// Now that you know where to use patterns and the difference between refutable and irrefutable
// patterns, let's cover all the syntax we can use to create patterns.


fn main() {
    ex1();
    ex2();
}
