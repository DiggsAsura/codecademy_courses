/* Processing a Guess
 *
 * The first part of the guessing game program will ask for user input, process that input, and
 * check that the input is in the expected form. To start, we'll allow the player to input a guess.
 */
use std::io;
use rand::Rng;   // The Rng trait defines methods that random number generators implement.
use std::cmp::Ordering;  // Ordering is an enum and has the variants Less, Greater and Equal

fn main() {
    println!("Guess the number!");

    // Modified version: Only have several attempts!
    let attempts: u32 = 5;
    let mut round: u32 = 1;

    let secret_number = rand::thread_rng().gen_range(1..=100);
//    println!("The secret number is: {secret_number}");

    println!("Please input your guess.");
    while round <= attempts {
        let mut guess = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");
 
        // cant compare String and i32, aka different types. Need to convert something, fx u32
        // secondly change it to a match expression to handle if user inputs words. aka dont crash
        // if user input anything else then numbers. 
        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,             // num is a... number... but not a defined variable
            Err(_)  => {                // _ is catchall
                println!("Please enter a valid number:");
                continue;
            },
            // Because parse() returns a Result, we can use match on it. :) 
        };

        println!("You guessed: {guess}"); 

        match guess.cmp(&secret_number) {
            Ordering::Less      => println!("{round}/{attempts}: Too small!"),
            Ordering::Greater   => println!("{round}/{attempts}: Too big!"),
            Ordering::Equal     => {
                println!("{round}/{attempts}: You win!");
                break
            }
        }
        round += 1;

        if round == attempts+1 {            // Might be possible to do this more clean
            println!("\nYou loose. The secret number was: {secret_number}!");
        }
    }
}

