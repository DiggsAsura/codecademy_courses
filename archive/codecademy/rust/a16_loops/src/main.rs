fn main() {
//    ex1();
    ex2();
    ex3();
    ex4();
    ex5();
    ex6();
    ex7();
}

// Loops
// ======


// loop
// -----
//
// We can repeat a block of code endlessly with the loop statement:

fn ex1() {
    println!("This is the program that never ends...");

    loop {  // ok lets change endless for now - but how? lol
        print!(" yes, it goes on and on, my friend,");
        break;  // this adds % to the output? O.o
    }
}


// break and continue
// --------------------
//
// Code execution within a loop can be diverted at any point with the break and continue
// keywords.
//
// break will stop code execution and exit the loop:

fn ex2() {
    loop {
        println!("I will be printed once");
        break;
        println!("I will not be printed");
    }

    println!("I will also never print"); // i dont beleive this? Exactly this is printed..
}

// continue will stop code execution and restart at the beginning of the loop:

fn ex3() {
    loop {
        print!(".");
        // continue;  // changing to break so i can continue the article
        break;
        println!("I will not be printed");
    }
    println!("I will also never print");
}


// Loop Labels
// -------------
//
// When we have multiple nested loops, we may want to break out of a parent loop 
// directly rather than the one we are currently in. Rust allows us to tag our loops
// with labels utilizing the syntax 'label: loop {}.
//
// We can denote which loop we want to break out of by its label.

fn ex4() {
    'first: loop {
        println!("entering 'first");

        'second: loop {
            println!("entering 'second");
            break 'first;
        }
        println!("I will never print")
    }
}

// while
// ------
//
// We can repeat code based on conditional evaluation with the while statement.
// Once the provided condition is satisfied, the loop will break. 
//
// This is an implementation of the previous example using while statement:

fn ex5() {
    let mut number = 0;

    while number <= 11 {
        println!("{number}");
        number += 2;
    }
}

// Note that we can still use break and continue within while statements to control its
// looping behavior.


// while let
// ----------
//
// We can destructure with a while statement using the while let pattern. This pattern 
// operates much the same way an if let pattern does. 
//
// This is particulary useful when utilizing mutable monadic types. 

fn ex6() {
    let mut timer = Some(10);

    while let Some(seconds_left) = timer {
        if seconds_left == 0 {
            println!("done!");
            timer = None;
        } else {
            println!("{seconds_left}");
            std::thread::sleep_ms(1000);
            timer = Some(seconds_left - 1);
        }
    }
}


// for/in
// -------
//
// It is possible to iterate over the items of a collection utilizing the for and in
// keywords. Any collection which implements the std::iter::Iterator trait can utilize
// this pattern.

fn ex7() {
    let numbers = vec![10, 9, 8, 7, 6, 5, 4, 3, 2, 1];

    println!("the numbers are ");

    // Here 'n' is newly created variable for each item of our collection.
    for n in numbers {
        println!("{n}");
    }
}

// Another way to approach looping over collections is through functional iteration.

