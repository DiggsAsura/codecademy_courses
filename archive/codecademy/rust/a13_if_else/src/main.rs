fn main() {
    println!("Hello, world!");
    ex1();
    ex2();
    ex3();
    ex4();
    ex6();
}

// if/else 

fn ex1() {
    let is_daytime = true;

    if is_daytime {
        println!("What a beautiful day!")
    } else {
        println!("ZZzzzzzzzzzzz")
    }
}

// else if

fn ex2() {
    #[derive(PartialEq, Eq)]
    enum Flower {
        Lilac,
        Orchid,
        Daffodil,
    }

    let flower = Flower::Daffodil;

    if flower == Flower::Lilac {
        println!("a lilac");
    } else if flower == Flower::Orchid {
        println!("a beautiful orchid");
    } else {
        println!("another flower");
    }
}


// Exhaustiveness
// Rust's conditional evaluations are fully exhaustive, so every possible outcome
// must be accounted for. This means that when if block is an expression, every
// else if and else block must return the same type:

fn ex3() {
    let carrots = 12;

    let rabbit_status = if carrots > 10 {
        "in burrow"
    } else if carrots == 9 {
        "snagging one more carrot"
    } else {
        "on the prowl"
    };

    println!("{rabbit_status}");
}


// We do not need to provide an else keyword when our conditional block is a 
// statement because statements inherently return the unit type, ().

fn ex4() {
    if true {
        println!("this is shorthand");
    }

    if true {
        println!("for this...");
        ()
    } else {
        ()
    }
}


// Conditional Operators
// Rust provides us with operators for conditional evaluations. These operators can
// be used on any type that implements the respective traits found in Rust's 
// standard library.
//
// Equality
// ---------
//
// Equality can be checked with == and non-equality with !=.
//
// These operators will work on any type which implements the Eq or PartialEq traits.

fn ex5() {
    let track_number = 8;

    if track_number == 9 {
        println!("number nine");
    }

    if track_number != 9 {
        println!("flip the record");
    }
}


// Ordering
// =========
//
// Ordering on a type can be compared with <, >, <=, >=.
//
// These operators will work on any type which implements the Ord or PartialOrd traits.

fn ex6() {
    let pancaces = 10;

    if pancaces < 3 {
        println!("Eat more pancaces.")
    } else if pancaces > 10 {
        println!("Uh oh...")
    } else if pancaces == 10 {
        println!("That's a lot of pancaces")
    } else {
        println!("Mmm syrup")
    }
}

// Keep in mind that since equality and ordering is handled by their respective traits,
// we can implement conditional operators for our own custom data types.

