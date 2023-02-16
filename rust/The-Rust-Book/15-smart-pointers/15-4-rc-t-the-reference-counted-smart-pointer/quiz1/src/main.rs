// Determine whether the program will pass the compiler. If it passes, write the expected output of
// the program if it were executed.

use std::rc::Rc;
fn main() {
    let n = Rc::new(1);
    let mut n2 = Rc::clone(&n);
    *n2 += 1;
    println!("{}", n2);
}

// First thought:
// I don't think it will compile. I think it will error becuase Rc is not really a number - or is
// it?
//
// Second thought:
// Hmm wait. I kinda mix with Rc::strong_count(&n). Maybe it in fact will compile and print 2?
//
// Nope. Won't compile, it required DerefMut - which we didn't learn about yet.
