#[derive(Debug)]
struct Contest {
    point: i32,
}

impl Contest {
    fn present(&self) -> String {
        format!("You had {:?} points", &self)
    }
}

fn main() {
    let kenny = Contest {
        point: 79,
    };

    println!("{}", kenny.present());
}
