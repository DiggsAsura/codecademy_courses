use add_one;
use add_two;
use add_rng;
use rand::Rng;

fn main() {
    let mut rng = rand::thread_rng();
    let num: i32 = rng.gen_range(1..101);
    println!("Hello world! {num} plus one is {}!", add_one::add_one(num));
    println!("Hello world! {num} plus two is {}!", add_two::add_two(num));
    println!("Hello world! {num} plus a random number is {}!", add_rng::add_rng(num));
}

