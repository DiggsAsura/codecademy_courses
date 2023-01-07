use std::env;   // 12-1
use std::fs;    // 12-4

fn main() {
    // Reading the Argument Values
    // ----------------------------------------------
    let args: Vec<String> = env::args().collect();
    //dbg!(args);
    // 12-1: Collecting the command line arguments into a vector and printing them.
    // ----------------------------------------------

    // Saving the Argument Values in Variables
    // ----------------------------------------------
    //let query = &args[1];       // 1 because 0 is the program itself (minigrep)
    //let file_path = &args[2];   // 2 because 1 is the query

    // 12-3
    let (query, file_path) = parse_config(&args);

    println!("Searching for {}", query);
    println!("In file {}", file_path);
    // 12-2: Creating variables to hold the query argument and file path argument
    // ----------------------------------------------

    // Reading a file
    // ----------------------------------------------
    let contents = fs::read_to_string(file_path)
        .expect("Should have been able to read the file");

    println!("With text:\n{contents}");
}

// 12-3
fn parse_config(args: &[String]) -> (&str, &str) {
    let query = &args[1];
    let file_path = &args[2];

    (query, file_path)
}
