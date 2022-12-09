/* Quiz 1
 *
 * Just writing the code after i took the quiz. Both quiz this times does compile, so could be
 * interesting to just write it for some muscle memory? I wish at least :P
 *
 */

struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let mut a = Point { x: 1, y: 2 };
    a.x += 1;
    let b = Point { y:1, ..a };
    a.x += 1;
    println!("{}", b.x);    // 2. Because last a.x += 1 wont be in b
}
