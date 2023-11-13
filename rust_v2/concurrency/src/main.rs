use std::thread;
use std::time::Duration;

fn main() {
    let handle1 = thread::spawn(|| {
        function1();
    });

    let handle2 = thread::spawn(|| {
        function2();
    });

    // Wait for both threads to finish
    handle1.join().unwrap();
    handle2.join().unwrap();

    println!("Both threads finished executing");
}

fn function1() {
    for i in 1..=50 {
        println!("Function 1: {:>5}", i);
        thread::sleep(Duration::from_millis(600));
    }
}

fn function2() {
    for i in 1..=50 {
        print!("Function 2: {:<5}", i);
        thread::sleep(Duration::from_millis(400));
    }
}
