/* How Matches Interact with Ownership
 *
 * If an enum contains non-copyable data like a String, then you should be careful with whether a
 * match will move or borrow that data. For example, this program using an Option<String> will
 * compile: */

fn main() {
    let opt: Option<String> = Some(String::from("Hello, world!"));

    match opt {
        Some(_) => println!("Some!"),
        None => println!("None!"),
    };

    println!("{:?}", opt.unwrap()); // unwrap is not a method of Option, but of Result


    ex2();
}

/* But if we replace the placehodler Some(_) with a variable name, like Some(s), then the program
 * will NOT compile:
 *

 let opt: Option<String> = Some(String::from("Hello, world!"));

 match opt {
    // _ became s
    Some(s) => println!("Some: {}", s),
    None => println!("None!"),
 };

 println!("{:?}", opt); 
 
 */

/* opt is a plain enum - its type is Option<String> and not a reference like &Option<String>.
 * Therefor a match on opt will move non-ignored fields like s. After the match expression, the
 * data within opt has been moved, so its illigal to use opt in the println. 
 *
 * If we want to peek into opt without moving its contents, the idiomatic solution is to match on a
 * reference: */

fn ex2() {
    let opt: Option<String> = Some(String::from("Hello world!"));

    // opt became &opt
    match &opt {
        Some(s) => println!("Some: {}", s),
        None => println!("None!")
    };

    println!("{:?}", opt);
}

/* Rust will "push down" the reference from the outer enum, &Option<String>, to the inner field,
 * &String. Therefore s has type &String, and opt can be used after the match. To better understand
 * this "pushing down" mechanism, see the section about binding modes in the Rust Reference. */
