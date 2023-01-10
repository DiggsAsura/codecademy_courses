// Quiz 2
// Reverse the elemnts of a vector in-place

fn main() {
    let mut my_vec: Vec<String> = vec!["Hello".to_string(), "World".to_string()];
    println!("Original vector: {:?}", my_vec);
    let reversed = reverse(&mut my_vec);
    //let reversed = reverse(&my_vec);
    println!("Reversed vector: {:?}", reversed);
}

/*
fn reverse(v: &mut Vec<String>) {
    let n = v.len();
    for i in 0 .. n / 2 {
        std::mem::swap(&mut v[i], &mut v[n - i - 1]);
    }
}
*/

/*
fn reverse(v: &Vec<String>) -> Vec<String> {
    let n = v.len();
    let mut v2 = Vec::new();
    for _ in 0..n {
        v2.push(v.pop().unwrap());
    }
    v2
}
*/

/* Nope - double mutable borrows
fn reverse(v: &mut Vec<String>) {
    let n = v.len();
    let mut v2 = v.clone();
    for i in 0..n / 2 {
        std::mem::swap(&mut v2[i], &mut v2[n - i - 1]);
    }
}
*/

/* Works! However, thought it would fail because of double muts but nope, worked.
fn reverse(v: &mut Vec<String>) -> Vec<String> {
    let n = v.len();
    for i in 0..n/2 {
        let p1 = &mut v[i] as *mut String;
        let p2 = &mut v[n - i - 1] as *mut String;
        unsafe { std::ptr::swap_nonoverlapping(p1, p2, 1); }
    }
    v.clone()
}
*/

fn reverse(v: &mut Vec<String>) -> Vec<String> {
    let n = v.len();
    for i in 0..n/2 {
        let s1 = v[i].clone();
        let s2 = v[n - i - 1].clone();
        v[i] = s2;
        v[n - i - 1] = s1;
    }
    v.clone()
}
