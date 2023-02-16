// Lifetime Annotation Syntax
// ==========================
//
// Lifetime annotations don't change how long any of the references live. Rather, they describe the
// relationships of the lifetimes of multiple references to each other without affecting the
// lifetimes. Just as functions can accept any type when the signature specifies a generic type
// parameter, functions can accept references with any lifetime by specifying a generic lifetime
// parameter.
//
// Lifetime annotations have a slighly unusla syntax: the names of lifetime parameters must start
// with an apostrophe (') and are usually all lowercase and very short, like generic types. Most
// people use the name 'a for the first lifetime annotation. We place lifetime parameter
// annotations after the & of a reference, using a space to separate the annotation from the
// reference's type.
//
// Here are some example: a reference to an i32 without a lifetime parameter, a reference to an i32
// that has a lifetime parameter named 'a, and a mutable reference to an i32 that also has the
// lifetime 'a.

// &i32        // a reference
// &'a i32     // a reference with an explicit lifetime
// &'a mut i32 // a mutable reference with an explicit lifetime

// One lifetime annotation by itself doesn't have much meaning, because the annotations are meant
// to tell Rust how generic lifetime parameters of multiple references relate to each other. Let's
// examine how the lifetime annotations relate to each other in the context of the longest
// function.

fn main() {
    let num: &i32 = &10;
    let num2: &i32 = &20;

    let x = nums(num, num2);
    println!("The longest number is {}", x);

}

fn nums<'a>(a: &'a i32, b: &'a i32) -> &'a i32 {
    if a > b {
        a
    } else {
        b
    }
}
