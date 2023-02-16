fn main() {
    ex1();
    ex2();
    ex3();
}

/* Traits
 * =======
 *
 * Rust allows us to define shared behavior between different types using traits. A trait defines
 * all methods that a type must implement to be considered a member of that trait. 
 *
 *
 * Defining shared behavior
 * -------------------------
 *
 * Let's imagine we want to be able to define specific behavior in our program for things that
 * harmonize. We determine thta to be able to harmonize, a thing must be able to both make a sound
 * and listen. 
 *
 * We can create a trait to define this behavior utilizing the trait keyword followed by its name.
 * All required methods are then placed within its declaration block.
 */

fn ex1() {
    trait Harmonize {
        // If we omit the body of a method, it must be manually defined when implemented.
        fn sound(&self) -> String;

        // If we provide a body for a method, it serves as a default that can be overwritten
        fn listen(&mut self) {
            std::thread::sleep_ms(4000);
        }
    }

    /* Now any type which implements Harmonize trait will be guaranteed a sound() method that
     * returns a &str, and a listen() method that will potentially sleep a thread for 4 mins and 33
     * seconds. 
     */
}

/* Implementing Traits
 * ---------------------
 *
 * We can implement a trait for a type using the syntax impl Trait for Type {}. Type signatures for
 * trait methods must match the trait's definition.
 */

fn ex2() {
    trait Harmonize {
        fn sound(&self) -> String;
        fn listen(&mut self) {
            std::thread::sleep_ms(4000);
        }
    }

    struct Human(String);

    impl Harmonize for Human {
        fn sound(&self) -> String {
            self.0.clone()
        }
        // We do not need to implement 'listen' as the default implementation is sufficient.
    }

    let mut alto = Human("oOoOo".to_string());
    alto.listen();

    let tenor = Human("oooooo".to_string());
    println!("{}", tenor.sound());



/* Traits are most useful when applied to multiple types, so let's implement our Harmonize trait on
 * a new Passerine struct. Here we will override the default for the listen() method.
 */


    struct Passerine {
        freq: Vec<u64>,
    }

    impl Harmonize for Passerine {
        fn sound(&self) -> String {
            format!("{:?}", self.freq)
        }
        fn listen(&mut self) {
            self.freq.push(432);
            std::thread::sleep_ms(303);
        }
    }

    let mut bird = Passerine {
        freq: vec![28, 37, 108, 92],
    };

    bird.listen();
    println!("{}", bird.sound());


/* Trait methods are always public, so use of the pub keyword is not allowed.
 *
 * We cannot implement a trait from an external crate on a type from an external crate. To
 * accomplish this we must make an intermediary type to connect them. 
 */


/* Generics
 * ----------
 *
 * Since traits are just method requirements that must be satisfied, we can use traits with
 * generics to create meaningful type signatures.
 *
 * Human and Passerine are different types, but we can now write use generics to be able to use
 * both interchangeably.
 */
    fn sing(creature: impl Harmonize) {
        creature.sound();
    }
}

/* Deriving Traits
 * ----------------
 *
 * Rust provides us with a way to implement certain types without having to manually declare an
 * impl block. This is called "deriving" a trait and is accomplished by placing the
 * #[derive(Trait)] attribute before our data structure */

fn ex3() {
    #[derive(Debug)]
    struct Passerine {
        freq: Vec<u64>,
    }

    let bird = Passerine {
        freq: vec![827, 23, 12, 189],
    };
    // Now it is possible to print a debug out for our 'Passerine' type.
    println!("{bird:?}");
}

/* Scope
 * -------
 *
 * Sometimes when attempting to call a trait method, we will enounter an error stating that the
 * method is not available. This is because in order to utilize the methods of a trait, that trait
 * must be in scope. When this happens, we need to import the trait into the necessary scope with
 * use path::to::Trait;
 */

