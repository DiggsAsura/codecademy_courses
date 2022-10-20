fn main() {
    println!("{:?}", ex4());
    println!("{:?}", ex3_shadow());
}

// MUTABILITY
// ============
//
// Mutability is the capability of a variable's value to be altered in memory.
// In Rust, all variables are immutable by default. 
//
// This design decision is extremly useful in practice and helps us avoid 
// unintended behavior. 
//
// mut
// ---
//
// Immutability means that once a variable is declared with let, its value 
// cannot change. To alter a value, we must explicitly declare it as mutable 
// with the mut keyword:

fn ex1() {
    // Immutable
    let three = 3;

    // Mutable
    let mut any_number = 20;
}

// Once we have declared a variable as mutable, we can reassign the value with
// the = operator:

fn ex2() {
    // Reassign explicitly
    let mut number = 20;
    number = 22;

    // Increment and decrement
    number += 1;
    number -= 3;
}

// While mutable states are sometimes the best approach to a particular problem,
// in Rust, it is generally advised to avoid mutability when possible. 
//
// To change a variable's value without mutation, we can choose to shadow a 
// variable instead.

fn ex3_shadow() {
    let number = 10;
    let number = number + 3;
    println!("{number}"); // prints "13"
}

// This allows us to avoid the complexity of mutability but at the cost of 
// extra memory allocation.
//          Ok so mut is memory efficient and shadowing are not? 



// MUTABLE REFERENCES
// ===================
//
// It is also possible to mutate values by reference with &mut.

fn ex4() {
    fn question(s: &mut String) {
        s.pop();      // popping last char in the string
        s.push('?');  // pushing ? on the end of the string
    }

    let mut sentence = String::from("I am.");
    question(&mut sentence);

    println!("{sentence}");
}
    // So I take it the takeaway is this function question, would not be able to
    // transform the string argument without mut. Remember to &mut at every 
    // instance of the sentence variable. 

// We can only have one mutable reference to a piece of data at a time. This
// means we cannot immutably borrow a mutable reference outside the lifetime
// of the mutable reference. 

fn ex5() {
    let mut sentence = String::from("Take care, take care.");
    let immutable_reference = &mut sentence;

    // Swappint the order of these statements will cause our code to not 
    // compile.
    println!("{}", immutable_reference);  // if using sentence first, this is dead too
    println!("{}", sentence);
}


// INTERIOR MUTABILITY
// ====================
//
// For more complex data types, we can only declare mutability on the entire 
// type. All fields are either immutable or mutable.

fn ex6() {
    struct Coordinate {
        x: i32,
        y: i32,
    }

    let mut coord = Coordinate { x: 20, y: 20 };

    // We can mutate each field because coord is mutable.
    coord.x = 12;
    coord.y = 91;
}

// Allowing mutability of a field when our data structure is otherwise immutable
// is called "Interior Mutability". Rust's std library provided us the 
// std::cell::Cell and std::cell::RefCell types which allow this capability.
//
// Be warned that these types can circumvent compile-time guarantees and
// generate runtime errors when not used properly. The std::cell documentation
// has more information about its implications.
