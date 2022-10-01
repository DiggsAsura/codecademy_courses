// A reference is a way of pointing to a particular piece of data within memory.
// By referencing existing data, we can re-use that data without needing to 
// allocate additional memory.
//
// Since Rust forces us to manage memory manually, references are found 
// everywhere and can help make it very performant. 

// &
// ---
// Every time we declare a value with let, we are creating data that is stored
// in memory. We can then create a reference to that data by prefixing our 
// expressions with the & prefix. 


// In this example, funny_number is a reference to pi: 
fn main() {
    println!("{:?}", example_7());
    println!("{:?}", example_5()); 
    println!("{:?}", example_4());
    println!("{:?}", example_3());
    println!("{:?}", example_2());
    println!("{:?}", example_1());
}

fn example_1() {
    let pi = 3.1415;
    let funny_number = &pi;

    println!("{funny_number}");

    let lightspeed = 299792458;

    let fast = &lightspeed;
    let still_fast = &&lightspeed; // notice the double &&

    let speed_of_light = &still_fast; // This is equivalent to &&&lightspeed

    println!("The speed of light: {speed_of_light}");
}

// We can also create references to references!



// DEREFERENCE
// -------------

// When we need to access the underlying data of a reference points to directly,
// we can dereference the * prefix:

fn example_2() {
    let mut year = 3020;
    let y = &mut year;

    *y + 10; // Is this a good example? Does not make much sense to me. 

    println!("The year is year {year}.");
}

// Automatic Dereferencing
// ------------------------
//
// The Rust compiler will automatically dereference whenever possible, 
// specifically when the . operator is used. Here we do not have to worry about
// manually dereferencing earth because the call to_uppercase() will accomplish
// this for us:

fn example_3() {
    let planet = "Earth";
    let earth = &&&&planet;

    assert_eq!("EARTH", earth.to_uppercase());
    println!("{earth}"); // My test. Not sure whats going on here. lol.    
}

// ref
// ----
//
// Sometimes we need a reference to the inner values of a complex data 
// structure. 
//
// When accessing an inner value by reference, we may need to utilize the ref
// keyword which permits this functionallity:

fn example_4() {
    let starship: Option<String> = Some("Omaha".to_string());

    match starship {
        Some(ref name) => println!("{}", name),
        None => {}
    }

    // Without the use of the 'ref' keyword above, this next line would not
    // compile:
    println!("{:?}", starship);
}

// We can also use ref with mutable data with ref mut: 

fn example_5() {
    let mut planet: Option<String> = Some("Waleco 8".to_string());

    match planet {
        Some(ref mut name) => {
            name.push('8');
        }
        None => {}
    }
}

// ref technically accomplishes the same thing as & but is placed on the other
// side of the assignment. In this way, they can be thought of as reciprocals
// of each other. 

fn example_6() {
    let val = "reciprocal";

    let ref r1 = val;
    let r2 = &val;

    assert_eq!(r1, r2);
}

// For quickly accessing inner values with a method, such as when attempting to
// use an &Option<T> as an Option<&T>, check out the as_ref() method. 
//
// lol yea as that gonna happen anytime soon. Not sure what that means.


// SLICES
//
// A reference to a range of elements from a collection is called a slice. To 
// take a slice we use index expressions on a referenced collection:

fn example_7() {
    let s = String::from("hello world");

    let hello = &s[0..5];
    let world = &s[6..11];
    println!("{hello} {world}");
}
