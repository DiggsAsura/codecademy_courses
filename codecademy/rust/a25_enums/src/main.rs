fn main() {
    ex1();
}

/* 
 * Enums
 * ======
 *
 * When we need a data type whose value can be only one of a set number of variants, Rust provides
 * us with "Enumerations". 
 *
 *
 * Enum Declaration
 * ------------------
 *
 * To create an enumeration, often just called an enum, we utilize the enum keyword. Every variant
 * for our enum is placed within its declaration block. Variants follow the "PascalCase" naming
 * convention. */

#[derive(Debug)]
enum InnerPlanet {
    Mercury,
    Venus,
    Earth,
    Mars,
}

/* Now that we have declared our enum, we can create a value of a specific variant using the ::
 * operator. */

fn ex1() {
    let home = InnerPlanet::Earth;

    println!("{home:?}");

/* Matching
 * ----------
 *
 * Since an enum's value can only be a single variant, matching on an enum is a very common and
 * useful programming pattern in Rust. */

    let vacation_location = InnerPlanet::Mercury;

    match vacation_location {
        InnerPlanet::Mercury => println!("Bring sun protection."),
        InnerPlanet::Venus => println!("Quite blue."),
        InnerPlanet::Earth => println!("Lots to see here."),
        InnerPlanet::Mars => {
            println!("Brrr.....");
            println!("Bring a coat!");
        }
    }

/* When matching on an enum, all variants must be handled. If we remove one of the match arms in
 * the previous example, our code will not compile.
 *
 * We can use the _ catch-all operator to handle the remaining unspecified variants though: */

    match home {
        InnerPlanet::Earth => println!("Lots to see here."),
        _ => println!("Lets clean up Earth first...."),
    }



/* Variant values
 * ---------------
 *
 * Enum variants can also contain values. This is possible because enum variants in Rust are
 * actually structs. */

    enum Meal {
        Pasta,                  // Unit struct
        StirFry(Vec<String>),   // Tuple struc 
        Burrito {               // Struct with named fields
            beans: bool,
            rice: bool,
        },
    }

/* We can access a variant's inner data by destructuring */

    let dinner = Meal::Burrito {
        beans: true,
        rice: false,
    };

    match dinner {
        Meal::Pasta => println!("Too heavy."),
        Meal::StirFry(veggies) => {
            println!("{veggies:?}")
        }
        Meal::Burrito { beans, rice } => {
            println!("with beans: {beans}");
            println!("with rice: {rice}")
        }
    }


/* impl Blocks
 * -------------
 * Like structs, enums are our own custom data type. We can provide methods for our enums through
 * an impl block. */

    enum Determination {
        Yes,
        No,
        Potentially,
    }

    impl Determination {
        pub fn totally() -> Self {
            Self::Yes
        }
    }
}


