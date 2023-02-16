/* Using if in a let Statement
 * --------------------------------
 *
 * Because if is an expression, you can use it on the right side of a let statement to assign the
 * outcome to a variable. 
 *
 * (let statement = if expression)
 * (left statement = right expression)
 *
 */

fn main() {
    let condition = true;
    let number = if condition { 5 } else { 6 };

    println!("The value of number is: {number}");

    quiz1();
    quiz2();
}

/* Remember that blocks of code evaluates to the last expression in them, and numbers by themselves
 * are also expressions. In this case, the value of the whole if expression depends on which block
 * of code executes. This means the value that have the potential to be results from each arm of
 * the if must be the same type; the result of both the if arm and the sle arm were i32 integers.
 * If the types are mismatched, as in the following example, we'll get an error:
 *
 * let condition = true;
 * let number = if condidion { 5 } else { "six" };
 *
 * When you try to compile this code, we'll get an error. The if and else arms have value types
 * that are incompatible, and Rust indicates exactly where to find the problem in the program.
 */

/* In short, both arms has to be the same type. */


fn quiz1() {
    let cond = true;
    let x = if cond { 1 } else { 2 };

    let y;
    if cond { y = 1; } else { y = 2; }  // Now i see if is an expression! no ; at the end.. 

    let answer = x == y;
    println!("{answer}");

    /* The first if-expression is a more concise way of representing the behavor of the second
     * if-statement */  // WHY ido they mix statement and expressions.*/ 
}

fn quiz2() {
    let x = true;
    let y = if x {};
    println!("{y:?}");

    /* An if-expression without an else-branch always return the unit type, therfore y has the type
     * and value of a unit (). */
}
