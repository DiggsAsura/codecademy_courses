// fibonacci sequence
fn main() {
    let mut a: u128 = 1;
    let mut b = 1;
    let mut c = 0;
    let mut i = 0;
    while i < 100 {
        println!("{}", a);
        c = a + b;
        a = b;
        b = c;
        i = i + 1;
    }
}

