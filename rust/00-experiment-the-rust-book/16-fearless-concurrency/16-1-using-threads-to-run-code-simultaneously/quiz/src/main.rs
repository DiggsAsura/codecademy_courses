use std::thread;

fn main() {
    let mut n = 1;
    let t = thread::spawn(move || {
        n = n + 1;
        println!("spawn 1: n + 1 = {}", n);

        thread::spawn(move || {
            n = n + 1;
            println!("spawn 2: n + 1 = {}", n);
        })
    });
    n = n + 1;
    println!("main: n + 1 = {}", n);

    //t.join().unwrap().join().unwrap();
    t.join().unwrap().join().unwrap();
    println!("after unwraps: {n}");
}
