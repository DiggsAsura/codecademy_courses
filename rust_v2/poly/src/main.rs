use std::{thread, time};
use indicatif::{ProgressBar, ProgressStyle};

fn spinning1() {
    let pb = ProgressBar::new_spinner();
    pb.set_style(
        ProgressStyle::default_spinner()
            .tick_strings(&["🌑", "🌒", "🌓", "🌔", "🌕", "🌖", "🌗", "🌘"]),
        );
    pb.set_message("loading...");

    for _ in 0..50 {
        thread::sleep(time::Duration::from_millis(30));
        pb.inc(1);
    }

    pb.finish_with_message("Done spinning1()");

}


fn spinning2() {
    let pb = ProgressBar::new_spinner();
    pb.set_style(
        ProgressStyle::default_spinner()
            .tick_strings(&["🌑", "🌒", "🌓", "🌔", "🌕", "🌖", "🌗", "🌘"]),
        );
    pb.set_message("loading...");

    for _ in 0..50 {
        thread::sleep(time::Duration::from_millis(30));
        pb.inc(1);
    }

    pb.finish_with_message("Done spinning2()");

}


fn main() {
    let handle1 = thread::spawn(|| {
        spinning1();
    });
    let handle2 = thread::spawn(|| {
        spinning2();
    });

    handle1.join().unwrap();
    handle2.join().unwrap();

    println!("Both functions completed");
}

