fn main() {
    let num = 10;

    for i in 1..num {
        if i == 8 {
            println!("if i == 8");
            break
        }
        println!("{i}");
    }

    println!("Oki just do the match() then");

    match num {
        0 => println!("Hello World"),
        10 => println!("The match is {num}"),
        _ => println!("Out of range"),
    };
}
