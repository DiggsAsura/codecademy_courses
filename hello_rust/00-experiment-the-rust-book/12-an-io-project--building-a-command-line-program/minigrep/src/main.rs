use std::env;   // 12-1

fn main() {
    // Reading the Argument Values
    // ----------------------------------------------
    let args: Vec<String> = env::args().collect();
    //dbg!(args);
    // 12-1: Collecting the command line arguments into a vector and printing them.
    // ----------------------------------------------

    // Saving the Argument Values in Variables
    // ----------------------------------------------
    let query = &args[1];       // 1 because 0 is the program itself (minigrep)
    let file_path = &args[2];   // 2 because 1 is the query

    println!("Searching for {}", query);
    println!("In file {}", file_path);
    // 12-2: Creating variables to hold the query argument and file path argument
    // ----------------------------------------------
}

