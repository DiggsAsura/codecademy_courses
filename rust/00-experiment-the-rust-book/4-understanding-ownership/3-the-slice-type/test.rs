fn main() {
    let word = String::from("hello");

    let bytes = word.as_bytes();

//    println!("{bytes:?}");

    for (i, &item) in bytes.iter().enumerate() {
        //println!("{i} {item}");
        let word2 = &word[0..i];
        println!("{item} {word2}");
    }
}
