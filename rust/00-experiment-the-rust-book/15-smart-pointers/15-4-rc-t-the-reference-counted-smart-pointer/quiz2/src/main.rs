// Determine wheter the program will pass the compiler. If it passes, write the expected output of
// the program if it were executed.

use std::rc::Rc;

struct Example;
impl Drop for Example {
    fn drop(&mut self) {
        println!("Drop");
    }
}

fn main() {
    let x = Rc::new(Example);
    let y = Rc::clone(&x);
    println!("A");
    drop(x);
    println!("B");
    drop(y);
    println!("C");
}


// Yes i do beleive this will compile. I think this will be the output:
//
// A
// Drop
// B
// Drop
// C


// I was correct about compiling - however I am stupid for not catching the point at all. Rc<T>,
// the whole point is to have shared owners. SO, of course Drop won't show after A. It won't be
// dropped before both are dropped.
