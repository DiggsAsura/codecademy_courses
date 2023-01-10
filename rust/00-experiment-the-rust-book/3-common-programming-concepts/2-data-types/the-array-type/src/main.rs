/* The Array Type
 *
 * Unlike tuple, every element in an array needs to be of same type. And unlike arrays in some
 * other languages, arrays in Rust have fixed length. 
 */

fn main() {
    let a = [1, 2, 3, 4, 5];

    /* Arrays -> STack 
     *
     * Arrays are useful when you want your data allocated on the stack rather than the heap (chap
     * 4) or when you want to ensure you always have a fixed number of elements. An array isn't as
     * the vector type, though. A vector is a similar collection type provided by the standard
     * library that IS allows to grow or shrink in size. If you're unsure wheter to use an array or
     * a vector, chances are you should use a vector. Chap 8 discuss vectors in more detail.
     *
     *
     * However, arrays are more useful when you know the number of elements will not need to
     * change. For example, if you were using the names of the month in a program, you would
     * probably use an array rather than a vector because you know it will always contain 12
     * elements. */

    let months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];


    /* You write an array's type using square brackets with the type of each element, a semicolon
     * and then the number of elements in the array: 
     */

    let b: [u8; 3] = [1, 2, 3];

    /* You can also initialize an array to contain the same value for each element by specifying
     * the initial value, followed by a semicolon, and then the length of the array in square
     * brackets, as shown: */

    let c = [3; 5];
    println!("{:?}", c);


    /* Accessing Elements
     * ------------------
     *
     * An array is a single chunk of memory of a known, fixed size that can be allocated on the
     * stack. You can access elements of an array using indexing, like this: */

    let first   = a[0];
    let second  = a[1];

    /* Invalid Array Element Access
     *
     * Let's see what happens if you try to access an element of an array that is past the end of
     * the array. Say you run this code, similar to the guessing game in Chapter 2, to get an array
     * index from the user: */

    use std::io;
    println!("\nPlease enter an array index.");

    let mut index = String::new();
    io::stdin()
        .read_line(&mut index)
        .expect("Failed to read line");

    let index: usize = index.trim().parse().expect("Index entered was not a number");

    let element = a[index];
    println!("The value of the element at index {index} is : {element}");


    /* This code compiles, but will panic if you enter a value above the last array element.
     * Runtime error at the point of using an invalid value in the indexing operation. The program
     * exited with an error message and didn't execute the final println! statement. When you
     * attempt to access an element using indexing, Rust will check the index you've specified is
     * less than the array length. If the index is greater than or equal to the length, Rust will
     * panic. This check has to happen at runtime, especiallly in this case, because the compiler
     * can't possibly know what value a user will enter when they run the code later. 
     *
     *
     * This is an example of Rust's memory safety principles in action. In many low-level
     * languages, this kind of check is not done, and when you provide an incorrect index, invalid
     * memory can be accessed. Rust protects you against this kind of error by immediately exiting
     * instead of allowing the memory access and continuing. Chap 9 discuss more of Rust's error
     * handling and how you can write readable, safe code that neither panics nor allows invalid
     * memory access. */

}
