fn main() {
    let my_vec = vec!["Diggs", "AurosouldSeiza", "jurandy969"];

    for name in my_vec.iter() {
        match name {
            &"Diggs" => println!("hello {name}"),
            &"AurosouldSeiza" => println!("hello {name}"),
            &"jurandy969" => println!("hello {name}"),
            _ => println!("hello {name}"),
        }
    }
}

// Point is, when matching with a string/str, need to use &str, not just str. 
