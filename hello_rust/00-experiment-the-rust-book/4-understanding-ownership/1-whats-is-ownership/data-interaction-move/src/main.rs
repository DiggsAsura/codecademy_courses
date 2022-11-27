/* Ways Variables and Data Interact: Move
 * ----------------------------------------
 *
 * Multiple variables can interact with the same data in different ways in Rust. Let's look at an
 * example using an integer: */
fn main() {
    // ex 1
    {
        let x = 5;
        let y = x;
    }

    /* We can probably guess what this is doing: "bind the value 5 to x; then make a copy of the
     * value in x and bind it to y." We now have two variables, x and y, and both equal 5. This is
     * indeed what is happening, because integers are simple values with a known, fixed size, and
     * these two 5 values are pushed onto the stack. 
     *
     * Now let's look at the String version:
     */

    // ex 2
    {
        let s1 = String::from("hello");
        let s2 = s1;
    } 

    /* This looks very similar, so we might assume that the way it works would be the same: that
     * is, the second line would make a copy of the value in s1 and bind it to s2. But this isn't
     * quite what happens.
     *
     * Take a look at Fig 4-1 (https://rust-book.cs.brown.edu/img/trpl04-01.svg) to see what is
     * happening to String under the covers. A String is made up of three parts, shown on the left:
     * a pointer to the memeory that holds the contents of the string, a length, and a capacity.
     * This group of data is stored on the stack. On the right is the memory on the heap that holds
     * the contents.
     *
     *          s1 data                             heap data 
     *      name    |   value   |               index   |   value   |
     *      ptr     |     ------|---------->        0   |   h       |
     *      len     |   5       |                   1   |   e       |
     *  capacity    |   5       |                   2   |   l       |
     *                                              3   |   l       |
     *                                              4   |   o       | 
     *
     * Length:
     * The length is how much memory, in bytes, the contents of the String is currently using. 
     *
     * Capacity:
     * The capacity is the total amount of memory, in bytes, that the STring has received from the
     * allocator. 
     *
     * The difference between length and capacity matters, but not in this context, so for now,
     * it's fine to ignore the capacity.
     *
     *
     * When we assign s1 to s2, the String data is copied, meaning we copy the pointer, the length,
     * and the capacity that are on the stack. We do not copy the data on the heap that the pointer
     * refers to. In other words, the data representation is memory looks like figure 4-2
     * (https://rust-book.cs.brown.edu/img/trpl04-02.svg)
     *
     * Fig 4-2
     *  s1       
     *  name    | value
     *  ptr     |     -----------
     *  len     |   5            \          HEAP DATA
     *  cap.    |   5             \         index   | value   
     *                              -->     0       | h 
     *  s2                        /         1       | e
     *  name    | value          /          2       | l
     *  ptr     |     -----------           3       | l 
     *  len     |   5                       4       | o
     *  cap.    |   5
     *
     *
     * So the HEAP DATA is not copied, just the pointer/length/capacity! That would be very
     * expensive in terms of runtime performance if the data on the heap were large. 
     */


    /* Earlier, we said that when a variable goes out of scope, Rust automatically calls the drop
     * function and cleans up the heap memory for that variable. But Figure 4-2 shows both data
     * pointers pointing to the same locations. This is a problem: when s2 and s1 go out of scope,
     * they will both try to free the same memory. This is known as a double free error and is one
     * of the memory safety bugs we mentioned previously. Freeing memory twice can lead to memory
     * corruption, which can potentially lead to security vulnerabiliites. 
     *
     * To ensure memory safey, after the line let s2 = s1, Rust considers s1 as no longer valid.
     * Therefore, Rust doesn't need to free anything when s1 goes out of scope. Check out what
     * happens when you try to use s1 after s2 is created; it won't work:
     *
     *  let s1 = String::from("hello");
     *  let s2 = s1;
     *
     *  println!("{}, world!", s1);         // s1 is moved to s2
     *
     * You'll get an error like this because Rust prevents you from using the invalid reference.
     *
     *
     * If you've heard the terms shallow copy and deep copy while working with other languages, the
     * concept of copying the pointer, length and capacity without copying the data probably sounds
     * like making a shallow copy. But because Rust also invalidates the first variable, instead of
     * calling it a shallow copy, it's known as a -move-. In this example, we would say that s1 was
     * MOVED into s2. So what actually happens is shown in Figure 4-4.
     *
     * Fig2-2 with greyed out s1.
     *
     * That solves our problem! With only s2 valid, when it goes out of scope, it alone will free
     * the memory, and we're done.
     *
     * In addition, there's a design choice that's implied by this: Rust will never automatically
     * create "deep" copies of your data. Therefore, any automatic copying can be assumed to be
     * inexpensive in terms of runtime performance. */
}

