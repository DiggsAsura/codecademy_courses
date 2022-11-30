#![allow(dead_code)]
#![allow(unused_variables)]
/* Mutable references
*
* We can fix the code from Listing 4-6 to allow us to modify a borrowed value with just a few small
* tweaks that use, instead, a mutlabe reference. */

fn main() {
    let mut s = String::from("hello");

    change(&mut s);

    println!("{s}");

    // ex4
    ex4();
}

fn change(some_string: &mut String) {
    some_string.push_str(", world");
}

/* First, we change s to be mut. Then we create a mutable reference with &mut s where we call the
* change function, and update the function signature to accept a mutable reference with
* some_string: &mut String. This makes it very clear that the change function will mutate the value
* it borrows. 
*
* Mutable references have one big restriction: if you have a mutable reference to a value, you can
* have no other references to that value. This code that attemps to reference s will fail: */

/*
fn ex2() {
    let mut s = String::from("hello");

    let r1 = &mut s;
    let r2 = &mut s;

    println!("{}, {}", r1, r2);
}
*/

/*
This error says that this code is invalid because we cannot borrow s as mutable more than wonce at a time. The first mutable borrow is in r1 and mut last until it's used in the println!, but between creation of that mutable reference and its usage, we tried to creat another mutable refernece in r2 that borrows the same data as r1.

The restriction preventing mutliple mutable references to the same data at the time allows for mutattion but in a very controlled fashin. It's something that new Rustaceans struggle with, because most languages let you mutate whenever you'd like. The benefit of having this restriction is that Rust can prevent data races at compile time. A data race is similar to a race condition and happens when these three behaviors occus:
    - Two or more pointers access the same data at the same time.
    - At least one of the pointers is being used to write to the data.
    - There's no mechanism being used to synchronize access to the data.

Data races cause undefined behavior and can be difficult to diagnose and fix when you're trying to track them down at runtime; Rust prevents this problem by refusing to compile with data races!

As always, we can use curly brackets to create a new scope, allowing for multiple mutable references, just not simulationeous ones:  */

fn ex3() {
    let mut s = String::from("hello");
    {
        let r1 = &mut s;
    } // r1 goes out of scope here, so we can make a new reference with no problem.
    
    let r2 = &mut s;
}

/* Rust enforces a similar rule for combining mutable and immutable references. This code results
* in an error: */

/* let mut s = String::from("hello");
*
* let r1 = &s;  //no problem
* let r2 = &s;  // no problem
* let r3 = &mut s; // BIG PROBLEM
*
* Here's the problem:
*
* Cannot borrow 's' as mutable because it is also borrowed as immutable
*
*
*
* Whew! We -also- cannot have a mutable reference while we have an immutable one to the same value. 
*
* Users of an immutable reference don't expect the value to suddenly change fout from under them!
* However, multiple immutable references are allowed because no one who is just reading the data
* has the ability to affect anyone else's reading of the data.
*
* Note that a reference's scope starts from where it is introduced and continues through the last
* time that referene is used. For instance, this code will compile because the last usage of the
* immutable references, the println!, occurs before the mutable reference is introduced:
*/

fn ex4() {
    let mut s = String::from("hello");

    let r1 = &s; // no problem
    let r2 = &s; // no problem
    println!("{} and {}", r1, r2);
    // variables r1 and r2 will not be used after this point
    println!("{r1} {r2}"); // so this one is ok

    let r3 = &mut s; // no problem
    println!("r3 {}", r3);

    // won't work:
    //println!("{r1}");

}

/* The scopes of the immutable references r1 and r2 end after the println! where they are last
* used, which is before the mutable reference r3 is created. These scopes don't overlap, so this
* code is allowed. The ability of the compiler to tell that a reference is no longer being used at
* this point beofre the end of the scope is called Non-Lexical Lifetimes (NLL for short), and you
* can read more about it in The Edition Guide
* https://doc.rust-lang.org/edition-guide/rust-2018/ownership-and-lifetimes/non-lexical-lifetimes.html
*
* Even though borrowing errors may be frustrating at times, remember that it's the Rust compiler
* pointing out a potential bug early (at compile time rather than at runtime) and showing you
* exactly where the problem is. Then you don't have to track down why your data isn't what you
* thought it was. 
*/

