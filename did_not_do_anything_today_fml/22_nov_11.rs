struct Person {
    name: &'static str,
}

impl Person {
    fn excuse(&self) {
        println!("Oh yea had school all day today. November 11 2022.");
        println!("Br, {}", self.name);
    }
}

fn main() {
    let kenneth = Person { name: "Kenneth" };

    kenneth.excuse();
}

