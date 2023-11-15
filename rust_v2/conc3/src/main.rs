// purpose: make to blinking dots in the terminal which runs for 10 seconds each. concurrency, so
// one dot in each thread.

use std::thread;
use std::time::Duration;




fn main() {
    let _handle = thread::spawn(|| {
        for i in 1..=10 {
            println!("hi number {} from the first spawned thread!\n", i);
            thread::sleep(Duration::from_millis(1000));
        }
    });

    let _handle2 = thread::spawn(|| {
        for i in 1..=10 {
            println!("hi number {} from the second spawned thread!\n", i);
            thread::sleep(Duration::from_millis(1000));
        }
    });

    // handle.join().unwrap();

    for i in 1..=10 {
        println!("hi number {} from the main thread!", i);
        thread::sleep(Duration::from_millis(1000));
    }
}
