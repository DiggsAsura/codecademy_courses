fn expect_none(x: Option<i32>) {
    match x {
        Some(n) => panic!("Expected None, found Some({n})"),
        None => (),
    }
}

fn main() {
    println!("{:?}", expect_none(None));
}


// I was unsure, if this actually would work - but it does.
