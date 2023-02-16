fn main() {
    let mut timer = 5;

    while timer >= 0 {
        println!("{timer}");
        std::thread::sleep_ms(1000);
        timer -= 1;
    }
    println!("Let's go");
    std::thread::sleep_ms(1000);
    println!("how long was that");
}
