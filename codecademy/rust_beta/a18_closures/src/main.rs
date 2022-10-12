fn main() {
    ex1_closures();
    ex2();
    ex3();
    ex4();
}

/* 
 * CLOSURES
 * ==========
 *
 * Rust allows us to write closures, which are anonymous functions that can capture the state of
 * the environment. While the differences between functions and closures might seem minimal, those
 * minor differences help make Rust a functional programmers's playground.
 *
 * An important thing to note about closures is that they are called lazily, which can help provide
 * significant performance benefits under certain circumstances.
 *
 *
 * Closure Syntax
 * ---------------
 *
 * To best understand cosures, let's take a look at their most verbose form. Closures follow a very
 * similar syntax to functions but with input parameters placed between ||. 
 *
 * Here we have declared a function that squares an integer and a closure that accomplishes the
 * same task.
 */

// Function
fn square_function(a: i32) -> i32 {
    a * a
}

// Closure
fn closure() {
    let square_closure = |a: i32| -> i32 { a * a };
}


/*
 * We rarely see closures in this verbose form thanks to Rust's ability to infer parameter and
 * return types. Additionally, the body of a closure does not require {} braces. 
 *
 */

fn ex1_closures() {
    // Single argument
    let square = |a| a*a;

    // Multiple arguments are separated by a comma
    let multiply = |a, b| a * b;

    // No arguments
    let hundred = || 10 * 10;

    square(5);
    multiply(5, 10);
    hundred();
}

/*
 * When we store a closure as a variable, we can call it the same way we would a function.
 */

/*
 * Capturing Environment
 * -----------------------
 *
 * Closures differ from functions in that they can capture values from the scope they are defined
 * in. Here we are utilizing the house_number variable directly within our where_are_we closure.
 */

fn ex2() {
    let house_number = 388;
    let where_are_we = || println!("{house_number}");

    where_are_we();
}


/*
 * Ownership and move
 * -------------------
 *
 * We can tell a closure to take ownership of the local data it utilizes by placing the move
 * keyword in front our closure declaration. 
 */

fn ex3() {
    let answer = 928;

    // Here we ahve moved the data from 'answer' into the 'is_correct' closure. 
    let is_correct = move |x| x == answer;

    // We can no longer access 'answer', but we can now use our closure to validate we have the
    // correct answer.
    println!("{}", is_correct(23)); // false
    println!("{}", is_correct(928)); // true
}


/* 
 * Closures as Data Structures
 * ------------------------------
 *
 * We talked previously in the functions article about how function pointers are a primitive
 * datatype. Since closures are also functions, we can use them as fields in structs or tuples.
 */

#[derive(Debug)]
struct Magic {
    field: fn(),
}

fn ex4() {
    let almost = Magic {
        field: || println!("almost magic!"),
    };
    println!("{:?}", almost);
}

/*
 * We can get even more specific in regards to ownership and mutability by utilizing generics with
 * the Fn, FnMut, and FnOnce traits.
 *
 *
 *
 * Laziness
 * -----------
 *
 * Closures in Rust are lazy, which means they are not computed until called. When we have a
 * function that takes a long time to compute, we can often achieve better performance in our
 * program by rewriting our function as a closure. 
 *
 * A good example of the effects of laziness can be found in the Functional Iteration article
 */

