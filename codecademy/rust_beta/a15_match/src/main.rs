fn main() {
    ex1();
    ex2();
    ex3();
    ex4();
    ex5();
    ex6();
}

// match
// =====
//
// A match expression takes a pattern and compares it against any number of provided
// match arms. We can define match arms with => placed between the matched pattern and
// its resultant code block.
//
// If the body of a match arm is a single statement or expression, we must terminate 
// the block with a ,.
//
// Here is another way of writing if expression for a boolean value as a match:

fn ex1() {
    let there_are_birds = true;

    match there_are_birds {
        true => println!("hooray!"),
        false => {
            println!("don't worry");
            println!("we can call for them");
        }
    }
}


// Exhaustiveness 
// ---------------
//
// Match expressions are exhaustive, meaning all possible patterns must be accounted for.
// We can declare a catch-all arm with the _ wildcard:

fn ex2() {
    let chosen_number = 3;

    match chosen_number {
        1 => println!("1"),
        2 => println!("2"),
        3 => println!("3"),
        _ => println!("Another nuber"),
    };
}

// Match arms are guaranteed to be processed in order from top to bottom. After the first
// successful match is found, its block is returned, and the remaining arms are not
// checked.


// Match Patterns
// ---------------
//
// Matches in Rust are really fantastic, thanks to the patterns we are capable of utilizing.
// All of the following patterns can be used on match arms as well as with if statements.
//
// Or
// ---
//
// We can match multiple values on the same arm with the | operator. This is called the
// Or-pattern

fn ex3() {
    let plant = "dandelion";

    match plant {
        "dandelion" | "almond" | "apple" => println!("Rose Family"),
        "tomato" | "pepper" | "potato" => println!("Nightshade Family"),
        _ => println!("not found")
    };
}


// Ranges
// -------
// 
// We can match a range of values with the .. and ..= operators to separate our starting
// and ending index. .. denotes an exclusive range while ..= is inclusive:

// !!!!
fn ex4() {
    let chipmunks = 39;

    match chipmunks {
        0 => println!("no chipmunks!"),
        1 ..= 20 => println!("some chipmunks"),
        n @ 21 ..= 40 => println!("warning: {n} chipmunks!"),
        _ => println!("too many chipmunks."),
    }
}


// Binding
// --------
//
// We can bind our matched value to a variable to utilize it in the matched block with the
// @ operator:

fn ex5() {
    let chipmunks = 5;
    
    match chipmunks {
        n @ 0 ..= 40 => println!("warning: {n} chipmunks!"),
        _ => println!("too many chipmunks."),
    }
}

// Match Guards
// -------------
//
// We can even perform additional conditional evaluations on each match arm using an if
// expression.

fn ex6() {
    let answer = Some("herring");

    match answer {
        Some(x) if x.len() > 7 => {
            println!("incorrect");
            println!("hint: password is less than 7 characters long");
        }
        Some(x) => println!("incorrect"),
        None => {
            println!("");
        }
    }
}
