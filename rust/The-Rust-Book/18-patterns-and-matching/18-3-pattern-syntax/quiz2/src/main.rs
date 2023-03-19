// Question 3
//
// Determine wheter the program will pass the compiler. If it passes, write the expected output of
// the program if it were executed.

fn main() {
    let x = Some(&[0, 1]);

    match x {
        Some(&[.., 1, ..]) => println!("1"),
        Some(&[0, 1]) | None => println!("2"),
        _ => println!("3"),
    }
}

// Nope. I think this code will error at line 6 here, because you can only have one .. if i
// remember correctly.
