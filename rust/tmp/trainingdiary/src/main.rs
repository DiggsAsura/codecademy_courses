use std::io;
use std::io::prelude::*;
use std::fs::File;
use std::fs::OpenOptions;

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

fn main() -> io::Result<()> {
    // Taking new info from user
    println!("Enter the day of the event: ");
    let mut day = String::new();
    io::stdin().read_line(&mut day).expect("Failed to read line");

    println!("Enter the month of the event: ");
    let mut month = String::new();
    io::stdin().read_line(&mut month).expect("Failed to read line");

    println!("Enter the year of the event: ");
    let mut year = String::new();
    io::stdin().read_line(&mut year).expect("Failed to read line");

    println!("Enter the description of the event: ");
    let mut description = String::new();
    io::stdin().read_line(&mut description).expect("Failed to read line");

    let new_event = Event {
        day: day.trim().parse().unwrap(),
        month: month.trim().parse().unwrap(),
        year: year.trim().parse().unwrap(),
        description: description.trim().to_string(),
    };

 //   println!("{}", new_event.summarize());

    // Make a new file to store the Event
    let mut file = OpenOptions::new()
        .write(true)
        .append(true)
        .open("diary.txt")
        .unwrap();

    let entry = new_event.summarize();

    // Write the Event to the file!
    file.write_all(entry.as_bytes());

    Ok(())
}
