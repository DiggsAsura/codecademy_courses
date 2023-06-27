fn add_x_perm(param: &mut String) {
    param.push_str("X\n");
    println!("{}", param);
}


fn main() {
    let mut word = String::from("Hello");
    add_x_perm(&mut word);
    println!("{}", word);
}




