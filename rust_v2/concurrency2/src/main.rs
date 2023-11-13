use std::io::{self, Write};
use std::thread;
use std::time::Duration;

fn main() {
    let handle = thread::spawn(|| {
        for _ in 0..10 {
            print!("Processing... ");
            io::stdout().flush().unwrap();
            thread::sleep(Duration::from_millis(500));
            print!("\r         \r");
            io::stdout().flush().unwrap();
            thread::sleep(Duration::from_millis(500));
        }
    });

    handle.join().unwrap();

    println!("Processing complete!");
}
