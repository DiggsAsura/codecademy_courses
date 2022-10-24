/* Expressions
 * ============
 *
 * A Rust program is (mostly) made up of a series of statements: */

fn main() {
    // Statement
    // Statement
    // Statement

/* There are a few kinds of statements in Rust. The most common two are declaring a variable
 * binding, and using a ; with an expressions. */

    // variable binding
    let x = 5;

    // expression;
    x;
    x + 1;
    15;

/* Blocks are expressions too, so they can be used as values in assignments. The last expression in
 * the block will be assigned to the place expression such as local variable. However, if the last
 * expression of the block ends with a semicolon, the return value will be (). */

    let a: u32 = 5;

    let b = {
        let a_squared = a * a;
        let a_cube = a_squared * a;

        // This expression will be assigned to 'b'
        a_cube + a_squared + a
    };
    
    let c = {
        // The semicolon suppresses this expression and '()' is assigned to 'z'
        2 * a
    };
    let d = {
        // The semicolon suppresses this expression and '()' is assigned to 'z'
        2 * a;
    };


    println!("a is {:?}", a);
    println!("b is {:?}", b);
    println!("c is {:?}", c);
    println!("d is {:?} (same exact block as c, just this is ending the expression with a semicolon...)", d);
}


/* Expressions learned me a bit! adding ; at the last expression of the block, will end in a
 * suppression and the compiler will return () instead of the value */
