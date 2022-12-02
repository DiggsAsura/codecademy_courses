/* String Slices
 *
 * A string slice is a reference to part of a String, and it looks like this:
 *
 *      let s = String::from("hello world");
 *
 *      let hello: &str = &s[0..5];
 *      let world: &str = &s[6..11];
 *      let s2: &String = &s;           // not a slice, for comparison
 *
 *
 * Rather than a reference to the entire String (like s2), hello is a reference to a portion of the
 * String, specified in the extra [0..5] bit. We create slices using a range within brackets by
 * specifying [starting_index..ending_index], where starting_index is the first position in the
 * slice and ending_index is one more than the last position in the slice. Internally, the slice
 * data structure stores the starting position and the length of the slice, which corresponds to
 * ending_index minus starting_index. So in the case of let world = &s[6..11];, world would be a
 * slice that contains a pointer to the byte at index 6 of s with a length value of 5.
 *
 * Figure 4-6 shows this in a diagram.
 *
 *
 *
 *      s2                         s
 * name | value         name        | value
 * ptr  |   --------->  ptr         |   ------------|
 *                      len         | 11            |
 *                      capacity    | 11            |
 *                                                  |
 *                      hello                       |       index   | value
 *                      name        | value         |-----> 0       | h
 *                      ptr         |   ------------|       1       | e
 *                      len         | 5                     2       | l
 *                                                          3       | l
 *                      world                               4       | o
 *                      name        | value                 5       |
 *                      ptr         | --------------------> 6       | w
 *                      len         | 5                     7       | o
 *                                                          8       | r
 *                                                          9       | l
 *                                                          10      | d
 *
 * Figure 4-6: String slice referring to part of a String
 *
 *
 * Note that there is a difference between s2: &String, a reference to an owned string, and hello:
 * &str, a string slice. s2 is two pointers away from the string data, while hello directly points
 * to the string data without going through s.
 *
 * With Rust's .. range syntax, if you want to start at index zero, you can drop the value before
 * the two periods. In other words, these are equal: 
 *
 *      let s = String::from("hello");
 *
 *      let slice = &s[0..2];
 *      let slice = &s[..2];
 *
 * By the same token, if your slice includes the alst byte of the String, you can drop the trailing
 * number. That means these are equal:
 *
 *      let s = String::from("hello");
 *
 *      let len = s.len();
 *
 *      let slice = &s[3..len];
 *      let slice = &s[3..];
 *
 * You can also drop both values to take a slice of the entire string. So these are equal:
 *
 *      let s = String::from("hello");
 *
*      let len = s.len();
*
*      let slice = &s[0..len];
*      let slice = &s[..];
*
* Note: String slice range indices must occur at valid UTF-8 character boundaries. If you attempt
* to create a string slice in the middle of a multibyte character, your program will exit with an
* error. For the purposes of introducing string slices, we are assuming ASCII only in this section;
* a more through discussion of UTF-8 handling is in the "Storing UTF-8 Encoded Text with Strings"
* section of Chapter 8.
*
*
* With all this information in mind, let's rewrite first_word to return a slice. The type that
* signifies "string slice" is written as &str:
 */

fn first_word(s: &String) -> &str {
    let bytes = s.as_bytes();

    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
            return &s[0..i];
        }
    }

    &s[..]
}

/* We get the index for the end for the word in the same way as we did in listing 4-7, by looking
 * for the first occurence of space. When we find a space, we return a string slice using the start
 * of the string and the index of the space as the starting and ending indices.
 *
 * Now when we call first_word, we get back a single value that is tied to the underlying data. The
 * value is made up of a reference to the starting point of the slice and the number of elements in
 * the slice. 
 *
 * Returning a slice would also work for a second_word function:
 *
 *      fn second_word(s: &String) -> &str {
 *
 * We now have a straightforward API that's much harder to mess up, because the compiler will
 * ensure the references into the String remain valid. Remember the bug in the program in Listing
 * 4-8, when we got the index to the end of the first word but then cleared the string so our index
 * was invalid? That code was logically incorrect but didn't show any immediate errors. The
 * problems would show up later if we kept trying to use the first word index with an emptied
 * string. Slices make this bug impossible and let us know we have a problem with our code much
 * sooner. Using the slice version of first_word will throw a compile-time error:
 *
 fn main() {
    let mut s = String::from("hello world");

    let word = first_word(&s);

    s.clear();  // error!
    
    println!("the first word is: {}", word);
}

 * Here's the compiler error:
 
 $ cargo run
   Compiling ownership v0.1.0 (file:///projects/ownership)
error[E0502]: cannot borrow `s` as mutable because it is also borrowed as immutable
  --> src/main.rs:18:5
   |
16 |     let word = first_word(&s);
   |                           -- immutable borrow occurs here
17 | 
18 |     s.clear(); // error!
   |     ^^^^^^^^^ mutable borrow occurs here
19 | 
20 |     println!("the first word is: {}", word);
   |                                       ---- immutable borrow later used here

For more information about this error, try `rustc --explain E0502`.
error: could not compile `ownership` due to previous error

 * Recall from the borrowing rules that if we have an immutable reference to something, we cannot
 * also make a mutable reference. Because clear needs to truncate the String, it needs to get a
 * mutable reference. The println! after the call to clear uses the reference in word, so the
 * immutable reference must still be active at that point. Rust disallows the mutable reference in
 * clear and the immutable reference in word from existing at the same time, and compilation fails.
 * Not only has Rust made our API easier to use, but it has also eliminated an entire class of
 * errors at compile time! 
 */

fn main() {
    let s = String::from("hello world");

    let hello: &str = &s[0..5];
    let world: &str = &s[6..11];
    let s2: &String = &s;

    println!("{hello}");
    println!("{s2}");

    println!("\nfirst_word():");
    let fword = String::from("hello");
    let fw = first_word(&fword);
    println!("{fw}");
    println!("{fword}");
    fn testing_something(s: String) -> String {
        let mut s2 = String::from(" from inside");
        let mut s3 = s + &s2;
        s3
    }
    let ts = testing_something(fword);
    println!("{ts}");
//    println!("{fword}"); // yup does not work
}

