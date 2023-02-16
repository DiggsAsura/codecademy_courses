use std::io;

fn main() {
    println!("Welcome to the guessing game!");

    let mut guess = String::new();
    println!("Please guess a number: {}", guess);
    io::stdin()
        .read_line(&mut guess)
        .expect("Sorry, something went wrong");
    
    let guess: u32 = guess.trim().parse().expect("Nope"); 
    println!("You guessed {guess}");

}
