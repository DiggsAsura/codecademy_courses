/* Unpacking options and defaults
 * ===============================
 *
 * There is more than one way to unpack an Option and fall back on a default if it is None. To
 * choose the one that meets our needs, we need to consider the following:
 *
 *  - do we need eager or lazy evaluation?
 *  - do we need to keep the original empty value intact, or modify it in place?
 *
 *
 * or() is chainable, evaluates eagerly, keeps empty value intact
 * ----------------------------------------------------------------
 *
 * or() is chainable and eagerly evaluates its argument, as is shown in the following example. Note
 * that because or's arguments are evaluated eagerly, the variable passed to or is moved. */

#[derive(Debug)]
enum Fruit { Apple, Orange, Banana, Kiwi, Lemon }

fn main() {
    let apple = Some(Fruit::Apple);
    let orange = Some(Fruit::Orange);
    let no_fruit: Option<Fruit> = None;

    let first_available_fruit = no_fruit.or(orange).or(apple);
    println!("first_available_fruit: {:?}", first_available_fruit);
    // first_available_fruit: Some(Orange)
    //
    // 'or' moves its argument.
    // In the example above, 'or(orange)' returned a 'Some', so 'or(apple)' was not invoked.
    // But the variable named 'apple' has been moved regardless, and cannot be used anymore.
    //println!("Variable apple was moved, so this line won't compile: {:?}", apple);
    // TODO: uncomment the line above to see the compiler error

    // Part 2
    ex2();

    // Part 3
    ex3();

    // Part 4
    ex4();
}


/* or_else() is chainable, evaluates lazily, keeps empty value intact.
 * ---------------------------------------------------------------------
 *
 * Another alternative is to use or_else, which is also chainable, and evaluates lazily, as is
 * shown in the following example: */
fn ex2() {
    let apple = Some(Fruit::Apple);
    let no_fruit: Option<Fruit> = None;
    let get_kiwi_as_fallback = || {
        println!("Providing kiwi as fallback");
        Some(Fruit::Kiwi)
    };
    let get_lemon_as_fallback = || {
        println!("Providing lemon as fallback");
        Some(Fruit::Lemon)
    };

    let first_available_fruit = no_fruit
        .or_else(get_kiwi_as_fallback)
        .or_else(get_lemon_as_fallback);
    println!("first_available_gruit: {:?}", first_available_fruit);
    // Providing kiwi as fallback
    // first_available_gruit: Some(Kiwi)
}


/* get_or_insert() evaluates eagerly, modifies empty value in place
 * ------------------------------------------------------------------
 *
 * To make sure an Option contains a value, we can use get_or_insert to modify it in place with a
 * fallback value, as is shown in the following example. Note that get_or_insert eagerly evaluaes
 * its paramter, so variable apple is moved: */

fn ex3() {
    let mut my_fruit: Option<Fruit> = None;
    let apple = Fruit::Apple;
    let first_available_fruit = my_fruit.get_or_insert(apple);
    println!("my_fruit is: {:?}", first_available_fruit);
    println!("first_available_fruit is: {:?}", first_available_fruit);
    // my_fruit is Apple
    // first_available_fruit is: Apple
    //println!("Variable named 'apple' is moved: {:?}", apple);
    // TODO: uncomment the line above to see the compiler error
}


/* get_or_insert_with() evaluates lazily, modifies emtpy value in place
 * ---------------------------------------------------------------------
 *
 * Instead of explicitly providing a value to fall back on, we can pass a closure to
 * get_or_insert_with, as follows: */

fn ex4() {
    let mut my_fruit: Option<Fruit> = None;
    let get_lemon_as_fallback = || {
        println!("Providing lemon as fallback");
        Fruit::Lemon
    };
    let first_available_fruit = my_fruit
        .get_or_insert_with(get_lemon_as_fallback);
    println!("my_fruit is: {:?}", first_available_fruit);
    println!("first_available_fruit is: {:?}", first_available_fruit);
    // Providing lemon as fallback
    // my_fruit is: Lemon
    // first_available_fruit is: Lemon
    
    // If the Option has a value, it is left unchanged, and the closure is not invoked
    let mut my_apple = Some(Fruit::Apple);
    let should_be_apple = my_apple.get_or_insert_with(get_lemon_as_fallback);
    println!("should_be_apple is: {:?}", should_be_apple);
    println!("my_apple is unchanged: {:?}", my_apple);
    // The output is as follows. Note that the closure 'get_lemon_as_fallback' is not invoked
    // should_be_apple is: Apple
    // my_apple is unchaged: Some(Apple)
}
