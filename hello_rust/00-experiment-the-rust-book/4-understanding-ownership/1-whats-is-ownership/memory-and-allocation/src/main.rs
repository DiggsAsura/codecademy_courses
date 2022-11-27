/* So, what's the difference between String (mutable) and &str (immutable)? Why can String be
 * mutated but literals cannot? The difference is how these two types deal with memory... */

/* Memory and Allocation
 * ----------------------
 *
 * String literal type: &str
 *      Here we know the size/content at compile time. The text is hardcoded directly into the
 *      executeable. Make it fast and efficient, but these properties come from literals
 *      immutablility. Stack memory.
 *
 * String type: String
 *      Heap memory. Allocated on the heap.
 *      
 *          - Memory must be requested from the memory allocator at runtime.
 *          - We need a way of returning this memory to the allocator when we're done with our
 *            String.
 *      
 *      The first part is done by us when we call String::from. It's impelementation requests the
 *      memory it needs. This is pretty much universal in programming languages. 
 *
 *      However, the second part is different. In GC'd languages, the GC keeps track of and cleans
 *      up the memory that isn't being used anymore, and we don't need to think about it. In most
 *      languages without GC, it's our responsibility to identify when memory is no longer being
 *      used and call code to explicitly free it, just as we did to reuest it. Doing this correctly
 *      has historically been a difficult programming problem. If we forget, we'll waste memory. If
 *      we do it too early, we'll have an invalid variable. If we do it twice, that's a bug too. We
 *      need to pair exactly one allocate when exactly one free.
 *
 *      Rust takes a different path: the memeory is automatically returned once the variable that
 *      owns it goes out of scope. Here's a version of our scope example using a String instead of
 *      a literal: */
 
fn main() {
    { // ex 1
        let s = String::from("hello");      // s is valid from this point forward
        println!("{s}");
    }                                       // scope end, s is no longer valid (memory is freed)


    /*  When a variable goes out of sope, Rust calls a special function for us. This function is
     *  called drop(), and it's where the author of String can put the code to return the memory.
     *  Rust calls drop automatically at the closing curly bracket.
     *
     *  Note: this is similar to C++ RAII
     *
     *  This pattern has a profound impact on the way Rust code is written. It may seem simple
     *  right now, but the behavior of code can be unexpected in more complicated situations when
     *  we want to have multiple variables use the data we've allocated on the heap. Let's explore
     *  some of those situations now. */
}

