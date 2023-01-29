// Running Code on Cleanup with the Drop Trait
// ==================================================
//
// The second trait important to the smart pointer pattern is Drop, which lets you customize what
// happens when a value is about to go out of scope. You can provide an implementation for the Drop
// trait on any type, and that code can be used to release resources like files or network
// connections.
//
// We're introducing Drop in the context of smart pointers because the functionality of the Drop
// trait is almost always used when implementing a smart pointer. For example, when a Box<T> is
// dropped it will deallocate the space on the heap that the box points to.
//
// In some languages, for some types, the programmer must call code to free memory or resources
// every time they finish using an instance of those types. Examples include file handles, sockets,
// or locks. If they forget, the system might become overloaded and crash. In Rust, you can specify
// that a particular bit of code be run whenever a value goes out of scope, and the compiler will
// insert this code automatically. As a a result, you don't need to be careful about placing
// cleanup code everywhere in a program that an instance of a particular type is finished with -
// you still won't leak resources!
//
// You specify the code to run when a value goes out of scope by implementing the Drop trait. The
// Drop trait requires you to implement one method named drop that takes a mutale reference to
// self. To see when Rust calls drop, let's implement drop with println! statements for now.
//
// Listing 15-14 shows a CustomSmartPointer struct whose only custom functionality is that it will
// print Dropping CustomSmartPointer! when the instance goes out of scope, to show when Rust runs
// the drop function.

struct CustomSmartPointer {
    data: String,
}

impl Drop for CustomSmartPointer {
    fn drop(&mut self) {
        println!("Dropping CustomSmartPointer with data {}!", self.data);
    }
}

fn main() {
    let c = CustomSmartPointer {
        data: String::from("my stuff"),
    };
    let d = CustomSmartPointer {
        data: String::from("other stuff"),
    };

    println!("CustomSmartPointers created.");
}

// 15-14: A CustomSmartPointer struct that implements the Drop trait where we would put our cleanup
// code

// The Drop trait is included in the prelude, so we don't need to bring it into scope. We implement
// hte Drop trait on CustomSmartPointer and provide an implementation for the drop method that
// calls println!. T-he body of the drop function is where you would place any logic that you
// wanted to run when an instance of your type goes out of scope. We're printing some text here to
// demonstrate viually when Rust will call drop.
//
// In main, we create two instances of CustomSmartPointer and then print CustomSmartPointers
// created. At the end of main, our instance of CustomSmartPointer will go out of scope, and Rust
// will call the code we put in the drop method, printing our final message. Note that we didn't
// need to call the drop method explicitly.
//
// When we run this program, we'll see the following output:

/*
$ cargo run
   Compiling drop-example v0.1.0 (file:///projects/drop-example)
    Finished dev [unoptimized + debuginfo] target(s) in 0.60s
     Running `target/debug/drop-example`
CustomSmartPointers created.
Dropping CustomSmartPointer with data `other stuff`!
Dropping CustomSmartPointer with data `my stuff`!
*/

// Rust automatically called drop for us when our instances went out of scope, calling the code we
// specified. Variables are dropped in the reverse order of their creation, so d was dropped before
// c. Variables are dropped in the reverse order of their creation, so d was dropped before c. This
// example's purpose is to give you a visual guide to how the drop method works; usually you would
// specify the cleanup code that your type needs to run rather than a print message.
