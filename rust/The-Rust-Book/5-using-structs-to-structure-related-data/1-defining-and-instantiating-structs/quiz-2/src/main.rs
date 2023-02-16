/* Quiz 2 */

struct Point {
    x: i32,
    y: i32,
}

fn main() {
    let mut p = Point { x: 1, y: 2 };
    let x = &mut p.x;
    let y = &mut p.y;
    *x += 1;            // not really sure how dereference works here, but apparently adding
    *y += 1;            // same as above
    println!("{} {}", p.x, p.y);

}
