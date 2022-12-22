// Reading Elements of Vectors
//
// There are two ways to reference a value stored in a vector: via indexing or using the
// get method. In the following example, we've annotated the types of the values
// that are returned from these functions for extra clairity.
//
// Listing 8-4 shows both methods of accessing a value in a vector, with indexing
// syntax and the get method.

fn main() {
    let v = vec![1, 2, 3, 4, 5];

    let third: &i32 = &v[2];    // we borrow the value at index 2. this won't consume the value
    let fourth: i32 = v[3];     // why borrow when this does the same? because we don't need to
                                // borrow the value at index 3. we can just take ownership of it.
                                // this is a move. we can't use v[3] after this line.

    println!("The third element is {third}");
    println!("The fourth element is {fourth}");
    println!("{:?}", v);
    println!("{fourth}");
    println!("{}", v[3]);
    // Ok i'm confused by the borrow and move stuff. Why can I use the v[3] again?

    let third: Option<&i32> = v.get(2); // this returns an Option<&i32> because it's possible
                                        // that the index we're trying to access is out of bounds.
                                        // if we try to access an element that doesn't exist,
                                        // we'll get a None value instead of a panic!
    match third {
        Some(third) => println!("The third element is {}", third),
        None => println!("There is no third element."),
    }
}

// The get method returns an Option<&T>, which is an enum that can be either Some or None.
// This makes sense to me now. Is it that easy to call Option? :D

// 8-4: Using indexing syntax or the get method to access an item in a vector.

// Note a few details here. We use the index ov value 2 to get the third element because
// vectors are indexed by number, starting at zero. Using & and [] gives us a reference
// to the index value. When we use the get method with the index passed as an argument,
// we get an Option<&T> that we can use with match.
//
// The reason Rust provides these two ways to reference an element is so you can choose how the
// program behaves when you try to use an index value outside the range of exissitng
// elements. As an example, let's see what happens when we have a vector of five elements and
// then we try to access an element at index 100 with each technique.
//
// let v = vec![1, 2, 3, 4, 5];
// let does_not_exist = &v[100]; // this will panic!
// let does_not_exist = v.get(100); // this will return None
//
// 8-5: Attempting to access the element at index 100 in a vector containing five elements.

// When we run this code, the first [] method will cause the program to panic because
// it references a nonexistent element. This method is best used when you want your
// program to crash if there's an attempt to access an element past the end of the vector.
//
// When the get method is passed an index that is outside the vector, it returns None
// without panicking. You would use this method if accessing an element beyont the range of
// the vector may happen occasionally under normal circumstances. Your code will then have
// logic to handle having either Some(&element) or None, as discussed in Chapter 6.
// For example, the index could be coming from a person entering a number. If they accidentally
// enter a numer that's too large and the program gets a None value, you could tell the
// user how many items are in the current vector and give them another chance to enter
// a valid value. That would be more user-friendly than crashing the program due to
// a type!
//
// When the program has a valid reference, the borrow checker enforces the ownership and
// borrowing rules (covered in Chapter 4) to ensure this reference and any other references
// to the contents fo the vector remain valid. Recall the rule that states you can't have
// mutable and immutable references in the same scope. That rule applies in Listing 8-6,
// where we hold an immutable reference to the first element in a vector and try to add
// an element to the end. This program won't work if we also try to refer to that
// element in a vector and try to add an element to the end. This program won't work if we
// also try to refer to that element later in the function

fn ex2() {
    let mut v = vec![1, 2, 3, 4, 5];
    let first = &v[0];  // immutable reference/borrow.
    v.push(6);
    println!("The first element is {}", first);
}
// 8-6: Attempting to add an element to a vactor while holding a reference to an item.

// The code in 8-6 might look like it should work: why should a reference to the first
// element care about changes at the end of the vector? This error is due to the way vectors
// work: because vectors put the values next to teach other in memory, adding a new element
// onto the end of the vector might require allocating new memory and copying the old elements
// to the new space, if there isn't enough room to put all the elements next to each
// other where the vector is currently stored. In that case, the reference to the first
// element would be pointing to deallocated memory. The borrowing rules prevent
// programs from ending up in that situation.
//
// Note: For more information on implementation details of the Vec<T> type, see
// "The Rustonomicon". https://rust-book.cs.brown.edu/nomicon/vec/vec.html
