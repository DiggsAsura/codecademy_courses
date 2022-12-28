trait MakeNoise {
    fn make_noise(&self) {
        println!("silence");
    }
}

struct Dog;
struct Cat;

impl MakeNoise for Dog {
    fn make_noise(&self) {
        println!("bark");
    }
}

impl MakeNoise for Cat {}

fn main() {
    Dog.make_noise();
    Cat.make_noise();
}
