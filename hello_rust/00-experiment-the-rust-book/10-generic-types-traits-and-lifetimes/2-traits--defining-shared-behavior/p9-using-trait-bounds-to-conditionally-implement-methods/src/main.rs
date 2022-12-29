// Using Trait Bounds to Conditionally Implement MethodsG
// ======================================================
//
// By using a trait bound with an impl block that uses generic type parameters, we can implement
// methods conditionally for types that implement the specified traits. For example, the type
// Pair<T> in Listing 10-15 always implements the new function to return a new instance of Pair<T>
// (recall from "Defining Methods" section of chapter 5 that Self is a type alias for the type of
// the impl block, which in this case is Pair<T>). But in the next impl block, Pair<T> only
// implements the cmp_display method if its inner type T implements the PartialOrd trait that
// enables comparison and the Display trait that enables printing.

mod listing_10_15 {
    use std::fmt::Display;

    pub struct Pair<T> {
        x: T,
        y: T,
    }

    impl<T> Pair<T> {
        pub fn new(x: T, y: T) -> Self {
            Self { x, y }
        }
    }

    impl<T: Display + PartialOrd> Pair<T> {
        pub fn cmp_display(&self) {
            if self.x >= self.y {
                println!("The largest member is x = {}", self.x);
            } else {
                println!("The largest member is y = {}", self.y);
            }
        }
    }
}

fn main() {
    use listing_10_15::Pair;

    let pair_of_chars = Pair::new('a', 'b');
    pair_of_chars.cmp_display();

    let pair_of_nums = Pair::new(1, 2);
    pair_of_nums.cmp_display();

}

// 10-15: Conditionally implementing methods on a generic type depending on trai bounds

// We can also conditionally implement a trait for any type that implements another trait.
// Implementations of a trait on any type that satisfies the trait bounds are called blanket
// implementations and are extensively used in the Rust standard library. For example, the standard
// library implements the ToString trait on any type that implements the Display trait. The impl
// block in the standard library looks similar to this code:

// impl<T: Display> ToString for T { // snip }

// Because the standard library has this blanket implementation, we can call the to_string method
// defined by the ToString trait on any type that implements the Display trait. For example, we can
// turn integers into their corresponding String values like this because integers implement
// Display:

// let s = 3.to_string();

// Blanket implementations apprea in the documentation for the trait in the "Implementators"
// section.
//
// Traits and trait bounds let us write code that uses generic type parameters to reduce
// duplication but also specify to the compiler that we want the generic type to have particular
// behavior. The compiler can then use the trait bound information to check that all the concrete
// types used with our code provide the correct behavior. In dynamically typed languages, we would
// get an error at runtime fir we called a method on a type which didn't define the method. But
// Rust moves these errors to compile time so we're forced to fix the problems before our code is
// even able to run. Additionally, we don't have to write code that checks for behavior at runtime
// because we've already checked at compile time. Doing so improves performance without having to
// give up the flexibility of generics.
