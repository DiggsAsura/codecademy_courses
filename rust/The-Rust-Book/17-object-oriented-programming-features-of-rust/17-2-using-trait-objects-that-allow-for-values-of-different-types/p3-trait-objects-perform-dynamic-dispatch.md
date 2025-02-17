# Trait Objects Perform Dynamic Dispatch

Recall the "Performance of Code Using Generics" section in Chapter 10 our discussion on the
monomorphization process performed by the compiler when we use trait bounds on generics: the
compiler generates nongeneric implementations of functions and methods for each concrete type
that we use in place of a generic type parameter. The code that results from monomorphization is
doing *static dispatch*, which is when the compiler knows what method you're calling at compile time.
This is opposed to *dynamic dispatch*, which is when the compiler can't tell at compile time which
method you're calling. In dynamic dispatch cases, the compiler emits code at runtime will figure
out which method to call.

When we use trait objects, Rust must use dynamic dispatch. The compiler doesn't know all the types
that might be used with the code that's using trait objects, so it doesn't know which method
implemented on which type to call. Instead, at runtime, Rust uses the pointers inside the trait object
to know which method to call. This lookup incurs a runtime cost that doesn't occur with static
dispatch. Dynamic dispatch also prevents the compiler from choosing to inline a method's code,
which in turn prevents some opimizations. However, we get extra flexibility in the code that we
wrote in Listing 17-5 and were able to support in Listing 17-9, so it's a trade-off to consider.
