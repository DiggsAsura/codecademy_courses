fn main() {
    let test = nested_fn();
    let mut count = 0;

    while count < test {
        for i in 0..test {
            println!("{i}: This is strange");
        }
        count += 1;
        println!("Count is now:  {count}");
    }
    println!("{:?}", test);
}

fn nested_fn() -> i32 {
    5
}
