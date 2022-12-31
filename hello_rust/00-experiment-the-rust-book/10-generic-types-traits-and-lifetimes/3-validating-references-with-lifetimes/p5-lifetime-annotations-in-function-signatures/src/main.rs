// Lifetime Annotations in Function Signatures
// ==================================================
//
// To use lifetime annotations in function signatures, we need to declare the generic lifetime
// parameter inside angle brackets between the function name and the parameter list, just as we did
// with generic type parameters.
//
// We want the signature to express the following contraint: the returned reference will be valid
// as long as both the parameters are valid. This is the relationship between lifetimes of the
// parameters and the return value. We'll name the lifetime 'a and then add it to each reference,
// as shown in Listing 10-21.

fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}
// 10-21: The longest function definition specifying that all the references in the signature must
// have the same lifetime 'a

// This code should compile and produce the result we want when we use it with the main function in
// Listing 10.19.
//
// The function signature now tells Rust that for some lifetime 'a, the function takes two
// paramters, both of which are string slices that live at least as long as lifetime 'a. The
// function signature also tells Rust that the string slice returned from the function will live at
// least as long as lifetime 'a. In practice, it means that the lifetime of the reference returned
// by the longest function is the same as the smaller of the lifetimes of the values referred to by
// the function arguments. These relationships are what we want Rust to use when analyzing this
// code.
//
// Remember, when we specify the lifetime parameters in this function signature, we're not changing
// the lifetimes of any values passed in or returned. Rather, we're specifying that the borrow
// checker should reject any values that don't adhere to these constraints. Note that the longest
// function doesn't need to know exactly how long x and y will live, only that some scope can be
// substituted for 'a that will satisfy this signature.
//
// When annotating lifetimes in functions, the annotations go in the function signature, not in the
// function body. The lifetime annotations become part of the contract of the function, much like
// the types in the signature. Having function signatures contain the lifetime contract means the
// analysis the Rust compiler does can be simpler. If there's a problem with the way a function is
// annotated or the way it is called, the compiler errors can point to the part of our code and the
// constraints more precisely. If, instead, the Rust compiler made more inferences about what we
// intended the relationships of the lifetimes to be, the compiler might only be able to point to a
// use of our code many steps away from the cause of the problem.
//
//
