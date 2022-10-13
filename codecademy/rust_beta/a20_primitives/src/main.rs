#![allow(dead_code)]
#![allow(unused_variables)]
fn main() {
    ex1();
    ex2();
    ex5();
}

/* 
 * Primitives
 * ===========
 *
 * Everything in Rust has a type.
 *
 * Some types are so commonly used in programming that they have been baked directly into the
 * language itself. These basic types are called primitives and they do not rely upon the std
 * library. 
 *
 *
 * Boolean
 * --------
 *
 * The bool primitive is a boolean value, which can be either true or false.
 */

fn ex1() {
    let this_is_a_variable = true;

    // A bool is its own conditional.
    if this_is_a_variable {
        println!("yep, its a variable");
    } else {
        println!("wrong universe");
    }
}

/* 
 * Integers
 * ---------
 *
 * Rust has multiple signed and unsigned integer primitives. They are designated by their memory
 * size in bits and wheter or not they allow negative numbers.
 *
 * Integer types that begin with an i are signed and allow negative integers, while unsigned
 * integers begin with a u.
 *
 * For example, u8 is an integer that can represent any number from 0 to 255.
 *
 * Available integer primitives include:
 *
 *  - Signed integers: i8, i16, i32, i64, i128, isize
 *  - Unsigned integers: u8, u16, u32, u64, u128, usize
 *
 * usize and isize will determine the memory size based on the system architecture during
 * compilation. When no type is specified, Rust infers the type to be i32.
 */

fn ex2() {
    let integer = 102;
    let negative = -48;

    // We can type annotate our integers to make sure we can handle large numbers. prefix
    let byte: u8 = 255;
    let large: i64 = -9223372036854775808;

    // We can also specify types as a postfix to the number. suffix
    let byte = 255u8;
    let large = -9223372036854775808i64;
}


/*
 * Floating Points
 * ----------------
 *
 * Rust has two floating point types of differing precision, f32 and f64, which are also denoted by
 * their bit size in memory. When no type is specified, Rust infers f64.
 *
 * Floating point numbers are specified by their inclusion of a decimal point. 
 */

fn ex3() {
    let float = 1.2;

    // Floats do not require a decimal portion.
    let still_a_float = 1.;

    // With type annotation.
    let a_less_precise_float: f32 = 2.83;
}


/*
 * Chars
 * ------
 * 
 * A char is a character, or more specifically, a unicode scalar value. 
 *
 * Chars are specified by enclosing the character within single parantheses.
 */

fn ex4() {
    let letter = 'q';
    let accented = 'á';
    let percent = '%';
    let checkmark = '✓';
}

/*
 * Soince Rust utilizes UTF-8 as an encoding scheme, some single width characters may be composed
 * of multiple chars. 
 */

fn ex5() {
    // This emoji is more than 1 char in length and cannot be declared as a char literal. We must
    // use a &str.
    let yourself = "😃";

    println!("{yourself}");
}


/* 
 * Other Primitives
 * ------------------
 *
 * The types we have just discussed are not the only primitives in Rust. There are also arrays,
 * str, and tuples. The unit type is a special kind of tuple without any contained data.
 *
 * Most importantly, function pointers are also a primitive type. This means we can pass functions
 * the same we would any other type. 
 */


