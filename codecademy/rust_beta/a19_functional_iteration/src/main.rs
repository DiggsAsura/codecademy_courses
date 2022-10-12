fn main() {
    ex1(); // Iteration
    ex2(); // collect()
    ex3(); // map()
    ex4(); // filter()
    ex5(); // enumerate()
    ex6(); // Laziness (for loop)
}

/* 
 * Functional Iteration
 * ======================
 *
 * Closures on their own provide only minor differences from functions. However, when functions
 * take functions as parameters, closures allow us to write very succinct code in a functional
 * style. (wth does that mean lol)
 *
 * This is best exemplified and most commonly encounterd when utilizing Rust's Iterators.
 *
 *
 * Iteration
 * ----------
 *
 * Any type that implements the Iterator trait gives us access to a plethora of methods that allow
 * us to operate on collections without having to use a for loop.
 *
 * We can create an iterator with the iter() method and then proceed through the collection with
 * next().
 */

fn ex1() {
    let numbers = [1, 2, 3];
    let mut numbers = numbers.iter();

    if let Some(first) = numbers.next() {
        println!("{first}");
    }
    if let Some(second) = numbers.next() {
        println!("{second}");
    }
    if let Some(third) = numbers.next() {
        println!("{third}");
    }
    if let Some(fourth) = numbers.next() {
        println!("{fourth}");
    } else {
        println!("No more enteries");
    }
}


/* 
 * Rust also provides us the into_iter() method for taking ownership of the items of a collection
 * and iter_mut() for accessing a mutable reference to each item.
 *
 * While calling next() is fun, the real strengths of iterators come from the other methods the
 * Iterator trait provides.
 * https://doc.rust-lang.org/std/iter/trait.Iterator.html
 */

/* 
 * Collect
 * --------
 *
 * The collect() method will transform an iterator back into a collection. Type annotations for the
 * returned type are required if they cannot be inferred.
 */

fn ex2() {
    let mut numbers = [10, 20, 30].iter();
    numbers.next();
    numbers.next();

    let remaining_numbers: Vec<&u32> = numbers.collect(); // [30]
    
    // Turbo-fish type annotation
    //let remaining_numbers = numbers.collect::<Vec<&u32>>();

    println!("{:?}", remaining_numbers);
}

// Since iterators are consuming, the above remaining_numbers is a Vec with a single value of 30.


/* 
 * Map
 * ----
 *
 * The map() method takes a closure that will operate on each value of the collection. Here are
 * doubling each item in our numbers array.
 */

fn ex3() {
    let numbers = [1, 2, 3];

    let nums: Vec<i32> = numbers.iter()
        .map(|x| x * 2)
        .collect();

    println!("{nums:?}"); // [2, 4, 6]
}



/* 
 * Filter
 * -------
 *
 * The filter() method will only return values that satisfy a provided boolean conditional. Here
 * are returning only uppercase characters.
 */

fn ex4() {
    let chars = ['a', '1', 'E', 'F'];

    let filtered: Vec<&char> = chars.iter()
        .filter(|c| c.is_uppercase())
        .collect();

    println!("{filtered:?}");  // ['E', 'F']
}


/* 
 * Enumerate
 * -----------
 *
 * We can access the indexes of a collection while iterating with the enumerate() method.
 */

fn ex5() {
    let names = ["Li", "Patrick", "Omar"];

    let enumerated: Vec<(usize, &&str)> = names.iter()
        .enumerate()
        .filter( |(i, n)| i > &1)
        .collect();

    println!("{enumerated:?}"); // [(2, "Omar")]
}


/* 
 * Laziness
 * ----------
 *
 * Iterators in Rust are lazy, which means they are not evaluated until needed. When we want to
 * apply an operation that only has a side effect, we should use a for loop to make sure our code
 * is being run. 
 */

fn ex6() {
    let numbers = [1, 2, 3];

    // This will compile but will not print our numbers
    numbers.iter()
        .map(|n| println!("map: {n}"));

    // This will print all the values of our collection
    for n in numbers {
        println!("for: {n}");
        std::thread::sleep_ms(1000);        
    }
}


/*
 * Implementing Iterator
 * -----------------------
 *
 * There are many other helpful methods such as reduce(), find(), enumerate(), and fold().
 *
 * We can gain access to all of these methods on our own custom types by implementing the Iterator
 * trait on our custom type. With next() being the only required method for this trait, we get a
 * lot of functionality for very little code.
 */

