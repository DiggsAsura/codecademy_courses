fn main() {
    ex2();
}

/* 
 * Structs
 * =========
 *
 * A struct is a way of grouping related data of differing types, much like a tuple. The main
 * differences is that a struct allows us to provide names for each field. 
 *
 * 
 * Struct Declaration
 * -------------------
 *
 * To declare a struct, we utilize the struct keyword. Fields are then provided within its
 * declaration block. 
 *
 * Field names follow 'snake_case' naming convention and must be type annotated. Here we have
 * provided three fields for our Guest struct: name, rsvp, and costume. */

#[derive(Default)]
struct Guest {
    name: &'static str,
    rsvp: bool,
    costume: bool,
}

/* 
 * Instantiating
 * ---------------
 *
 * When we instantiate a struct, we must provide values for every field. If a field is missing, our
 * code will not compile. */

fn ex1() {
    let guest = Guest {
        name: "Anand",
        rsvp: true,
        costume: false,
    };
}

/* When instantiating a struct's fields from variables, we can use a shorthand syntax if the
 * varialb ename is the same as the field. */

fn ex2() {
    let name = "Anand";
    let rsvp = true;
    let costume = false;

    let guest = Guest {
        name,
        rsvp,
        costume,
    };



/* 
 * Accessing Fields
 * ------------------
 *
 * To access the values of a field, we can use dot notation with the desired field name. Here we
 * are accessing the rsvp and name fields on our previously defined variable, guest. */

    if guest.rsvp {
        println!("Our first guest is {}", guest.name);
    }


/* The major benefit of using field names is the clairity they provide to our codebase. If we had
 * made our Guest struct a tuple, we would need to access the guest's rsvp status with guest.1.
 * This would require us to look at the declaration of our tuple to know what field 1 represents.
 *
 *
 * Multiple fields
 * -----------------
 *
 * We can populate the fields of a struct from a previously declared variable of the same type. We
 * can use ..var as the last field declaration in our struct to accomplish this. */

    let guest1 = Guest {
        name: "Kim",
        rsvp: true,
        costume: true,
    };

    let guest2 = Guest {
        name: "Jamal",
        ..guest1
    };

    println!("{} == {}", guest1.rsvp, guest2.rsvp);


/* We can also use a function to populate the remaining fields as long as the function resolves to
 * the same type for each remaining field.
 *
 * This is commonly found on structs that implement the Default trait. Using ..Default::default()
 * as the last field will populate the remaining fields with their default value. */
 
    // Assuming we have deried 'Default' for our 'Guest' struct
    let guest3 = Guest {
        name: "Selena",
        ..Default::default()
    };



/* 
 * Matching
 * -----------
 *
 * We can match on a struct the same as any other datatype. */

    match guest1 {
        Guest { name: "Selena", rsvp: true, costume: true } => println!("Selena is wearing a costume to the party!"),
        Guest { name: "Selena", rsvp: true, costume: false } => println!("Selena is not dressing up for the party."),
        _ => {}
    }

/* When matching on a struct, we generally only want to match against a small subset of all
 * available fields. We can choose to ignore the valuse of a specific field by utilizing _ as it's
 * value. */

    match guest1 {
        Guest { name: "Jamal", rsvp: true, costume: _ } => println!("Jamal is coming to the party!"),
        _ => {}
    }

/* We can ignore all remaining fields with the .. operator. */

    match guest1 {
        Guest { rsvp: true, .. } => println!("{} is coming to the party!", guest1.name),
        _ => {}
    }

/* 
 * impl Blocks
 * -------------
 *
 * Structs are powerful tools in Rust because when we create a struct, we are defining our own
 * custom data type. Declaring a type allows us make an impl block to create specialized functions
 * which are specific to that struct. 
 *
 * Functions declared within an impl block are called methods. Methods can utilize the special
 * input parameter self to operate directly on the type being implemented. mut self and &mut self
 * are also available for accessing the type mutabaly. */

    impl Guest {
        pub fn print_name(&self) {
            println!("{}", self.name);
        }
        pub fn wearing_costume(&mut self) {
            self.costume = true;
        }
    }

    // we can call methods with the "dot notation"
    guest1.print_name();
    guest2.print_name();
    guest3.print_name();

    // We can also supply the implemented type as a parameter
    Guest::print_name(&guest1);
}

