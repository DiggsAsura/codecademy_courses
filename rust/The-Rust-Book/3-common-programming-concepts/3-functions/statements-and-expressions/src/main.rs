/* Statements and Expressions
 *
 * Statements are instructions that perform some action and do not return a value. 
 *
 * Expressions evaluate to a resulting value. 
 *
 *
 * let keyword is a statement.
 */

fn main() {
    let _y = 6;                  // statement

    expressions();
}

/* Function definitions are also statements; the entire preceding example is a statement itself.
 *
 * Statements do not return values. Therefore, you can't assign a let statement to another
 * variable, as the following code tries to do; you'll get an error.
 *
 * let x = (let y = 6);
 *
 * Error. 
 *
 *
 * The let y = 6 statement does not return a value, so there isn't anything for x to bind to. This
 * is different from what happens in other languages, such as C and Ruby, where the assignment
 * returns the value of the assignment. In those languages, you can write x = y = 6 and have both x
 * and y have the value 6; that is not the case in Rust. 
 *
 */

/* Expressions evaluates to a value and make up most of the rest of the code that you'll write in
 * Rust. 
 *
 * Consider a math operation, such as 5+6, which is an expression that evaluates to the value 11.
 * Expressions can be part of statements: In Listing 3-1, the 6 in the statement let y = 6; is an
 * expression that evaluates to the value 6. Calling a function is an expression. Calling a macro
 * is an expression. A new scope block created with curly brackets is an expression, for example:
 * */

fn expressions() {
    let y = {
        let x = 3;
        x + 1
    };

    println!("The value of y is: {y}");
}

/* This is the expression
 *
 *  {
 *      let x = 3;
 *      x + 1
 *  }
 *
 * This block evaluates to 4. The value gets bound to y as part of the let statement. Note that the
 * x + 1 line doesn't have a semicolon at the end, unlike most of the lines you've seen so far.
 * Expressions do not include ending semicolons. If you add semicolon to the end of an expression,
 * you turn it into a statement, and it will then not return a value. Keep this in mind as you
 * explore funcions return values and expressions next. 
 */

