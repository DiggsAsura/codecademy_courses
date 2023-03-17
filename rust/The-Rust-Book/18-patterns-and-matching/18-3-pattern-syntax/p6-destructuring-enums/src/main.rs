// Destructuring Enums
// ===================
//
// We've destructured enums in this book (for example, Listing 6-5 in Chapter 6), but we haven't
// yet explicitly discussed what the pattern to destructure an enum corresponds to the way the data
// stored within the enum is defined. As an example, in Listing 18-15 we use the Message enum from
// Listing 6-2 and write a match with patterns that will destructure each inner value.

enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}

fn main() {
    let msg = Message::Move { x: 3, y: 5 };

    match msg {
        Message::Quit => {
            println!("The Quit variant has no data to destructure.")
        }
        Message::Move { x, y } => {
            println!("Move in the x direction {} and in the y direction {}.", x, y)
        }
        Message::Write(text) => println!("Text message: {}", text),
        Message::ChangeColor(r, g, b) => println!(
            "Change the color to red {}, green {}, and blue {}",
            r, g, b
        ),
    };
}
// Listing 18-15: Destructuring enum variants that hold different kinds of values

// This code will print Change the color to red 0, green 160, and blue 255. Try changing the value
// of msg to see the code form the other arms run.
//
// For enum variants without any data, like Message::Quit, we can't destructure the value any
// further. We can only match on the literal Message::Quit value, and no variables are in that
// pattern.
//
// For struct-like enum variants, such as Message::Move, we can use a pattern similar to the
// pattern we specify to match structs. After the variant name, we place curly brackets and then
// list the fields with variables so we break apart the pieces to use in the code fro this arm.
// Here we use the shorthand from as we did in Listing 18-13.
//
// For tuple-like enum variants, like Message::Write that hodls a tuple with one element and
// Message::ChangeColor that holds a tuple with three elements, the pattern is similar to the
// pattern we specify to matck tuples. The number of variables in the pattern must match the number
// of elements in the variant we're matching.
