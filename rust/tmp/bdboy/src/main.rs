struct Bdboy {
    name: String,
    bdyear: u16,
}

fn main() {
    let kenny = Bdboy {
        name: "Kenneth".to_owned(),
        bdyear: 1984,
    };

    let current_year: u16 = 2023;

    let age = current_year - kenny.bdyear;

    println!("{} is {} years old today", kenny.name, age);
}

