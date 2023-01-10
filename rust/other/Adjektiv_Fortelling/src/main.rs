use std::io;
use rand::seq::SliceRandom;
//use rand::prelude::*;

fn main() {
    println!("Adjektivfortelling!");
    println!("Hvor mange ord vil du bruke? Max 10:");

    let mut count = String::new();
    io::stdin().read_line(&mut count).expect("Error");
    let count = count.trim();
    println!("Ok, du har valgt {count}:");


    let word_one = new_adjektiv();
    let word_two = new_adjektiv();
    //println!("{:?}", word_one);
    //println!("{:?}", word_two);

    let mut words = vec![word_one, word_two];
    println!("{:?}", words);

    // Need a logic to add random word to a variable 
    let mut random_word_1 = words.choose(&mut rand::thread_rng());
    println!("{:?}", random_word_1);

}


fn new_adjektiv() -> String {
    let mut word = String::new();
    io::stdin().read_line(&mut word).expect("Error");
    let fixed_word = word.trim();
    return fixed_word.to_string();
}

