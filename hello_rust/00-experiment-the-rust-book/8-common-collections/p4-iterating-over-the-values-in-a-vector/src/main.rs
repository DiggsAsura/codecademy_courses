// Iterating over the Values in a Vector
//
// To access each element in a vector in turn, we would iterate through all of the
// elements rather than use indices to access one at the time. Listing 8-7 shows how to use
// a for loop to get immutable references to each element in a vector of i32 values
// and print them.

fn main() {
    let v = vec![100, 32, 57];
    for n_href in &v {
        let n_plus_one: i32 = *n_href + 1; // whats the difference between n_href and *n_href?
                                           // n_href is a reference to the value in the vector
                                           // *n_href is the value in the vector
        println!("{}", n_plus_one);
    }
}
// 8-7: Accessing each element in a vector by iterating over the elements using a for loop.

// To read the number that n_ref refers to, we have to use the * dereference operator to get
// the value in n_ref before we can add 1 to it. We'll talk more about the dereference operator
// in the "Following the Pointer to the Value with the Dereference Operator" section of
// Chapter 15.
//
// We can also iterate over mutable references to each element in a mutable vector in order
// to make changes to all the elements. The for loop in Listing 8-8 will add 50 to each
// element. Because we have a mutable reference to each element, these changes are
// actually made to the vector.
fn ex2() {
    let mut v = vec![100, 32, 57];
    for n_ref in &mut v {
        // n_ref has type &mut i32
        *n_ref += 50;
    }
}
// 8-8: Iterating over mutable references to elements in a vector.

//  To change the value that the mutable reference refers to, we again use the * dereference
//  operator to get the value in n_ref before we can use the += operator.
//
//  Iterating over a vector, wheter immutably or mutably, is safe because of the borrow
//  checker's rules. If we attempted to insert or remove itmes in the for loop bodies in
//  listing 8-7 and 8-8, we would get a compiler error similar to the one we got with the
//  code in Listing 8-6. The reference to the vector that the for loop holds prevents
//  simulataneous modifications of the whole vector.
