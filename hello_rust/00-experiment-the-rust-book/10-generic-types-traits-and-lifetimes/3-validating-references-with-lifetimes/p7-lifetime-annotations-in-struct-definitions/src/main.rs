// Lifetime Annotations in Struct Definitions
// ==================================================
//
// So far, the structs we've defined all hold owned types. We can define structs to hold
// references, but in that case we would need to add a lifetime annotation on every reference in
// the struct's definition. Listing 10-24 has a struct named ImportantExcerpt that holds a string
// slice.

struct ImportantExcerpt<'a> {
    part: &'a str,
}

fn main() {
    let novel = String::from("Call me Ishmael. Some years ago...");
    let first_sentence = novel.split('.')
        .next()
        .expect("Could not find a '.'");
    let i = ImportantExcerpt {
        part: first_sentence,
    };
}

// 10-24: A struct that holds a reference, requireing a lifetime annotation

// This struct has the single field part that holds a string slice, which is a reference. As with
// generic data types, we declare the name of the generic lifetime parameter inside angle brackets
// after the name of the struct so we can use the lifetime parameter in the body of the struct
// definition. This annotation means an instance of ImportantExcert can't outlive the reference it
// holds in its part field.
//
// The main function here creates an insteance of the ImportantExcerpt struct that holds a
// reference to the first sentence of the String owned by the variable novel. The data in novel
// exists before the ImportantExcerpt instance is created. In addition, novel doesn't go out of
// scope until after the ImportantExcerpt goes out of scope, so the reference in the
// ImportantExcerpt instance is valid.
