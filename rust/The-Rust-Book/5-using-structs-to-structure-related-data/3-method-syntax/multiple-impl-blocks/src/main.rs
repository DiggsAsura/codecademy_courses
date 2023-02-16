/* Multiple impl Blocks
 *
 * Each struct is allowed to have multiple impl blocks. For example, the last (associated
 * functions) is equivalent to the code shown below, which has each method in its own impl block.
 * */

struct Rectangle {
    width: u32,
    height: u32,
}

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }
}

impl Rectangle {
    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}

fn main() {
    println!("Hello, world!");
}

/* There's no reason to separate these methods into multiple blocks here, but this is valid syntax.
 * We'll see a case in which multiple impl blocks are useful in Chapter 10, where we discuss
 * generic types and traits. */


/* Summary
 *
 * Structs let you create custom types that are meaningful for your domain. By using structs, you
 * can keep associated pieces of data connected to each other and name each piece to make your code
 * clear. In impl blocks, you can define functions that are associated with your type, and methods
 * are a kind of associated function that let you specify the behavior that instances of your
 * structs have. 
 *
 * But structs aren't the only way you can create custom types: let's turn Rust's enum feature to
 * add another tool to your toolbox.
 */
