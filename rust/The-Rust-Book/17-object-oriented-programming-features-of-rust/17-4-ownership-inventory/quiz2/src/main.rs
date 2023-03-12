// Adds the string 's' to all elements of
// the input iterator

fn concat_all(iter: impl Iterator<Item = String>, s: &str) -> impl Iterator<Item = String> {
    iter.map(move [s2| s2 + s)
}

fn main() {
}


fn alts() {
    // alt 1
    let v = vec![String::from("Rust")];
    concat_all(v.into_iter(), "Yes").collect::<Vec<_>>();


    // alt 2
    let v2 = vec![String::from("Rust")];
    let it = {
        let s = String::from("Yes");
        concat_all(v2.into_iter(), &s)
    };
    it.collect::<Vec<_>>();


    // alt 3: none of these programs


    // alt 4
    let v4 = vec![String::from("Rust")];
    let s4 = String::from("Yes");
    concat_all(v4.into_iter(), &s4);
    println!("{}", s);
}


