// Consider the following program:

fn main() {
    let x: &[(i32, i32)] = &[(0, 1)]; // x is a pattern of type &[(i32, i32)] and is bound to the
                                      // value &[(0, 1)] which is the expression &[(0, 1)]
}
// Which of the following are refutable patterns for x?
//
//
// The correct answer is:
//
// &[(x, y)]
// &[(x, y), ..]
//
// Conetxt:
// A slice does not have a fixed length, so any pattern which asserts that x must have a least one
// element is refutable.
