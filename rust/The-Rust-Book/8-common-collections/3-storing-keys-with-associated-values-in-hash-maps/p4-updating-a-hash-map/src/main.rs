// Updating a Hash Map
// ===================
//
// Although the number of key and value pairs is growable, each unique key can
// only have one value associated with it at a time (but not vica versa: for
// example, both the Blue team and the Yellow team could have value 10 stored in the
// scores hash map).
//
// When you want to change the data in a hash map, you have to decide how to handle
// the case when a key already has a value assigned. You could replace the old value
// with a new value, completly disregarding the old value. You could keep the old value
// and ignore the new value, only adding the new value if the key doesn't already have a
// value. Or you could combine the old value and the new value. Let's look at how to do
// each of these!
//
//
// Overwriting a Value
// -------------------
//
// If we insert a key and value into a hash map and then insert that same key with
// a different value, the value associated with that key will be replaced. Even though
// the code in Listing 8-23 calls insert twice, the hash map will only contaie one
// key/value pair because we're inserting the value for the Blue team's key both times.
use std::collections::HashMap;

fn main() {
    let mut scores = HashMap::new();

    scores.insert(String::from("Blue"), 10);
    scores.insert(String::from("Blue"), 25);

    println!("{:?}", scores);

    ex2();
    ex3();
}
// 8-23: Replacing a value stored with a particular key

// This code will print {"Blue": 25}. The original value of 10 has been overwritten.



// Adding a Key and Value Only if a key Isn't Present
// ---------------------------------------------------
//
// It's common to check wheter a particular key already exists in the hash map with
// a value then take the following actions: if the key does exist in the hash map,
// the existing value should remain the way it is. If the key doesn't exist, insert it
// and a value for it.
//
// Hash maps have a special API for this called entry that takes the key you want to check
// as a parameter. The return value of the entry method is an enum called Entry
// that represents a value that might or might not exist. Let's say we want to check wheter
// the key for the Yellow team has a value associated with it. If it doesn't, wa want to
// insert the value 50, and the same for the Blue team. Using the entry API, our code
// looks like listing 8-24:

fn ex2() {
    let mut scores = HashMap::new();
    scores.insert(String::from("Blue"), 10);

    scores.entry(String::from("Yellow")).or_insert(50);
    scores.entry(String::from("Blue")).or_insert(50);

    for (key, value) in &scores {
        println!("{}: {}", key, value);
    }

    println!("{:?}", scores);
}
// 8-24: Using the entry method to only insert if the key does not already have
// a value.

// The or_insert method on Entry is defined to return a mutable reference to the value for
// the corresponding Entry key if that key exists, and if not, inserts the parameter as
// the new value for this key and returns a mutable reference to the new value. This
// technique is much cleaner than writing the logic ourself and, in addition, plays
// more nicely with the borrow checker.
//
// Running the code in Listing 8-24 will print {"Yellow": 50, "Blue": 10}. The first
// call to entry will insert the key for the Yellow team with value 50 because the
// Yellow team doesnt't have a value already. The second call to entry will not
// change the hash map because the Blue team already has the value 10.



// Updating a Value based on the Old Value
// ---------------------------------------
//
// Another commont use case for hash maps is to look up a key's value and then
// update it based on the old value. For instance, Listing 8-25 shows code that counts
// how many times each word appears in some text. We use a hash map with the words as
// keys and increment the value to keep track of how many times we've seen that word. If
// it's the first time we've seen a word, we'll first insert the value 0.
fn ex3() {
    let text = "hello world wonderful world";

    let mut map = HashMap::new();

    for word in text.split_whitespace() {
        let count = map.entry(word).or_insert(0);
        *count += 1;  // dereference, need to learn more
    }

    println!("{:?}", map);
}
// 8-25: Counting occurences of words using hash map that stores words and counts

// This code will print {"world": 2, "hello": 1, "wonderful": 1}. You might see the
// same key/value pairs printed in a different order: recall from the "Accessing
// Values in a Hash Map" section that iterating over a hash map happens in an
// arbitrary order.
//
// The split_whitespace method returns an iterator over sub-slices, separated by
// whitespaces, of the value in text. The or_insert method returns a mutable reference
// (&mut V) to the value for the specified key. Here we store that mutable reference in
// the count using the asterisk (*). The mutable reference goes out of scope at the
// end of the for loop, so all of these changes are safe and allowed by the
// borrowing rules.
