fn main() {
    let mut v = vec![(1, 2), (3, 4)].into_iter();
    let mut sum = 0;

    while let Some(t) = v.next() {
        let (_, n) = t;
        println!("{}", n);
        sum += n;
    }
    println!("{}", sum);
}

// Context:
//
// This example provides a valid use of while let matching and let matching. Note that you could
// combine them, e.g.
//
// while let Some((_, n)) = v.next() {
//      /* ... */
// }
//
