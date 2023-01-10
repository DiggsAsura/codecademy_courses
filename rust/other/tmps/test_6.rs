fn main() {
    let a = 123;
    {
        println!("{a}");
    }
    let b = a;
    println!("{b}");
}
