struct Bd {
    name: String,
    greeting: String,
}

fn main() {
    let bdboy = Bd {
        name: "Marius".to_string(),
        greeting: "Grattis med dagen".to_string(),
    };

    println!("{} {}!", bdboy.greeting, bdboy.name);
}
