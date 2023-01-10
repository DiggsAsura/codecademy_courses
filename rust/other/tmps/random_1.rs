use std::io;

fn main() {
    println!("Whats your name: ");

    let mut name = String::new();
    io::stdin().read_line(&mut name).expect("Error");

    println!("Hello {name}");
}
