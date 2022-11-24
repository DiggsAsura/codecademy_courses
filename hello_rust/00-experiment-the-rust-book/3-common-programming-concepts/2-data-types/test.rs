fn main() {
    println!("A little confused about something in the book, so just checking if u8::MAX and 2_u8.pow(7) is the same\n");
    let my_u8_max = u8::MAX;
    let my_u8_pow = 2_u8.pow(7);

    println!("{} vs {}", my_u8_max, my_u8_pow);

    let my_u128_max = u128::MAX;
    let my_u128_pow = 2_u128.pow(127);

    println!("{} vs {}", my_u128_max, my_u128_pow);

    println!("\nNope, pow(7)/pow(127) will of course not work");
}
