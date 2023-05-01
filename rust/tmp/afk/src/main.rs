struct Testing {
    name: String,
    age: u8,
}

fn main() {
    let kayi = Testing {
        name: "Kayi".to_owned(),
        age: 31,
    };

    println!("{}", kayi.name);
    println!("{}", kayi.age);
}
