fn expect_none(x: Option<i32>) -> ! {
    match x {
        Some(n) => panic!("Expected None, found Some({n})"),
        None => (),
    }
}

fn main() {
    println!("{:?}", expect_none(None));
}


// I was unsure, if this actually would work - but it does.
//

// Edit: it DOES NOT compile. I did miss the -> ! in the function signature. This function needs to
// return something, but it can never return anything. So it needs to be marked as diverging.
