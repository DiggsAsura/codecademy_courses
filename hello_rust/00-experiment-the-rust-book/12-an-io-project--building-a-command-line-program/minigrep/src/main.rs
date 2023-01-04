use std::env;   // 12-1

fn main() {
    // 12-1 --------------------------------------------
    let args: Vec<String> = env::args().collect();
    dbg!(args);
    // 12-1: Collecting the command line arguments into a vector and printing them.
    // ------------------------------------------------
}
