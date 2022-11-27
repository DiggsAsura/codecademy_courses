/* The Compiler Is Not Perfect
 * ----------------------------
 *
 * A common issue in statically-typed languages is that the compiler can reject programs which
 * would execute without a problem. For example, take this program: */

fn main() {
    /*
    {
        let x = if true { 1 } else { "hello" };
        assert_eq!(x + 1, 2);
    }
    */

/* If this program were allowed to execute, x would always b 1, and so computing x + 1 would always
 * work without issue. That's because the if condition is true. But the compiler ignores the actual
 * value of the condition, and assumes either branch -could- be executed. Therefore this program is
 * rejected because x cannot be both a number and a string.
 *
 * Similarly, the compiler may reject programs that seem acceptable under the rules of ownership.
 * For example, like this program: */

    fn move_two(s1: String, s2: String) -> String {
        s1
    }

    let (s1, s2) = (String::from("a"), String::from("b"));
    let s3 = move_two(s1, s2);
    println!("{} {}", s2, s3);
}

/* Even though s2 is never used or returned in move_two, the compiler still considers s2 to be
 * moved when calling move_two.
 *
 * So as you're learning about ownership and Rust, keep in mind that the compiler's safety checks
 * often assume the worst case about your code. Part of learning to write Rust is convincing the
 * compiler that the worst case is still safe!
 */

