#![allow(dead_code)]
#![allow(unused_variables)]

fn main() {
    ex1();
    ex2();
}

/* Generics
 * ==========
 *
 * Rust is a strongly typed language, so we must provide single type signatures for data structures
 * and fucntion parameters. This helps the compiler figure out how to manage its memory safely, but
 * can be limiting from a programmer's point of view.
 *
 * This is why Rust provides Generic Types, which are type declarations that can work across
 * multiple types. 
 *
 *
 * When to use Generics
 * ----------------------
 *
 * Imagine we are working with the velocity of an object. We know that our velocity might be
 * measured in either integer or floating point numbers and can build separate data structures to
 * account for this. 
 */

fn ex1() {
    struct VelocityInt(u32);
    struct VelocityFloat(f64);

/* However, this would mean a lot of duplicated code to account for distinct type signatures in
 * every data structure and function we use. 
 *
 * Generics help us to avoid this code repetition. Here we have combined the above datatypes into a
 * single datatype using the generic type, T. 
 */

    struct Velocity<T>(T);

    let velocity_int = Velocity(5);         // Velocity<u32>
    let velocity_float = Velocity(2.8);     // Velocity<f64>
}

/* You should note that if you have previously used types such as Option<T> and Vec<T>, you have
 * already been making use of generics.
 *
 *
 * Declaring Generics
 * --------------------
 *
 * We can utilize generics as fields on custom data types and as function parameters.
 *
 * Since generics are situational, any item utilizing generics must provide a signature declaring
 * the generic types it uses. We annotate generics the same as lifetimes. 
 * The signature is declared within the angle brackets (<>) following the item we are annotating.
 *
 * Generic types are conventionally named with single uppercase letters such as T.
 */

fn ex2() {
    // Here the 'Wrapper' struct utilizes a single generic type 'T'
    struct Wrapper<T> {
        data: T,
    }

    // If we have multiple generic types, we separate them with commas.
    enum Present<T, U> {
        Food(T),
        Card(U),
    }

    // In functions, generics are declared after the name, and before the parameters.
    fn wrap_data<T>(data: T) -> Wrapper<T> {
        Wrapper {
            data
        }
    }

    /* NOTE: I really don't understand much of what I'm doing now. */

    /* When declaring generics on impl blocks, the generic type is made available to the entire
     * block. This means we forego declaring generics on contained methods. */

    impl<T> Wrapper<T> {
        fn get_data(self) -> T {
            self.data
        }
    }

    /* Trait Bounds
     * --------------
     *
     * So far we have been able to create generic types and do simple things like pass generic
     * values through functions. But if we try to print out generic type with println!(), our code
     * will not compile.
     *
     * This is because the println!() macro requires that the data it prints implements the Display
     * trait. Not every type implements Display, so we must tell the compiler that we reuire our
     * generic type to implement this trait. 
     *
     * Trait requirements on generic types are called Trait Bounds. Rust provides us multiple ways
     * of declaring trait bounds and they each have their unique syntax.
     *
     * The standard approach is to define trait bounds after our generic declaration with a :
     * followed by the required trait.
     */

//    use std::fmt::Display;
    use std::fmt::{Display, Debug};

    // This function will only accespt types which implement 'Display'
    fn sound<T: Display>(noise: T) {
        println!("{noise}");
    }

    /* We can require multiple constraints on the same generic type with the + operator. */

//    use std::fmt::{Display, Debug};

    // This function will only accept types which implement 'Display' AND 'Debug'
    fn debug_sound<T: Display + Debug>(noise: T) {
        println!("normal: {noise}");
        println!("debug: {noise:?}");
    }
}
    /* impl Trait
     * ============
     *
     * Rust provides us a shorthand syntax of impl Trait for function parameters and return values.
     * This allows us to utilize generics without having to manually declare them. 
     *
     * Since this is only shorthand, the following code will actually expand to the same example
     * above.
     */

fn ex3() {
    use std::fmt::{Display, Debug};
    fn sound(noise: impl Display) {
        println!("{noise}");
    }

    fn debug_sound(noise: impl Display + Debug) {
        println!("Normal: {noise}");
        println!("Debug: {noise:?}");
    }
}


/* where 
 * =======
 *
 * When applying many constraints to generics, our signature can become unwieldly fairly quick. To
 * keep our code readable, Rust provides us the where keyword which allows us to declare our
 * constrainst after our function signature.
 *
 * The following are equivalent.
 */

fn ex4() {
    use::std::fmt::{Display, Debug};
    fn mimic_sound<T: Display + Clone, U: Debug + Copy>(noise: T, room: U) -> T {
        println!("{noise} in the {room:?}");
        noise.clone()
    }

    fn mimic_where<T, U>(noise: T, room: U) -> T 
        where 
            T: Display + Clone,
            U: Debug + Copy,
            {
                println!("{noise} in the {room:?}");
                noise.clone()
            }
}

// Ok I have no idea what I'm doing.
// Great.


/* Turbofish Generics
 * ===================
 *
 * When defining generics of a data structure, we place the type annotation before the function
 * call. */
fn ex5() {
    let vec_of_bytes = Vec::<u8>::new();

    // When defining generics of a function parameter, we place the type annotation after the
    // function name and before '()'
    // This is commonly utilized with the 'parse' methods.
    let str_to_integer = "-91".parse::<i32>();
}
