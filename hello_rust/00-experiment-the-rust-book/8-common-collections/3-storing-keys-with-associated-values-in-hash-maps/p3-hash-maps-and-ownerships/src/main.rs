// Hash Maps and Ownership
// =======================
//
// For types that implement the Copy trait, like i32, the values are copied into the
// hash map. For owned values like String, the values will be moved and the hash map
// will be the owner of those values.
use std::collections::HashMap;

fn main() {
    let field_name = String::from("Favorite color");
    let field_value = String::from("Blue");

    let mut map = HashMap::new();
    map.insert(field_name, field_value);
    // field_name and field_value are invalid at this point, try using them and
    // see what compiler error you get!
    //println!("{field_name}");

    for (key, value) in &map {
        println!("{}: {}", key, value);
    }

    ex2();
}
// Listing 8-22: Showing that keys and values are owned by the hash map once they're
// inserted

// We aren't able to use the variables field_name and field_value after they've
// been moved into the hash map with the call to insert.
//
// If we insert references to values into the hash map, the values won't be moved
// into the hash map. The values that the references point to must be valid for at least
// as long as the hash map is valid.
//
// We'll talk more about these issues in the "Validating References with Lifetimes"
// section in Chapter 10.

fn ex2() {
    let field = String::from("Favorite game");
    let game =  String::from("Tetris");

    let mut map = HashMap::new();
    map.insert(&field, &game);

    for (key, value) in &map {
        println!("{}: {}", key, value);
    }

    println!("field: {}", field);
    println!("game: {}", game);
}
