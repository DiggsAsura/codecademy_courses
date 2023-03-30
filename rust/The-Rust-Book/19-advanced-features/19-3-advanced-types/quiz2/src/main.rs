fn is_equal<T: Eq + ?Sized>(t1: &T, t2: &T) -> bool {
    t1 == t2
}

fn main() {
    println!("{:?}", is_equal("Hello", "world"));
}

// I have a hunch this will compile.
//
// Well initially it did not compile because I had to add + ?Sized to the trait bound. After that
// it compiled.
