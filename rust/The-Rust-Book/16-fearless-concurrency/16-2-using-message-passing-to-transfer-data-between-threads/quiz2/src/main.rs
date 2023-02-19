use std::{sync::mpsc, thread};

fn main() {
    let (tx, rx) = mpsc::channel();
    thread::spawn(move || {
        let s = String::from("Hello World");
        tx.send(s.clone()).unwrap();
        tx.send(s.len().to_string()).unwrap();
    });

    let s = rx.recv().unwrap();
    let n = rx.recv().unwrap();

    println!("s = {}, n = {}", s, n);

}
