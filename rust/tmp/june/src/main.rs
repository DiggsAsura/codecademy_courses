#[allow(dead_code)]
#[derive(Debug)]
enum Car {
    Tesla,
    VW,
    Ford,
}

impl Car {
    fn present(&self) -> String {
        format!("{:?} is a car!", &self)
    }
}

fn main() {
    let tesla = Car::Tesla;

    println!("{}", tesla.present());
}
