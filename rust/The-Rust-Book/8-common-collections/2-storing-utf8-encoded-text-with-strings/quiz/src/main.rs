/* What is the maximum number of times a heap allocation could occur in this program? */
fn main() {
    let s1 = String::from("tic");
    let s2 = String::from("tac");
    let s3 = String::from("toe");
    let s = s1 + "-" + &s2 + "-" + &s3;

    // s1, s2 and s3 is 3 heap allocations
    // s is 1 heap allocation
    // the + operator is another allocations
    // so 7 in total
}
