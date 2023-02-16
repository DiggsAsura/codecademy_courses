/* abort and unwind
 * =================
 *
 * The previous section illustrates the error handling mechanism panic. Different code paths can be
 * conditionally compiled based on the panic setting. The current values available are unwind and
 * abort. 
 *
 * Building on the prior lemonade example, we explicitly use the panic strategy to exercise
 * different lines of code. */

fn drink(beverage: &str) {
    // You should'nt drink too much sugary beverages.
    if beverage == "lemonade" {
        if cfg!(panic="abort"){println!("This is not your party. Run!!!");}
        else{println!("Spit it out!!!");}
    }
    else{ println!("Some refreshing {} is all I need.", beverage); }
}

fn main() {
    drink("water");
    drink("lemonade");

    // Part 2
    drink_two("water");
    drink_two("lemonade");
}


/* Here is another example focusing on rewriting drink() and explicitly use the unwind keyword. */

#[cfg(panic = "unwind")]
fn ah() {
    println!("Spit it out!!!");
}

#[cfg(not(panic="unwind"))]
fn ah() {
    println!("This is not your party. Run!!!!");
}

fn drink_two(beverage: &str) {
    if beverage == "lemonade" {
        ah();
    } else {
        println!("Some refreshing {} is all I need.", beverage);
    }
}

/* The panic strategy can be set from the command line using abort or unwind.
 *
 * rustc lemonade.rs -C panic=abort
 */

