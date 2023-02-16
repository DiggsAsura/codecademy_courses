/* From and Into
 * ==============
 *
 * The From and Into traits are inherently linked, and this is actually part of its implementation.
 * If you are able to convert A from type B, then it should be easy to beleive that we should be
 * able to convert B to type A. 
 *
 * 
 * From 
 * -----
 *
 * The From trait allows for a type to define how to create itself from another type, hence
 * providing a very simple mechanism for converting between several types. There are numerous
 * implementtations of this trait within the standard library for confersion of primitive and
 * common types. 
 *
 * For example we can easily convert a str into a String */

fn main() {
    let my_str = "Hello";
    let my_string = String::from(my_str);

    /* We can do similar for defining a conversion for our own type. */

    use std::convert::From;

    #[derive(Debug)]
    struct Number {
        value: i32,
    }

    impl From<i32> for Number {
        fn from(item: i32) -> Self {
            Number { value: item }
        }
    }

    let num = Number::from(30);
    println!("My number is {:?}", num);

    /* Into
     * -----
     *
     * The Into trait is simply the reciprocal of the From trait. That is, if you have implemented
     * the From trait for your type, Into will call it when necessary. 
     *
     * Using the Into trait will typically require specification of the type to convert into as the
     * compiler is unable to determine this most of the time. However this is a small trade-off
     * considering we get the functionality for free. */

    // use std::convert::From;

    #[derive(Debug)]
    struct Number2 {
        value: i32,
    }

    impl From<i32> for Number2 {
        fn from(item: i32) -> Self {
            Number2 { value: item }
        }
    }

    let int = 5;
    // Try removing the type declaration
    let num: Number2 = int.into();
    println!("My number is {:?}", num);
}

/* I'm not sure this makes too much sense atm but maybe it's not totally needed? Or feels like not
 * super important at this point. */

