// Using Box<T> Like a Reference
// =============================
//
// We can rewrite the code in Listing 15-6 to use a Box<T> instead of a reference; the dereference
// operator used on the Box<T> in Listing 15-7 functions in the same way as the dereference
// operator used on the reference in Listing 15-6:

fn main() {
    let x = 5;
    let y = Box::new(x); // can't use &x here because

    assert_eq!(5, x);
    assert_eq!(5, *y);
}

// 15-7: Using the dereference operator on a Box<i32> to get the value 5

// The main difference between Listing 15-7 and Listing 15-6 is that here we set y to be an
// instance of a Box<T> pointing to a copied value of x rather than a reference pointing to the
// value of x. In the last assertion, we can use the dereference operator to follow the pointer of
// the Box<T> in the same way that we did when y was a reference. Next, we'll explore twhat is
// special about Box<T> that enables us to use the dereference operator by defining our own type.
