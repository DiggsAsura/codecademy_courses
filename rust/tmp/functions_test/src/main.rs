fn testing_return() {
    println!("This code runs")
}

fn test_two() -> String {
    return "This code does not run?".to_owned();
}

fn main() {
    let x = testing_return();
    let y = test_two();

    println!("y runs now, because it's called in this string\n: {}", y);
}

// interesting. y, well the println is executed before let x.
