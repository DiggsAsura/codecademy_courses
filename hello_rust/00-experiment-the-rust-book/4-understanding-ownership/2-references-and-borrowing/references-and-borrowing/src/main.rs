// References and Borrowing
//
// The issue with the tuple code in Listing 4-5 is what we have to return the String to the calling
// function so we can still use String after the call to calculate_length, because the String was
// moved into calcualte_length. Instead, we can provide a reference to the String value. A
// reference is like a pointer in that it@s an address we can follow to access the data stored at
// that address; that data is owned by some other variable. Unlike pointer, a reference is
// guaranteed to point to a valid value of a particular type for the life of that reference.

fn main() {
    let s1 = String::from("hello");

    let len = calculate_length(&s1);   // soo, passing in a reference to s1 &s1

    println!("The length of '{}' is {}.", s1, len);
}

fn calculate_length(s: &String) -> usize { // and here, its a reference to the TYPE, not the
    // variable. 
    s.len()
}

// First, notice all the tuple code in the variable declaration and the function return value is
// gone. Second, note that we pass &s1 into calculate_length and, in its definition, we take
// &String rather than String. These ampersands represent -referenecs-, and they allow you to refer
// to some value without taking ownership of it. Figure 4-5 depicts this concept: 

//      s               s1
// name | value     name | value        index | value
// ptr  | ---------> ptr |    --------->   0  | h
//                   len | 5               1  | e
//                   cap | 5               2  | l
//                                         3  | l 
//                                         4  | o 

// Note: The opposite of referencing using & is dereferencing, which is accomplished with the
// dereference operator, *. We'll see some uses of the dereference operator in Chapter 8 and
// discuss details of dereferencing in Chapter 15.

// Lets look at the function call here: 
//
//      let s1 = String::from("hello");
//      let len = calculate_length(&s1);
//      
// The &s1 syntax let us create a reference that -refers- to the value of s1 but does not own it.
// Because it does not own it, the value it point to will not be dropped when the reference stops
// being used.
// 
// Likewise, the signature of the function uses & to indicate that the type of the parameter s is a
// reference. Let's add some explanatory annotations:
//
//      fn calculate_length(s: &String) -> usize { // s is a reference to a String 
//          s.len()
//      } // here, s goes out of scope. But because it does not have ownership of what it refers
//      to, it is not dropped.
// 
// The scope in which the variable s is valid is the same as any function parameter's scope, but
// the value pointed to by the reference is not droped when s stops being used because s doesn't
// have ownership. When functions have references as parameters instead of the actual values, we
// won't need to return the values in order to give back ownership, because we never had ownership.
//
// We call the action of creating a reference -borrowing-. As in real life, if a person owns
// something, you can borrow it from them. When you're done, you have to give it back. You don't
// own it. 
//
// So what happens if we try to modify something we're borrowing? Try the code in Listing 4-6.
// Spoiler alert, it doesn't work! 

/*
fn ex2() {
    let s = String::from("hello");
    change(&);

    fn change(some_string: &String) {
        some_string.push_str(", world");
    }
}
*/
