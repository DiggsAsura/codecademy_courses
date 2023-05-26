use std::fmt::Debug;

#[derive(Debug)]
enum Month {
    January,
    February,
    March,
    April,
    May,
    June,
    July,
    August,
    September,
    November,
    December
}

trait Summary {
    fn summarize(&self) -> String where Self: Debug {
        format!("The month is {:?}", self)
    }
}

impl Summary for Month {
    fn summarize(&self) -> String {
        format!("The month is {:?}", &self)
    }
}

fn main() {
    println!("Hello, world!");
}
