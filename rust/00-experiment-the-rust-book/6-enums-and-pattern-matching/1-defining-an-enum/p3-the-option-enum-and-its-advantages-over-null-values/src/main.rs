/* The Option Enum and Its Advantages Over Null Values
 *
 * This section explores a case studo of Option, which is another enum defined by the standard
 * library. The Option type encodes the very common scenario in which a value could be something or
 * it could be nothing.
 *
 * For example, if you request the first of a list containing items, you would get a value. If you
 * request the first item of an empty list, you would get nothing. Expressing this concept in terms
 * of the type system means the compiler can check wheter you've handled all the cases you should
 * be handling; this functionality can prevent bugs that are extremly common in other programming
 * languages.
 *
 * Programming language design is often through of in terms of which features you include, but the
 * features you exclude are important too. Rust doesn't have the null feature that many other
 * languages have. Null is a value that means there is no value there. In languages with null,
 * variables can always be in one of two states: null or not-null.
 *
 * In his 2009 presentation "Null References: The Billion Dollar Mistake", Tony Hoare, the inventor
 * of null, has this to say:
 *
 * "I call it my billion-dollar mistake. At that time, I was designing the first comprehensive type
 * system for references in an object-oriented language. My goal was to ensure that all use of
 * references should be absolutely safe, with checking performed automatically by the compiler. But
 * I couldn't resist the temptation to put in a null reference, simply because it was so easy to
 * implement. This had led to innumerable errors, vulnerabilities, and system crashes, which have
 * probably caused a billion dollar of pain and damage in the last forty years."
 *
 * The problem with null values is that if you try to use a null value as a not-null value, you'll
 * get an error of some kind. Because this null or not-null property is pervasive, it's extremly
 * easy to make this kind of error.
 *
 * However, the concept that null is trying to express is still a useful one: a null is a value
 * that is currently invalid or absent for some reason.
 *
 * The problem isn't really with the concept but with the particular implementation. As such, Rust
 * does not have nulls, but it does have an enum that can encode the concept of a value being
 * present or absent. This enum is Option<T>, and it is defined by the standard library as follows:
 */

enum Option<T> {
    None, // No value
    Some(T), // Some value T
}

/* The Option<T> enum is so useful that it's even included in the prelude; you don't need to bring
 * it into scope explicitly. Its variants are also included in the prelude: you can use Some and
 * None directly without the Option:: prefix. The Option<T> enum is still just a regular enum, and
 * Some(T) and None are still variants of type Option<T>.
 *
 * When we have Some value, we know that a value is present and the value is held withint the Some.
 * When we have a None value, in some sense, it means the same thing as null: we don't have a valid
 * value. So why is having Option<T> any better than having null?
 *
 * In short, because Option<T> and T (where T can be any type) are different types, the compiler
 * won't let us use an Option<T> value if it were definetly a valid value. For example, this code
 * won't compile becaue it's trying to add an i8 to an Option<i8>:
 *
 let x: i8 = 5;
 let y: Option<i8> = Some(5);
 
 let sum = x + y;
 *
 * If we run this code, we get an error message like this: 
 *
 * cargo run
 *   Compiling option v0.1.0 (file:///projects/option)
 * error[E0277]: cannot add 'Option<i8>' to 'i8'
 * --> src/main.rs:9:13
 * |
 * 9 | let sum = x + y;
 * |             ^ no implementation for 'i8 + Option<i8>'
 * |
 * = help: the trait 'std::ops::Add<Option<i8>>' is not implemented for 'i8'
 * = help: the following other types implement trait 'Add<Rhs>':
 *           <&'a f32 as Add<f32>>
 *           <&'a f64 as Add<f64>>
 *           <&'a i128 as Add<i128>>
 *           <&'a i16 as Add<i16>>
 *           <&'a i32 as Add<i32>>
 *           <&'a i64 as Add<i64>>
 *           <&'a i8 as Add<i8>>
 *           <&'a isize as Add<isize>>
 *  and 48 others
 *
 * For more information about this error, try 'rustc --explain E0277'.
 * error: could not compile 'enums' due to previous error
 *
 *
 * Intense! In effect, this error message means that Rust doesn't understand how to add an i8 and
 * an Option<i8>, because they're different types. When we have a value of a type like i8 in Rust,
 * the compiler will ensure that we always have a valid value. We can proceed confidently without
 * having to check for null before using that value. Only when we have an Option<i8> (or whatever
 * type of value we're working with) do we have to worry about possibly not having a value, and the
 * compiler will make sure we handle that case before using the value. 
 *
 * In other words, you have to convert an Option<T> to a T before you can perform T operations with
 * it. Generally, this helps catch one of the most common issues with null: assuming that something
 * isn't null when it actually is.
 *
 * Eliminating the risk of incorrectly assuming a not-null value helps you to be more confident in
 * your code. In order to have a value that can possibly be null, you must explicitly opt in by
 * making the type of that value Option<T>. Then, when you use that value, you are required to
 * explicitly handle the case when the value is null. Everywhere that a value has a type that isn't
 * an Option<T>, you can safely assume that the value isn't null. This was a deliberate design
 * decision for Rust to limit null's pervasiveness and increase the safety of Rust code.
 *
 * So, how do you get the T value out of a Some variant when you have a value of type Option<T> so
 * you can use that value? The Option <T> enum has a large number of methods that are useful in a
 * variety of situations; you can check them out in its documentation. Becoming familiar with the
 * methods on Option<T> will be extremly useful in your journey with Rust.
 *
 * In general, in order to use an Option<T> value, you want to have code that will handle each
 * variant. You want some code that will run only when you have Some(T) value, and this coode is
 * allowed to use the inner T. You want some other code to run if you have a None value, and that
 * code doesn't have a T value available. The match expression is a control flow construct that
* does just this when used with enums: it will run different code depending on which variant of the
* enumt it has, and that code can use the data inside the matching value.*/

 */
