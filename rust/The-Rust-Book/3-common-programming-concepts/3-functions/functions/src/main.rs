/* Functions
 *
 * snake case convention for functions and variable names.
 */

fn main() {
    println!("Hello, world!");

    another_func(2, "5");

}

fn another_func(a: i32, b: &str) {
    let b: i32 = b.trim().parse().expect("This is not a number bro, fix it!");
    let c: i32 = a + b;
    println!("{a} + {b} = {c}")
}


