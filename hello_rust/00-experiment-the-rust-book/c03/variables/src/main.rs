fn main() {
    let mut x = 5;          // make it mut(able) to be able to later change x
    println!("The value of x is: {x}");
    x = 6;
    // let x = 6;   // could also use shadowing here in this example
    println!("The value of x is: {x}");
}
