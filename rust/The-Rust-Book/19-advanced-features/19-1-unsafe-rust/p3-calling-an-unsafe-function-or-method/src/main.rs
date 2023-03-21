// Calling an Unsafe Function or Method
// ====================================
//
// The second type of operation you can perform in an unsafe block is calling unsafe functions.
// Unsafe functions and methods look exactly like regular functions and methods, but they have an
// extra unsafe before the rest of the definition. T_he unsafe keyword in this context indicates
// the function has requirements we need to uphold when we call this function, because Rust can't
// guarantee we've met these requirements. By calling an unsafe function within an unsafe block,
// we're saying that we've read this funciton's documentation and take responsibility for upholding
// the function's contracts.
//
// Here is an unsafe funciton named dangerous that doesn't do anythihng in its body:

unsafe fn dangerous() {
    println!("This is called from an unsafe function.");
}
unsafe fn another() {
    println!("This is called from another unsafe function.");
}

fn main() {
    unsafe {
        dangerous();
        another();
    }
}
// We must call dangerous function within a separate unsafe block. If we try to call dangeous
// without the unsafe block, we'll get an error.
//
// With the unsafe block, we're asserting to Rust that we've read the function's documentation, we
// understand how to use it properly, and we've verified that we're fulfilling the contract of the
// function.
//
// Bodies of unsafe functions are effectively unsafe blocks, so to perform other unsafe operations
// within an unsafe function, we don't need to add another unsafe block.
