// Specifying Placeholder Types in Trait Definitions with Associated Types
// =======================================================================
//
// Associated types connect a types connect a type placeholder with a trait such that the trait
// method definitions can use these placeholder types in their signatures. The implementor of a
// trait will specify the concrete type to be used instead of the placeholder type for the
// particular implementation. That way, we can define a trait that uses some types without needing
// to know exacty what those types are until the trait is implemented.
//
// We've described most of the advanced features in this chapter as being rarely needed. Associated
// types are somewhere in the middle: they're used more rarely than features explained in the rest
// of the book but more commonly than many of the other features discussed in this chapter.
//
// One example of a trait with an associated type is the Iterator trait that the standard library
// provides. The associated types is named Item and stands in for the type of the values the type
// implementing the Iterator trait is iterating over. The definition fot he Iterator trait as shown
// in Listing 19-12:

pub trait Iterator {
    type Item;

    fn next(&mut self) -> Option<Self::Item>;
}

// Listing 19-12: The definition of the Iterator trait that has an associated type Item

// The type Item is a placeholder, and the next method's definition shows that it will return
// values of type Option<Self::Item>. Implementors of the Iterator trait will specify the concrete
// type for Item, and the next method will return an Option containing a value of that concrete
// type.
//
// Associated types might seem like a similar concept to generics, in that the latter allow us to
// define a function without specifying what types it can handle. To examine the difference between
// the two concepts, we'll look at an implementation of the Iterator trait on a type named Counter
// that Specifies the Item type is u32

struct Counter {
    count: u32,
}

impl Counter {
    fn new() -> Counter {
        Counter { count: 0 }
    }
}

impl Iterator for Counter {
    type Item = u32;

    fn next(&mut self) -> Option<Self::Item> {
        // --snip--
        if self.count < 5 {
            self.count += 1;
            Some(self.count)
        } else {
            None
        }
    }
}

// This syntax seems comparable to that of generics. So why not just define the Iterator trait with
// generics, as shown in Listing 19-13?
/*
pub trait Iterator2 {
    fn next(&mut self) -> Option<T>;
}
*/
// Listgin 19-13: A hypotethical definition of the Iterator trait using generics.


// The difference is that when using generics, as in Listgin 19-13, we must annotate the types in
// each implementation; because we can also implement Iterator<String> for Counter or any other
// type, we could have multiple implementations of Iterator for Counter. In other words, when a
// trait has a generic parameter, it can be implemented for a type multiple times, changing the
// concrete types of the generic type parameters each time. When we use the next method on Counter,
// we would have to provide type annotations to indicate which implementation of Iterator we want
// to use.
//
// With associated types, we don't need to annotate types because we can't implement a trait on a
// type multiple times. In Listing 19-12 with the definition that uses associated types, we can
// only choose what the type of Item will be once, because there can only be one impl Iterator for
// Counter. We don't have to specify that we want an iterator of u32 values everywhere that we call
// next on Counter.
//
// Assocaited types also become part of the trait's contract: implementors of the trait must
// provide a type to stand in for the associated type placeholder. Associated types often have a
// name that describes how the type will be used, and documenting the associated type in the API
// documentation is good.


fn main() {}
