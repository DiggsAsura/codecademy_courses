/* An Example Program Using Structs
 *
 * To understand when we might want to use structs, let's write a program that calculates the area
 * of a rectangle. We'll start by using single variables, and then refactor the program until we're
 * using structs instead.
 *
 * Let's make a new binary project called rectangles that will take the width and height of a
 * rectangle specified in pixels and calculate the area of the rectangle. Listing 5-8 shows a short
 * program with one way of doing exactly that in our project's stc/main.rs
 *
 */
fn main() {
    let width1 = 30;
    let height1 = 50;

    println!(
        "The area of the rectangle is {} square pixels.",
        area(width1, height1)
    );
}

fn area(width: u32, height: u32) -> u32 {
    width * height
}
