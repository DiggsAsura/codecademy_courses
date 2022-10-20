fn main() {
    ex1();
    ex2();
    println!("{:?}", ex3());
    ex4();
}

/* 
 * Tuples
 * =======
 *
 * When we need to group together data of differing types, we cannot use an array or Vec as they
 * are homogenous collections. To create compound types with differing contained types, we can
 * utilize the tuple primitive. 
 *
 *  
 *  Tuple Declaration
 *  -------------------
 *
 *  We can declare a tuple by placing our data within paranthesis, ().
 */

fn ex1() {
    // Here we have a tuple of type (char, i32, str).
    let awesome = ('q', 38, "this is great");

    /* We can access the fields of a tuple by tacking on a . and then providing the respective
     * field's index. This is referred to as dot notation.
     *
     * Like most programming languages, Rust uses 0-based indexing, which means that our first
     * field is accessed with .0.
     */

    let cat = ("Meowzer", 10, true);

    let name = cat.0;  // "Meowzer"
    let age = cat.1; 
    let awake = cat.2;

    println! { "
    {cat:?}
    {age}
    {awake}
    {name}
    "};
}



/*
 * Destructuring
 * ---------------
 *
 * We can destructure a tuple anywhere the Rust syntax allows it. 
 */

fn ex2() {
    // This function will return our tuple.
    fn get_cat() -> (&'static str, f64, bool) {
        ("Meowzer", 2.8, true)
    }

    // Destructuring within the variable assignment.
    let (name, cuteness, is_sleeping) = get_cat();
    println!("This is our cat {name}.");

    // We can ignore unused fields with '_'
    let (name, _, _) = get_cat();
    println!("This is our cat {name}.");

    // Destructuring within a match expression:
    match get_cat() {
        (name, _, is_sleeping) => {
            if is_sleeping {
                println!("{name} is sleeping.");
            } else {
                println!("{name} is awake");
            }
        }

        // We can ignore a range of fields with '..'
        (name, ..) => {
            println!("{name} is cute when asleep or awake.");
        }
    }
}


/* 
 * Tuple Struct
 * -------------
 *
 * If we want to re-use a tuple across our codebase, we can define it as it's own custom type. This
 * is referred to as a Named Tuple or a Tuple Struct.
 *
 * To declare a Tuple Struct we utilize the struct keyword. Here we have named our tuple struct
 * Cat.
 */

// Tuple struct declarations must end with a ';'
#[derive(Debug)]
pub struct Cat(&'static str, f64, bool);

fn ex3() -> Cat {
    Cat("Meowzer", 2.8, true)
}

/* The advantage of naming our tuple is that we can then create methods specific to this type
 * utilizing an impl block. 
 */


/* () Unit Type
 * -----------
 *
 * A tuple that does not contain any fields, (), is its own primitive type in Rust called the unit
 * type. We can think of the unit type as a piece of data, but without any actual data. It's only
 * value is its own existence. 
 *
 * This type helps provide a safe way to handle certain situations while avoiding the pitfalls of a
 * "null" type. 
 */

fn ex4() {
    let this_variable_exists = ();

    /* A function which does not return a value actually returns () */

    fn empty_function() {
        // A function without a return signature...
    }

    println!("{:?}", empty_function());

    fn empty_expanded() -> () {
        // ... actually expands to this.
        // Both syntaxes are valid.
        ()
    }

    println!("{:?}", empty_expanded());
}

/* 
 * Unit Structs
 * --------------
 *
 * We can also give names to our custom unit types. These are called "Unit Strcuts" and are useful
 * when working with traits.
 */

// We do not need to append '()' as it is inferred. 
pub struct NoValue;
