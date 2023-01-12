// The Iterator Trait and the next Method
// ======================================
//
// All iterators implement a trait named Iterator that is defined in the standard library. The
// definition of the trait looks like this:

pub trait Iterator {
    type Item;

    fn next(&mut self) -> Option<Self::Item>;

    // methods with default implementations elided
}

// Notice this definition uses some new syntax: type Item and Self::Item, which are defining an
// associated type with this trait. We'll talk about associated types in depth in Chapter 19. For
// now, all you need to know is that this code says implementing the Iterator trait requires that
// you also define an Item type, and this Item type is used in the return type of the next method.
// In other words, the Item type will be the type returned from the iterator.
//
// The Iterator trait only requires implementors do define one method: the next method, which
// returns one item of the iterator at a time wrapped in Some and, when iteration is over, returns
// None.
//
// We call the next method on iterators directly; Listing 13-12 demonstrates what values are
// returned from repeated calls to next on the iterator created from the vector.

#[test]
fn iterator_demonstration() {
    let v1 = vec![1, 2, 3];

    let mut v1_iter = v1.iter();

    assert_eq!(v1_iter.next(), Some(&1));
    assert_eq!(v1_iter.next(), Some(&2));
    assert_eq!(v1_iter.next(), Some(&3));
    assert_eq!(v1_iter.next(), None);
}
// 13-2: Calling the next method on an iterator

// Note that we neede to make v1_iter mutable: calling the next method on an iterator changes internal
// state that the iterator uses to keep track of where it is in the sequence. In other words, this
// code consumes, or uses up, the iterator. Each call to next eats up an item from the iterator. We
// didnt't need to make v1_iter mutable when we used a for loop because the loop took ownership of
// v1_iter and made it mutable behind the scenes.
//
// Also note that the values we get from the calls to next are immutable references to the values
// in the vector. The iter method produces an iterator over immutable references. If we want to
// create an iterator that takes ownership of v1 and returns owned values, we can call into_iter
// instead of iter. Similarly, if we want to iterate over mutable references, we can call iter_mut
// instead of iter.

fn main() {
    println!("ex1():");
//    ex1();

}
