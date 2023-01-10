// solved the quiz with lifetime bounds (thanks chatgpt) and it works.
fn shortest<'a, 'b>(x: &'a str, y: &'b str) -> &'a str where 'b: 'a {
    if x.len() < y.len() {
        x
    } else {
        y
    }
}

fn main() {
    println!("{}", shortest("hello", "rust"));
}
