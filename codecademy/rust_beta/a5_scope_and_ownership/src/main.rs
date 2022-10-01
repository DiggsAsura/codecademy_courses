fn main() {

    println!("{:?}", struct_test());
//    println!("{:?}", visibility());
    println!("{:?}", scope());
    println!("{:?}", p1_blocks());
    println!("{:?}", sum());    

    // This part is supposed to work, following Rust Beta course but it's not
    // really doing that or..?
    //let sum = {
    //    let number_1 = 111;
    //    let number_2 = 222;
    //    number_1 + number_2;
    //};
    //println!("{:?}", sum);
}


fn p1_blocks() -> i32 {

    // In Rust, code can be separated into blocks. A block of code is a 
    // collection of statements and an optional expression contained with
    // {}:

    // Statement block
    {
        let number_1 = 11;
        let number_2 = 31;
        let sum = number_1 + number_2;
        println!("{sum}");
    }

    // Expression block
    {
        let number_1 = 1;
        let number_2 = 2;
        number_1 + number_2
    }

    // Blocks can be treated as the single statement or expression they evaluate
    // to. This means we can assign variables to a block of code:

//    let sum = {
//        let number_1 = 11;
//        let number_2 = 200;
//        number_1 + number_2
//    };
//    println!("{sum}");

}

fn sum() -> i32 {
    let number_1 = -11;
    let number_2 = -12;
    number_1 + number_2
}


// SCOPE
// -------

// Scope is the concept of wheter or not a particular item exists in memory
// and is accessible at a certain location in our codebase. In Rust, the scope
// of any particular item is limited to the block it is contained in.
//
// When a block is closed, all of its values are released from memory and
// are then considered out-of-scope. If an item is accessible, it is considered
// in-scope.
//
// The following example showcases how scoping works by shadowing a variable.
// Note how our last println!() call will print "10" because our second 
// declaration of a number is dropped from memory at the end of its containing
// block.
//

fn scope() {
    let number = 10;
    {
        println!("{number}"); // Prints 10
        
        let number = 22;
        println!("{number}"); // Prints 22
    }
    // Our second declaration of 'number' is dropped from memory after }. 
    // It is now considered out of scope.

    println!("{number}"); // Prints 10
}

// VISIBILITY
// -----------
//
// We can make an item accessible outside of its normal scope by denoting it as
// public with the pub keyword.
//
// All items in Rust are private by default. Private items can only be accessed
// within their declared module and any children modules. 
//

//fn visibility() {
//    mod numbers {
//        pub const ZERO: i32 = 0;
//    }
//
//    mod another_scope {
//        use super::numbers::ZERO;
//
//        fn print_zero() {
//            println!("{ZERO}");
//        }
//    }
//}
//
// (above does not work written like this)
//

//fn visibility() {
//    {
//        pub const ZERO: i32 = 0;
//    }
//
//    println!("{ZERO}");
//}

// above does not work either hm. 
//

fn struct_test() {
    pub struct Number {
        pub value: i32,
    }

    let mut number = Number { value: 0 };

    number.value += 1;
    println!("{}", number.value);
    println!("End of struct_test()");
}

