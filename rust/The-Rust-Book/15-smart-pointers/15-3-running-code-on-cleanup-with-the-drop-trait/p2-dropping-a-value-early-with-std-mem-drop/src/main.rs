// Dropping a Value Early with std::mem::drop
// ==========================================
//
// Unfortunately, it's not straightforward to disable the automatic drop functionality. Disabling
// drop isn't usually necessary; the whole point of the Drop trait is that it's taken care of
// automatically. Occasionally, however, you might want to clean up a value early. One example is
// when using smart pointers that manage locks: you might want to force the drop method that
// releases the lock so that other code in the same scope can aquire the lock. Rust doesn't let you
// call the Drop trait's drop method manually; instead you have to call the std::mem::drop function
// provided by the standard library if you want to force a value to be dropped before the end of
// its scope.
//
// If we try to call the Drop trait's drop method manually by modifying the main function from
// Listing 15-14, as shown in Listing 15-15, we'll get a compiler errer:

struct CustomSmartPointer {
    data: String,
}

impl Drop for CustomSmartPointer {
    fn drop(&mut self) {
        println!("Dropping CustomSmartPointer with data '{}'!", self.data);
    }
}
/*
fn main() {
    let c = CustomSmartPointer {
        data: String::from("some data"),
    };
    println!("CustomSmartPointer created.");
    c.drop();
    println!("CustomSmartPointer dropped before the end of main.");
}
*/
// Listing 15-15: Attempting to call the drop method from the Drop trait manually to clean up
// early

// When we try to compile this code, we'll get this error:

/*
$ cargo run
   Compiling drop-example v0.1.0 (file:///projects/drop-example)
error[E0040]: explicit use of destructor method
  --> src/main.rs:16:7
   |
16 |     c.drop();
   |     --^^^^--
   |     | |
   |     | explicit destructor calls not allowed
   |     help: consider using `drop` function: `drop(c)`

For more information about this error, try `rustc --explain E0040`.
error: could not compile `drop-example` due to previous error
*/

// This error message states that we're not allowed to explicitly call drop. The error message uses
// the term destructor, which is the general programming term for a function that cleans up an
// instance. A destructor is analogous to a constructor, which creates an instance. The drop
// function in Rust is one particular destructor.
//
// Rust doesn't let us call drop explicitly because Rust would still automatically call drop on the
// value at the end of main. This would cause a double free error because Rust would be trying to
// clean up the same value twice.
//
// We can't disable the automatic insertion of drop when a value goes out of scope, and we can't
// call the drop method explicitly. So, if we need to force a value to be cleaned up early, we use
// the std::mem::drop function.
//
// The std::mem::drop function is different from the drop method in the Drop trait. We call it by
// passing as an argument the value we want to force drop. The function is in the prelude, so we
// can modify main in Listing 15-15 to call the drop function, as shown in Listing 15-16:

fn main() {
    let c = CustomSmartPointer {
        data: String::from("some data"),
    };
    println!("CustomSmartPointer created.");
    drop(c);
    println!("CustomSmartPointer dropped before the end of main.");
}

// 15-16: Calling std::mem::drop to explicitly drop a value before it goes out of scope

// Running this code will print the following:

/*
$ cargo run
   Compiling drop-example v0.1.0 (file:///projects/drop-example)
    Finished dev [unoptimized + debuginfo] target(s) in 0.73s
     Running `target/debug/drop-example`
CustomSmartPointer created.
Dropping CustomSmartPointer with data `some data`!
CustomSmartPointer dropped before the end of main.
*/

// The text Dropping CustomSmartPointer with data 'some data'! is printed between the
// CustomSmartPointer created. and CustomSmartPointer dropped before the end of main. text, showing
// that the drop method code is called to drop c at that point.
//
// You can use code specified in a Drop trait implementation in many ways to make cleanup
// convenient and safe: for instance, you could use it to create your own memory allocator! With
// the Drop trait and Rust's ownership system, you don't have to remember to clean up because Rust
// does it automatically.
//
// You also don't have to worry about problems resulting from accidentally cleaning up values still
// in use: the ownership system that makes sure references are always valid also ensures that drop
// gets called only once when the value is no longer being used.
//
// Now that we've examined Box<T> and some of the characteristics of smart pointers, let's look at
// a few other smart pointers defined in the standard library.
