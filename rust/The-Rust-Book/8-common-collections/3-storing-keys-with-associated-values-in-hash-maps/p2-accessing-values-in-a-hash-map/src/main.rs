// Accessing Values in a Hash Map
// ================================
//
// We can get a value out of the hash map by providing its key to the get method,
// as shown in Listing 8-21.
use std::collections::HashMap;

fn main() {

    let mut scores = HashMap::new();

    scores.insert(String::from("Blue"), 10);
    scores.insert(String::from("Yellow"), 50);

    let team_name = String::from("Blue");
    let score = scores.get(&team_name).copied().unwrap_or(0);
    println!("{}: {}", team_name, score);

    // ex2
    ex2();
}

// Listing 8-21: Accessing the score for the Blue team stored in the hash map

// Here, score will have the value that's associated with the Blue team, and the result
// will be 10. The get method returns an Option<&V>; if there's no value for that key
// in the hash map, get will return None. This program handles the Option by calling
// copied to get an Option<i32> rather than an Option<&i32>, then unwrap_or to
// set score to zero if scores doesn't have an entry for the key.
//
// We can iterate over each key/value pair in a hash map in a similar manner as
// we do with vectors, using a for loop:

fn ex2() {
//    use std::collections::HashMap;
    let mut scores = HashMap::new();
    scores.insert(String::from("Blue"), 10);
    scores.insert(String::from("Yellow"), 50);

    for (key, value) in &scores {
        println!("{}: {}", key, value);
    }
}
