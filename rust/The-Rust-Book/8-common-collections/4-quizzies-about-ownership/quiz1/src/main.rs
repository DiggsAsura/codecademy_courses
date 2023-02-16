fn main() {
    let x = remove_zeros(&mut vec![0, 1, 0, 3, 12]);
    println!("{:?}", x);
}

fn remove_zeros(v: &Vec<i32>) -> Vec<i32> {
    let mut new_vec = Vec::new();
    for (i, t) in v.iter().enumerate().rev() {
        if *t != 0 {
            new_vec.push(*t);
        }
    }
    new_vec
}

/*
fn remove_zeros(v: Vec<i32>) {
    for (i, t) in v.iter().enumerate().rev() {
        if *t == 0 {
            v.remove(i);
        }
    }
}
*/
