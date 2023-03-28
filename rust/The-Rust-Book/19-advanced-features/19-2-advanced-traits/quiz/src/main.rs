// Question 3

mod inner {
    pub trait A {
        fn f(&self) -> usize { 0 }
    }
    pub trait B {
        fn f(&self) -> usize { 1 }
    }
    pub struct P;
    impl A for P {}
    impl B for P {}
}

fn main() {
    use inner::{P, B};
    println!("{}", P.f());
}

// I think it will compile actually, but very unsure what the output will be. Kinda think it will
// be 0, but I'm not sure.
//
// Doh - it was 1.
