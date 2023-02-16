/* Trying to wrap my head around mutability. From the chapter on this in the Rust by Example book,
 * it kinda gives me the hunch you can kinda hack your way around chaning a originally immutable
 * value. Gotta test a few things only. */



#[derive(Clone, Copy)]    // Important! the last println will fail without this! 
struct Person {
    name: &'static str,
}


fn main() {
    let kenny = Person {
        name: "Kenneth",
    };

    let mut ken = kenny;

    // Struggle a bit to come to my actual example. Lets try via a function
    fn change_name(ken: &mut Person) {
        ken.name = "Kayi";
        println!("new name: {}", ken.name);
    }

    //kenny.name = "Kayi";
    println!("{}", ken.name);
    change_name(&mut ken);

    println!("is kenny still available? {}", kenny.name);
}

/* Ok so this is very interesting. How to move ownership etc. 
 *
 * 1. made an immutable struct Person
 * 2. made an immutable instance "kenny"
 * 3. then made a mutable instance 'ken' of immutable instance kenny (which again is made from an
 *    immutable struct)
 * 4. renamed the 'name' field of the immutable Person struct via the mutable variable 'ken' (see
 *    the function change_name
 * 5. After this, could not call 'kenny' anymore, without adding #[derive(Clone, Copy)]
 *
 * Very interesting. Probably logic but yea, will take some time. */ 
