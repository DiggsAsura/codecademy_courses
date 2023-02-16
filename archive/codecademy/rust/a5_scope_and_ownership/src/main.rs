fn main() {
    
    println!("{:?}", heap_clone());
    println!("{:?}", stack_vs_heap_2());
    println!("{:?}", stack_vs_heap_1());
    println!("{:?}", struct_test());
//    println!("{:?}", visibility());
    println!("{:?}", scope());
    println!("{:?}", p1_blocks());
    println!("{:?}", sum());    

    // This part is supposed to work, following Rust Beta course but it's no
    //
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

// When our crate is a library, all items denoted as public will be accessible 
// to anyone who imports our library. More information about pub and use
// can be found in the modules article.


// OWNERSHIP
// -----------
//
// Scoping rules in Rust are very strict, but with good reason. Managing
// lifetimes and mutability in a memory-safe way is much easier when we disallow
// accessing items from parent blocks. 
//
// Rules
// ------
//
// The rules that the Rust compiler follows to validate that we do not attempt
// unsafe behavior are as follows:
//
// 1. Each value in Rust has a variable that's called its owner
// 
// 2. There can only be one owner at a time.
//
// 3. When the owner goes out of scope, the value will be dropped.
//
// These rules of ownership have differing implications depending on whether
// our data is stored on the stack or the heap.
//
//
// Stack Vs Heap
// ---------------
//
// If we assign a variable to an existing variable with a stack-based type 
// such as i32, it will make a computationally inexpensive copy of that value.
//

fn stack_vs_heap_1() {
    let stack_1 = 32;
    let stack_2 = stack_1; // The value of 'stack_1' is copied into 'stack_2'

    // We now have two values we can work with
    println!("{stack_1}");
    println!("{stack_2}");
}

// When working with datatypes that utilize the heap, such as String, we cannot
// copy values from one variable to another since heap-based types do not
// implement the Copy trait.
//
// Instead of copying, Rust will instead move the value out of the original
// variable into the new one. 

fn stack_vs_heap_2() {
    let heap_1 = String::from("Only you can!");
    let heap_2 = heap_1; // The value of heap_1 is moved into heap_2

    // We cannot print 'heap_1' because it's now owned by 'heap_2'
    println!("{heap_2}");
}

// We can choose to clone() our data, which is equivalent to copying on the
// heap. But unlike implicit copying, cloning data must always be explicitly 
// stated.
//
// We can clone any type that implements the Clone trait.

fn heap_clone() {
    let heap_1 = String::from("Prevent corruption!");
    let heap_2 = heap_1.clone(); // We have now cloned the data

    println!("{heap_1}");
    println!("{heap_2}");
}

// Be aware that cloning is only necessary when we need another copy of the 
// data. When we are not in need of a separate copy, we can instead reference
// the data. 


// Functions
// -----------
//
// Ownership rules with functions work much the same way. 

// When we have a function that return a value, the ownership of that value is
// passed to the caller.

fn ownership_functions() {
    fn abc() -> String {
        "abs".to_string()
    }

    let letters = abc(); // The value created in 'abc()' is now owned by 
                         // 'letters'

    // When we have a function that passes a value through it, it can be 
    // thought of as temporarily taking ownership of that value until the
    // function call has completed.

    fn print_through(s: String) -> String {
        s
    }

    let finished = print_through(letters); // letters has been moved into 
                                           // finished
}

// NOT entirly sure whats going on in the last function here... But I hope it
// will make sense as I'm going. 
