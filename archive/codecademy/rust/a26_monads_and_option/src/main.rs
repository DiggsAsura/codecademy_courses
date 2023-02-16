fn main() {
    ex1();
}

/* Monads and Option
 * ==================
 *
 * A monad is an inherent pattern of nature that expresses itself in computer science beautifully.
 * It is a hard concept to grasp at first, but fortunately, Rust's own Option<T> type is a perfect
 * example of the concept.
 *
 * (Well with an fuzzy explanation like that it does not make it better)
 *
 *
 * Why Monads?
 * ------------
 *
 * Monadic structures are a core part of the Rust language because they inherently solve a
 * multitude of problems. Specifically, they circumvent the decades-old issue of Null.
 *
 * If Rust is not your first programming language, you have likely encountered the concept of null
 * before and might have been really sad you did. You also may have utilized monadic types in other
 * languages without realizing it. 
 *
 *
 * Option
 * -------
 *
 * In programming languages, the monadic pattern expresses itself as a two-variant enum with
 * generic types on at least one of the variants. The Option<T> type from the std library is
 * precisely this. 
 *
 * Option is an enum with two variants, Some(T) and None. */

pub enum Option<T> {
    None,
    Some(T),
}

fn ex1() {
    let some_str = Some("has a value");
    //let no_str = None;

/* Since Option only has two variants and we can pass data along its Some(T) variant, it somewhat
 * acts as a boolean expression that is capable of passing a value along with it.
 *
 * Let's imagine we have a function that tries to return a String value from a databasae by
 * accessing the data's index. */

    fn get_by_index(i: u32) -> &'static str {
        // Imaginary code that access our database and returns a String.
        let imaginary = "ok";
        imaginary
    }

    let record = get_by_index(27);

/* If our database has a value at the supplied index, our function will return the Some(&str)
 * variant. If that index does not exist, it will return None.
 *
 * Now our code does not need to panic if the index does not exist because Option<T> has provided
 * us a way to handle both outcomes.*/

/* Unwrapping
 * -----------
 *
 * When we need to access the inner data of a monadic type, we can use the unwrap() method.
 * unwrap() will return the successful Some value but will also cause our program to panic if the
 * value is None. */

    let vehicle = Some("bisycle");
    let v = vehicle.unwrap();

    println!("{v}");

//    let vehicle = None;
//    vehicle.unwrap()  // This will panic 

/* Due to this, using the unwrap() method is helpful during development, but production code should
 * avoid using it unless you intentionally want your program to crash. 
 *
 * Other useful methods are unwrap_or(), unwrap_or_else(), and unwrap_or_default() for returning a
 * fallback value if our Option is None. We can also utilize is_some() and is_none() for performing
 * boolean checks on the value. */


/* But, what are monads?
 * -----------------------
 *
 * The mathematical definition of a monad involves the satisfaction of three distinct laws.
 * However, understanding monads through the lens of mathematical notation is merely a bonus. It is
 * not at all necessary to understand how monads operate and how best to utilize them in Rust. 
 *
 * You might even understand how to use Option<T> effectively, but still not grasp the larger idea
 * of what monad really is.
 *
 * That is ok.
 *
 * Monads are a truly difficult thing to understand. Like anything, it will take time and practice
 * to fully grasp the concept. One day the concept of monads will "click" and you will wonder why
 * it seemed so hard in the first place.
 *
 *
 * (For real - did i read a long article about what Monad is, where the answer is its ok to dont
 * know it - and not tell us what it is? lol Codecademy...)
 */



}
