use rand::seq::SliceRandom;

fn main() {
    let choices = ["yes", "no"];
    println!("Choose from array/vector: {:?}", choices.choose(&mut rand::thread_rng()));

    // Choose multiple
    let multiple_choice = ["1", "2", "3", "4", "5"];
    let choice: Vec<_> = multiple_choice
        .choose_multiple(&mut rand::thread_rng(), 2)
        .collect();
    println!("Multiple choice: {:?}", choice);
}
