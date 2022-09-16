use std::io;

fn main() {
    println!("Started school today");

    let mut name = String::new();
    io::stdin().read_line(&mut name).expect("Could not read name");

    let name = name.trim();

    println!("{name}");

    match name {
        "kenneth" => println!("Hi Kenny!"),
        "sarah" => println!("Cool cat!"),
        "kayi" => println!("Strong woman!"),
        _ => println!("No match"),
    };
}
