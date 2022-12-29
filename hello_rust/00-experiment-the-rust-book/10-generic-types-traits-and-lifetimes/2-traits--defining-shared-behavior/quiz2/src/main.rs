use std::fmt::Display;
fn displayable<T: Display>(t: T) -> impl Display  {
    t
}

fn main() {
    let mut s = String::from("hello");
    let mut s2 = displayable(s);
//    s2.push_str(" world");
    println!("{}", s2);
}
// This does not compile because the method push_str is not available on the type impl Display
