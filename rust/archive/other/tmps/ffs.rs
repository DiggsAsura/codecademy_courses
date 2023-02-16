fn main() {
    let n = 10;
    let mut i = 0;
    while i < n {
        let sum = second(i, n);
        i += 1;
        println!("{i}: {sum}");
    }
}

fn second(a: i32, b: i32) -> i32 {
    return a + b
}
