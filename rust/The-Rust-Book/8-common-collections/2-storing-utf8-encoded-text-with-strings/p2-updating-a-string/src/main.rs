use std::fmt::format;

// Updating a String
//
// A String can grow in size and its contents can change, just like contents of a
// Vec<T>, if you push more data into it. In addition, you can conveniently use the
// + operator on the format! macro to concatenate String values.
//
//
// Appending to a String with push_str and push
//
// We can grow a String by using the push_str method to append a string slice, as shown
// in Listing 8-15:
fn main() {
    let mut s = String::from("foo");
    s.push_str("bar");

    listing_8_16();
    listing_8_17();
    listing_8_18();
    concatenate_multiple_strings();
    format_instead();
}
// 8-15: Appending a string slice to String using the push_str method

// After these two lines, s will contain foobar. The push_str method takes a string slice
// because we don't necessarily want to take ownership of the parameter. For example, in the
// code in Listing 8-16, we want to be able to use s2 after appending its contents to s1.
fn listing_8_16() {
    let mut s1 = String::from("foo");
    let s2 = "bar";
    s1.push_str(s2);
    println!("s2 is {}", s2);
}
// 8-16: Using a string slice after appending its contents to a String

// If the push_str method took ownership of s2, we wouldn't be able to print its value on
// the last line. However, this code works as we'd expect!
//
// The push method takes a single character as a parameter and adds it to the String.
// Listing 8-17 adds the letter "l" to a String using the push method:
fn listing_8_17() {
    let mut s = String::from("lo");
    s.push('l');
    println!("s is {}", s);
}
// 8-17: Adding one character to a String value using push

// As a result, s will contain lol.
//
//
// Concatenation with the + Operator or the format! macro
//
// Often, you'll want to combine two existing strings. One way to do so is to use the
// + operator, as shown in Listing 8-18:
fn listing_8_18() {
    let s1 = String::from("Hello, ");
    let s2 = String::from("world!");
    let s3 = s1 + &s2; // note s1 has been moved here and can no longer be used
    println!("s3 is {}", s3);
}
// 8-18: Using the + operator to combine two String values into a new String value

// The string s3 will contain Hello, world! The reason s1 is no longer valid after the
// addition, and the reason we used a reference to s2, has to do with the signature of the
// method that's called when we use the + operator. The + operator uses the add method,
// whose signature looks something like this:
//
// fn add(self, s: &str) -> String {}
//
// In the standard library, you'll see add defined using generics and associated types. Here
// we've substituted in concrete types, which is what happens when we call thie method
// with String values. We'll discuss generics in Chapter 10. This signature gives us the
// clues we need to understand the tricky bits of the + operator.
//
// First, s2 has an &, meaning that we're adding a reference of the second string to the
// first string. This is because of the s parameter in the add function: we can only add
// a &str to a String; we can't add two String values together. But wait-the type of &s2
// is &String, not &str, as specified in the second parameter to add. So why does Listing 8-18
// compile?
//
// The reason we're able to use &s2 in the call to add is that the compiler can coerce the
// &String argument into a &str. When we call the add method, Rust uses a deref coercion,
// which here turns &s2 into &s2[..]. We'll discuss deref coercion in more depth in
// Chapter 15. Because add does not take ownership of the s paramter, s2 will still be
// a valid String after this operation.
//
// Second, we can see in the signature that add takes ownership of self, because self does
// not have an &. This means s1 in Listing 8-18 will be moved into the add call and
// will no longer be valid after that. So although let s3 = s1 + &s2; looks like it will
// copy both strings and create a new one, this statement instead does the following:
//
// 1. add takes ownership of s1
// 2. it appends a copy of the contents of s2 into s1,
// 3. and then it returns back ownership of s1.
//
// If s1 has enough capacity for s2, then no more memory allocation occur. However, if s1
// does not have enough capacity for s2, then s1 will internally make a larger memory
// allocation to fit both strings.
//
// If we need to concatenat multiple strings, the behavior of the + operator gets
// unwieldy:

fn concatenate_multiple_strings() {
    let s1 = String::from("tic");
    let s2 = String::from("tac");
    let s3 = String::from("toe");

    let s = s1 + "-" + &s2 + "-" + &s3;
    println!("s is {}", s);
}

// At this point, s will be tic-tac-toe. With all of the + and " characters, it's difficult
// to see what's going on. For more complicated string combining, we can instead use
// the format! macro:

fn format_instead() {
    let s1 = String::from("tic");
    let s2 = String::from("tac");
    let s3 = String::from("toe");

    let s = format!("{}-{}-{}", s1, s2, s3);
    println!("s is {}", s);
}
// This code also sets s to tic-tac-toe. The format! macro works like println!, but instead
// of printing the output to the screen, it returns a String with the contents. The version
// of the code using format! is much easier to read, and the code generated by format! macro
// uses references so that this call doesn't take ownership of any of its parameters.

