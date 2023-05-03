struct Car {
    brand: String,
    owner: String,
    model: String,
    year: u16,
    delivery: String,
}

fn main() {
    let kenneth = Car {
        brand: "Tesla".to_owned(),
        owner: "Kenneth".to_owned(),
        model: "Y Performance".to_owned(),
        year: 2023,
        delivery: "May 3 2023".to_owned(),
    };

    println!("Kenneth picking up a new {} today {}", kenneth.brand, kenneth.delivery);
    println!("It is the model {}, {}", kenneth.model, kenneth.year);
    println!("Going to be exciting!");
}
