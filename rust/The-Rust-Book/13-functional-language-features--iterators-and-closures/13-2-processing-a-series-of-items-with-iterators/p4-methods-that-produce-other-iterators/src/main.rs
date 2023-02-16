// Methods that Produce Other Iterators
// ====================================
//
// Iterator adaptors are methods defined on the Iterator trait that don't consume the iterator.
// Instead, they produce different iterators by changing some aspect of the original iterator.
//
// Listing 13-14 shows an example of calling the iterator adaptor method map, which takes a closure
// to call each item as the items are iterated through. The map method returns a new iterator that
// produces the modified items. The closure here creates a new iterator in which each item from the
// vector will be incremented by 1:

fn ex1() {
    let v1: Vec<i32> = vec![1, 2, 3];
    v1.iter().map(|x| x + 1);
}
// 13-14: Calling the iterator adaptor map to create a new iterator

// However, this code produces a warning.

// The code in Listing 13-14 doesn't do anything; the closure we've specified never gets called.
// The warning reminds us why: iterator adaptors are lazy, and we need to consume the iterator
// here.
//
// To fix this warning and consume the iterator, we'll use the collect method, which we used in
// Chapter 12 with env::args in Listing 12-1. This method consumes the iterator and collects the
// resulting values into a collection data type.
//
// In Listing 13-15, we collect the result of iterating over the iterator that's returned from the
// call to mep into a vector. This vector will end up containing each item from the original vector
// incremented by 1.

fn ex2() {
    let v1: Vec<i32> = vec![1, 2, 3];
    let v2: Vec<_> = v1.iter().map(|x| x + 1).collect();

    assert_eq!(v2, vec![2, 3, 4]);
    println!("v2: {:?}", v2);
}
// 13-15: Calling the map method to create a new iterator and then calling the collect method to
// soncume the new iterator and create a vector

// Because map takes a closure, we can specify any operation we wan to perform on each item. This
// is a great example of how closures let you customize some behavior while reusing the iteration
// behavior that the Iterator trait provides.
//
// You can chain multiple calls to iterator adaptors to perform complex actions in a readable way.
// But because all iterators are lazy, you ahve to call one of the consuming adaptor methods to get
// reults from calls to iterator adaptors.

fn main() {
    ex1();
    ex2();
}
