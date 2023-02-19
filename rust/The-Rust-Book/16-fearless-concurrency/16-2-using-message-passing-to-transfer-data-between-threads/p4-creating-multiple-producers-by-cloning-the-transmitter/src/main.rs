// Creating Multiple Producers by Cloning the Transmitter
// =======================================================
//
// Earlier we mentioned that mpsc was an acronym for multiple producer, single consumer. Let's put
// mpsc to use and expand the code in Listing 16-10 to create multiple threads that all send values
// to the same receiver. We can do so by cloning the transmitter, as shown in Listing 16-11:

use std::sync::mpsc;
use std::thread;
use std::time::Duration;

fn main() {
    let (tx, rx) = mpsc::channel();

    let tx1 = tx.clone();
    thread::spawn(move || {
        let vals = vec![
            String::from("thread 1: hi"),
            String::from("thread 1: from"),
            String::from("thread 1: the"),
            String::from("thread 1: thread"),
        ];

        for val in vals {
            tx1.send(val).unwrap();
            thread::sleep(Duration::from_secs(1));
        }
    });

    let tx2 = tx.clone();
    thread::spawn(move || {
        let vals = vec![
            String::from("thread 3: yolo"),
            String::from("thread 3: swag"),
            String::from("thread 3: lol"),
            String::from("thread 3: brb"),
        ];
        for val in vals {
            tx2.send(val).unwrap();
            thread::sleep(Duration::from_secs(1));
        }
    });


    thread::spawn(move || {
        let vals = vec![
            String::from("thread 2: more"),
            String::from("thread 2: messages"),
            String::from("thread 2: for"),
            String::from("thread 2: you"),
        ];

        for val in vals {
            tx.send(val).unwrap();
            thread::sleep(Duration::from_secs(1));
        }
    });

    for received in rx {
        println!("From {}", received);
    }
}

// Listing 16-11: Sending multiple messages from multiple producers


// This time, before we create the first spawned thread, we call clone on the transmitter. This
// will give us a new transmitter we can pass to the first spanwed thread. We pass the original
// transmiiter to a second spawned thread. This gives us two threads, each sending different
// messages to the one receiver.
//
// When you run this code, your output should look something like this (with my added tx2 weaved in
// too in addition):

/*
Got: hi
Got: more
Got: from
Got: messages
Got: for
Got: the
Got: thread
Got: you
*/

// You might see the values in another order, depending on your system. This is what makes
// concurrency interesting as well as difficult. If you experiment with thread::sleep, giving it
// various values in the different threads, each run will be more nondeterministic and create
// different output each time.
//
// Now that we've looked at how channels work, let's look at a different method of concurrency.
