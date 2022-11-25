/* Function parameters needs to have specific types. */
fn main() {
    another_function("argument");
}

fn another_function(parameter: &str) {
    println!("the {parameter} is used when calling the function.. right?");
}
