// make an enum with different types of messages
#[derive(Debug)]
enum Message {
    Quit,
    Move { x: i32, y: i32 }, // anonymous struct
    Write(String),
    ChangeColor(i32, i32, i32),
}

// implement methods on enums
impl Message {
    fn call(&self) {
        // method body would be defined here
        println!("{:?}, {}", self, "called");
    }
}

fn main() {
    // create instances of the enum
    let m = Message::Write(String::from("hello"));
    m.call();
}

