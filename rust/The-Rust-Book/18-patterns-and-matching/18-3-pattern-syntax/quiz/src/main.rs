// Question 1
//
// Determine whether the program will pass the compiler. If it passes, write the expeceted output
// of the program if it were executed.

fn main() {
    let x = (0, 1);

    match x {
        (_, y) if y == 0 => println!("A"),
        (0, _) => println!("B"),
        _ => println!("C"),
    }
}


// I think B
// Correct!
