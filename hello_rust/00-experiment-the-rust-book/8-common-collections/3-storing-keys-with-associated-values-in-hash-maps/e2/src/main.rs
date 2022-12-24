// Convert strings to pig latin challenge

const VOW: [char; 5] = ['a', 'e', 'i', 'o', 'u'];
const CON: [char; 21] = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'];

fn main() {
    let word = String::from("first");
    // check first letter of the word
    let first_letter = word.chars().nth(0).unwrap();
    for c in first_letter.to_string().chars() {
        if VOW.contains(&c) {
            let answer = vowel(&word);
            println!("{answer}");
        } else if CON.contains(&c) {
            let answer = consonants(&word);
            println!("{answer}");
        } else {
            println!("Not a valid word");
        }
    }
}

fn vowel(word: &String) -> String {
    let mut pig_latin = String::new();
    pig_latin.push_str(&word);
    pig_latin.push_str("-hay");
    pig_latin
}

fn consonants(word: &String) -> String {
    let mut pig_latin = String::new();
    pig_latin.push_str(&word[1..]);
    pig_latin.push_str("-");
    pig_latin.push_str(&word[0..1]);
    pig_latin.push_str("ay");
    pig_latin
}
