struct Event {
    day: u8,
    month: u8,
    year: u16,
    description: String,
}

trait Summary {
    fn summarize(&self) -> String;
}

impl Summary for Event {
    fn summarize(&self) -> String {
        format!("{}-{}-{}: {}", self.day, self.month, self.year, self.description)
    }
}

fn main() {
    let new_event = Event {
        day: 15,
        month: 5,
        year: 2023,
        description: String::from("Running 6km. No strength training today though. Destroyed after two last days."),
    };

    println!("{}", new_event.summarize());
}
