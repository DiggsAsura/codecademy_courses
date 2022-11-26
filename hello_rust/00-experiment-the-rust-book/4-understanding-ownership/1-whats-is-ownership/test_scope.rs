fn main() {
    let x: Vec<i32> = vec![1, 2, 3];

    drop(x);

    println!("{x:?}");
}
