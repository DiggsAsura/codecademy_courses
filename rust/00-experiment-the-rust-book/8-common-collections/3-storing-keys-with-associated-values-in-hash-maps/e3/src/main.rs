// Challenge:
//
// Using a hash map and vectors, create a text interface to allow a user to
// add employee names to a department in a company. For exampe, "Add Sally to
// Engineering" or "Add Amir to Sales". Then let the user retrieve a list of
// all people in a department or all people in the company by department, sorted
// alphabetically.

use std::collections::HashMap;

fn main() {
    let mut company = HashMap::new();
    let mut input = String::new();
    std::io::stdin().read_line(&mut input).unwrap();


    loop {
        println!("Enter a command: ");
        let mut parts = input.split_whitespace();
        let command = parts.next().unwrap();
        let name = parts.next().unwrap();
        let department = parts.next().unwrap();

        if command == "Add" {
            company.entry(department).or_insert(Vec::new()).push(name);
        } else if command == "List" {
            if let Some(names) = company.get(department) {
                for name in names {
                    println!("{} works in {}", name, department);
                }
            }
        }
    }
}
