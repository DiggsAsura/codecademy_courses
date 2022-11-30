/* Implicit Borrowing
*
* Borrows and references are used -everywhere- in Rust. So to make Rust less verbose, the Rust
* compiler has a number of strategies for implicitly creating borrows and converting references.
* For example, mutable references can be moved by direct assignment: */
fn main() {
    let mut s = String::from("hello world");
    let s2 = &mut s;
    let s3 = s2;
//    println!("s2 not valid: {s2}"); // Does not work, as its moved into s3.

    // consume     
    ex2();
}
fn consume(_s: &mut String) {}

/* But mutable references are NOT moved by function calls:
*/
fn ex2() {
    let mut s = String::from("Hello World");
    let s2 = &mut s;
    consume(s2);
    println!("{}", s2); // Valid because s2 is NOT moved
}

/* This fact contradicts what you learend in the previous section! But this program works because
* Rust automatically -reborrows- mutable references when passed as input to a function call. That
* way, Rust programmers don't have to keep creating new mutable references on every call. Inside
* the compiler, the call to consume is transformed to look like this: */

// consume(&mut *s2)

/* Therefor s2 is -not moved by- consume, but rather -borrowed- by consume.
*
* The complete set of implicit behavior is beyond of scope of this chapter. We will introduce these
* rules as the book goes on, for example how Rust deals with methods (Section 5.3) and smart
* pointers (Section 15.2). For now, just be aware that these rules exist. If you come across a
* piece of Rust code that seems wrong but actually compiles, then these rules might be the reason.
*
* Conversely, Rust will never implicitly convert borrows in a way that would violate ownership. For
* example, if you use an immutable reference &x where mutable reference &mut x is expected, Rust
* will not automatically convert &x to &mut x. You have to write out &mut x yourself.
*/

