use std::time::{Duration, Instant};

fn main() {
    let start = Instant::now();
    let mut j: u64 = 5;
    for i in 0..5000000 {
        println!("Rust: {}", i * j);
        j += 1;
    }
    let duration = start.elapsed();
    println!("Rust time it took: {:?}", duration);
}
