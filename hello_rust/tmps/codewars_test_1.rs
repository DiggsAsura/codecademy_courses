fn main() {
    let sum = thingy(6);

    println!("{:?}", sum);
}

fn thingy(num: i32) -> i32 {
    let n_num = [3, 5, 6, 9, 10, 12, 15];
    let mut n_sum = 0;

    for n in n_num {
        if num > n {
            n_sum += n;
        } else {
            break;
        }
    }

    return n_sum;
}


#[test]
fn returns_expected() {
    assert_eq!(thingy(10), 23);
    assert_eq!(thingy(11), 33);
    assert_eq!(thingy(6), 8);
}
