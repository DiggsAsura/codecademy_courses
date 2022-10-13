fn main() {
    ex1();
    ex2();
    ex3();
    ex4();
    ex6();
}

/* 
 * Arrays and Vec
 * ================
 *
 * Rust provides us with a few different ways of creating collections of data of the same type. Two
 * of the most common are the array primitives and the Vec<T> type. 
 *
 *
 * Homogenous Collections
 * ------------------------
 *
 * As a general guideline, an array should be used when our collection has a fixed length. When we
 * are in need of a collection that can grow or shrink in size, we should utilize a Vec. 
 *
 * If you are looking to group together data of differing types, consider using a tuple or a
 * struct. 
 *
 *
 * Arrays
 * -------
 *
 * Arrays are the most basic homogenous collection in Rust. They have a fixed length, and their
 * data is stored on the stack. This makes arrays very efficient at runtime. 
 *
 * We can declare an array with square brackets, [], containing comma separated values. 
 */

fn ex1() {
    let integers = [1, 2, 3];

/*
 * We can initialize the values of an array from an expression rather than manually defining each
 * value. This takes the form of [expression; length] and is useful when creating large arrays.
 */

    // This will create an array with 20 chars of value 'e'
    let many_e = ['e'; 20];

    // We can use any expression to populate the default value.
    let initial_value = 'E';
    let more_e = [initial_value.to_ascii_lowercase(); 20];

    for c in more_e {
        println!("{c}");
        //std::thread::sleep_ms(500);
    }
}


/* 
 * Accessing Values
 * -----------------
 *
 * We can access values of collections using a special syntax referred to as index expression
 * syntax. This allows us to directly access a single value or an range of values by index.
 *
 *
 * Single Values
 * ---------------
 *
 * We can access a single value of a collection by placing the index of the desired item within
 * square brackets after the collection, collection[3]. It is important to remember that array
 * indexing in Rust, as with most languages, is 0-based.
 */

fn ex2() {
    let array_of_chars = ['a', 'b', 'c'];

    let letter_a = array_of_chars[0];
    let letter_c = array_of_chars[2];

    println!("{letter_a}");
    println!("{letter_c}");

    println!("{array_of_chars:?}");  // thought maybe this would only print b but did not, printed
                                     // it all.


    // Rather than directly supplying a number, we can utilize any expression which evaluates to
    // the type usize.
    
    fn one() -> usize { 1 }
    let letter_b = array_of_chars[one()];
    println!("{letter_b}");
}

    // If we try to acces an index that does not exist, our code will not compile.


/* 
 * Ranges 
 * -------
 *
 * We can access a range of values from a collection by supplying a beginning and ending index
 * separated by .. wihin our index expression.
 *
 * This special syntax is referred to as range syntax. The beginning index is inclusive and the
 * ending index is exclusive. 
 */

fn ex3() {
    let words = ["rise", "sun", "ship", "to", "sail"];

    let sunship = &words[1..3]; // ["sun", "ship"]   neat!
    
    for w in sunship {
        println!("{w}");
        std::thread::sleep_ms(100);
    }

    // If we omit the beginning or ending index, the range will continue until the respective
    // beginning or end.
    
    let head = &words[..2]; // ["rise", "sun"]
    println!("{head:?}");

    let tail = &words[2..]; // ["ship", "to", "sail"]
    println!("{tail:?}");

    let everything = &words[..]; 
    println!("{everything:?}");

}


/* 
 * Looping/Iteration
 * ------------------
 *
 * We can operate on the individual values of any collection with for loops and iterators.
 */

fn ex4() {
    let array_of_chars = ['a', 'b', 'c'];

    // Looping
    for c in array_of_chars {
        println!("{c}");
    }

    // Functional Iteration
    array_of_chars.iter().map(|c| println!("{c}"));
}


/* 
 * Vec
 * ----
 *
 * When we need a dynamically sized collection, the std library provides us the Vec<T> type. Vec,
 * commonly called a "Vector", stores it's data in the heap, which allows it to grow or shrink in
 * size. 
 *
 * There are many helpful methods (https://doc.rust-lang.org/std/vec/struct.Vec.html) already
 * available on the Vec type to make development more ergonomic.
 *
 * We can construct Vecs using methods such as new() and from(), but Rust also provides us the
 * vec![] macro that allow us to declare a Vec the same way we sould an array.
 */

fn ex5() {
    // Initialize an new, empty Vec
    let new_vec: Vec<char> = vec![];

    // Initialize with values
    let vec_of_chars = vec!['a', 'b', 'c'];

    // This is equivalent to the previous example, but utilizing methods
    let mut vec_of_chars = Vec::new();
    vec_of_chars.push('a');
    vec_of_chars.push('b');
    vec_of_chars.push('c');
}


/*
 * Accessing Values
 * ------------------
 *
 * Like arrays, we can use index expressions to access the values of a Vec. Unlike an array, if we
 * try to access an index that does not exist, our code will successfully compile but will panic at
 * runtime.
 *
 * To avoid this, accessing the values of a Vec is generally accomplished through methods such as
 * get() and first(). These methods return an Option<T> which allows us to handle situations where
 * the index does not exist. 
 */

fn ex6() {
    let vec_of_chars = vec!['a', 'b', 'c'];
    let a = vec_of_chars.first();  // Some('a')
    
    // Note that the 'get()' method does not use 0-based indexing
    let c = vec_of_chars.get(2);  // But it does...? 2 = c with 0 indexing no??
    println!("{c:?}");

    let f = vec_of_chars.get(9);  // none
    println!("{f:?}");
}


/* 
 * Other Collections
 * -------------------
 *
 * The std library has many other collections available such as VecDeque, BTreeMap, and HashMap,
 * Info about the available collections can be found in Rust's documentation.
 */

