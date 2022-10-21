// OK! Finally starting to get some grasp on structs, traits, and impls! 
// Need enums now i guess!


struct Member {
    name: String,
    email: String,
}

trait Summarize {
    fn summarize(&self) -> String {
        String::from("Default")
    }
    fn another_default(&self) -> String {
        String::from("Another default trait")
    }
    fn summ(&self) -> String;
}

impl Summarize for Member {
    fn summ(&self) -> String {
        format!("{}: {}", self.name, self.email)
    }
}

fn main() {
    let member_1 = Member {
        name: String::from("DiggsAsura"),
        email: String::from("your@email.com"),
    };

    println!("{}", member_1.summarize());
    println!("{}", member_1.summ());
    println!("{}", member_1.another_default());
}
