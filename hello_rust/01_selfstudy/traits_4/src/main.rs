struct Guest {
    name: String,
    email: String,
}

trait Rsvp {
    fn coming(&self) -> bool;
}

impl Rsvp for Guest {
    fn coming(&self) -> bool {
        true
    }
}

fn main() {
    println!("OK, just spamming with some basic trait stuff to try get it under my skin");
    
    let guest_1 = Guest {
        name: String::from("Sarah"),
        email: String::from("test@test.com"),
    };

    println!("{} is coming: {}", guest_1.name, guest_1.coming());
}
