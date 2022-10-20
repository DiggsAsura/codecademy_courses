fn main() {

}

// CONSTANTS
// ==========
//
// In Rust, constants are immutable data or functions that are declared at 
// compile time. 
//
// When we have a piece of data that is used in many places throughout a 
// codebase, we can avoid code duplication and ease development by utilizing
// constants.
//
//
// const
// ------
//
// We can declare a constant with the const keyword. Constant names must follow
// the SCREAMING_SNAKE_CASE convention.
//
// Constants always require a type declaration and only types with a known size
// at compile time can be declared as a constant:

fn ex1() {
    const ANIMAL: &str = "penguin";

    // String does not have a known size, so it cannot be used as a constant
    // The below commented code will not compile.
    // const OOPS: String = String::from("sorry");
    //
            // WHATS the difference between String and &str
            // str: immutable sequence of UTF-8 bytes of dynamic length
            //      somewhere in memory
            // String: is the dynamic heap string type, like Vec: use it when 
            //       you need to own or modify your string data.
}

// Constants can be assigned to any expression as long as that expression can be
// computed at compile time. 

fn ex2() {
    const SECONDS_IN_A_DAY: usize = 60 * 60 * 24;
    
    // Constants follow the same visibility requirements as any other 
    // expression.

    mod calculation {
        pub const REVOLUTIONS: usize = 38;
    }

    pub fn number_of_revolutions() {
        let revolutions = calculation::REVOLUTIONS;
        println!("{revolutions} revolutions per second");
    }
}


// const fn
// ========
//
// In Rust, function pointers are primitive data type. This means we can declare
// functions as constants. Making a function constant will enforce restrictions
// to validate that the function will provide the same result wheter evaluated
// at compile time or runtime. This is similar to the concept of a 
// mathematically "pure function" and helps to prevent unintended side effects.
//
// const fn parameters are limited to datatypes with a known size at compile-
// time:

fn ex3() {
    const fn days_to_seconds(days: usize) -> usize {
        days * 60 * 60 * 24
    }

    // We can utilize constant functions within other constant declarations
    const WEEK_IN_SECONDS: usize = days_to_seconds(7);
    let february_in_seconds = days_to_seconds(28);

    println!("{WEEK_IN_SECONDS}");
    println!("{february_in_seconds}");
}

// Associated Constants
// =====================
//
// Rust also allows associated constants which are constants declared within
// traits.

fn ex4() {
    trait Golf {
        const BIRDIE: i32 = -1;
    }

    struct Caddy;

    impl Golf for Caddy {}

    println!("{}", Caddy:BIRDIE);
}

// Constants are an ever-progressing aspect of the Rust language. Soon on the
// horizon, we can expect constant generics.
//
    // Traits and Structs, then impl is all something I have to really 
    // understand. 
