#![allow(dead_code)]
#![allow(unused_variables)]
fn main() {
    ex1_say_howdy();    
    ex2_my_function();
    ex3_another_function();
    ex4_another_function();
    let ex5 = ex5_multiply(32, 32);
    println!("{}", ex5);
    ex6();
}

/*
 * Functions
 * -----------
 *
 * A computer program is fundamentally made up of two things: data and instructions for 
 * manipulating the data. These instructions are called functions and are the things that
 * make our code work.
 *
 * Function declarations
 * -----------------------
 *
 * We can declare a function in Rust with the fn keyword. Declaring a function requires supplying
 * a name for the function, any potential parameters, and a block for the body of the function:
*/

// Declare a function
fn ex1_say_howdy() {
    println!("Howdy!");
}



/*
 * Funciton bodies have their own scope and cannot access variables from the local 
 * environment. 
 *
 */

fn out_of_scope_test() {
    let out_of_scope = "sorry, this won't compile";
}

fn ex2_my_function() {
    // This will not compile
    // println!("{out_of_scope}");

    let in_scope = "this will compile";
    println!("{in_scope}");
}


/*
 * If you need to access variables from the local environment, closures are kind of
 * lazy function that allow this. (next article)
 *
 * 
 * Return Values
 * ----------------
 *
 * We can specify a return value for a function with the -> operator followed by the
 * return type. This is placed after the function name and before the function's block.
 *
 */

// Here we are returning a 'i32'
fn ex3_another_function() -> i32 {
    27
}

// Assigning a returned value to a variable.
fn ex4_another_function() {
    let integer = ex3_another_function();
    println!("{integer}"); // This will print 27
}



/* 
 * Parameters
 * -------------
 *
 * Our functions can take data as input to operate on. These are called input parameters and in
 * Rust, prarmeters always require a type signature. 
 *
 * Type signatures are declared with the paameter name, followed by a :, followed by the type.
 * Multiple parameters are separated by a ,.
 *
 * This multiply function takes two arguments of type u32 and multiplies them together:
 */

fn ex5_multiply(first: u32, second: u32) -> u32 {
    first * second
}

/* 
 * Since all parameters for a function must be manually declared and of a specified type, variadic
 * functions do not exist in Rust. However, we can use macros to mimic this behavior. 
 *
 * The format!() macro in Rust's std library is a great example of this.
 */


/*
 * Functions as Parameters
 * -------------------------
 *
 * We can also pass functions as parameters with the fn pointer primitive. The type signature for
 * a fn paramter requires type annotations and take the form fn(T) -> T.
 *
 * Here the call to the roundabout function will call the function we pass to it.
 */

fn ex6_increment(num: u32) -> u32 {
    num + 1
}

fn ex6_decrement(num: u32) -> u32 {
    num -1
}

fn ex6_roundabout(f: fn(u32) -> u32, num: u32) -> u32 {
    f(num)
}

fn ex6() {
    let inc = ex6_roundabout(ex6_increment, 2); // This returns 3
    let dec = ex6_roundabout(ex6_decrement, 2); // This returns 1

    println!("{}", inc);
    println!("{}", dec);
}

// NOTE that when we are passing a function pointer as an argument, we forego the trailing ().
