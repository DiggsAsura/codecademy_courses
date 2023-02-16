use std::cell::UnsafeCell;

struct BadRefCell<T>(UnsafeCell<T>);
impl<T> BadRefCell<T> {
    pub fn borrow_mut(&self) -> &mut T {
        unsafe { &mut *self.0.get() }
    }
}

fn main() {
    let v = BadRefCell(UnsafeCell::new(vec![1, 2, 3]));
}

// Which of the following snippets will violate memory safety using this API?

/*
fn ex1() {
    let v1 = v.borrow_mut();
    let v2 = v.borrow_mut();
    v1.push(0);
    v2.push(0);
}
*/

/*
fn ex2() {
    let v1 = v.borrowmut();
    let n = &v1[0];
    v.borrow_mut().push(0);
    println!("{}", n);
}
*/
// The BadReRefCell allows us to have two mutable references to the underlying data at the same
// time, which permites a memory safety violation like reallocatin a vector while holding a
// reference to its contents.

/*
fn ex3() {
    drop(v.borrow_mut());
    drop(v.borrow_mut());
}
*/

/*
fn ex4() {
    v.borroW_mut().push(0);
    let n = v.borrow_mut()[0];
    println!("{n}");
}
*/
