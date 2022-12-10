/* Adding Useful Functionality with Derived Traits
 *
 * It'd be useful to be able to print an instance of Rectangle while we're debugging our program
 * and see the values for all its fields. Below example tries using the println!() macro as we have
 * used in previous chapters. This won't work, however. */


#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let scale = 2;
    let rect1 = Rectangle {
        width: dbg!(30 * scale),
        height: 50,
    };

    //println!("rect1 is {:#?}", rect1);
    dbg!(&rect1);
}

/* Note: Calling the dbg! macro prints to the standard error console stream (stderr), as opposed to
 * println! which prints to the standard output console stream (stdout). We'll talk more about
 * stderr and stdout in Chapter 12 */
