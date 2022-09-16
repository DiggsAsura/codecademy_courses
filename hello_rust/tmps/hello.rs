fn main() {
    let first_name: &str = "Kenneth";
    let last_name: &str = "Bæver Bjerke";
    let current_year: u16 = 2022;
    let age: u16 = current_year - 1984;

    println!("Hello {} {}!", first_name, last_name);
    println!("I hear you are {} years old.", age);
}
