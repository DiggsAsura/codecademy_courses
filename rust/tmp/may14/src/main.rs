struct Happening {
    name: String,
    year: u128,
}

impl Happening {
    fn new(name: String, year: u128) -> Happening {
        Happening { name, year }
    }

    fn summary(&self) -> String {
        format!("{} happened in {}", self.name, self.year)
    }
}

fn main() {
    let happening = Happening::new(String::from("The Big Bang"), 13_800_000_000);
    println!("{}", happening.summary());
}

