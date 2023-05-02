struct Things {
    thing1: u8,
    thing2: u8,
    thing3: u8,
}

fn main() {
    let dathing = Things {
        thing1: 29,
        thing2: 30,
        thing3: 30,
    };

    println!("thing1: {}", dathing.thing1);
    println!("thing2: {}", dathing.thing2);
    println!("thing3: {}", dathing.thing3);
}
