use testing::math::add::adding;
use testing::math::sub::subbing;

fn main() {
    let my_add = testing::math::add::adding(1, 2);
    println!("1 + 2 = {}", my_add);

    let my_sub = subbing(2, 1);
    println!("2 - 1 = {}", my_sub);
}
