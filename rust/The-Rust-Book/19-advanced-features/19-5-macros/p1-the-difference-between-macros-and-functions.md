# The Difference Between Macros and Functions

Fundamentally, macros are a way of writing code that writes other code, which is known as
*metaprogramming*. In Appendix C, we discuss the **derive** attribute, which generates an
implementation of various traits for ou. We've also used the **println!** and **vec!** macros
throughout the book. All of these macros *expand* to produce more code than the code you've written
manually.

Metaprogramming is useful for reducing the amount of code you have to write and maintain, which
is also one of the roles of functions. However, macros have some additional powers that functions
don't.

A function signature must declare the number and type of parameters the function has. Macros, on
the other hand, can take a variable number of parameters: we can call **println!("hello")** with one
argument or **println!("hello {}", name)** with two arguments. Also, macros are expanded before
the compiler interprets the meaning of the code, so a macro can, for example, implement a trait on
a given type. A function can't, because it gets called at runtime and a trait needs to be implemented
at compile time.

The downside to implementing a macro instead of a function is that macro definitions are more
complex than function defintions because you're wirting Rust code that writes Rust code. Due o
this indirection, macro definitions are genrally more difficult to read, understand, and maintain
than function definitions.

Another important difference between macros and fucntions is that you must define macros or
bring them into scope *before* you call them in a file, as opposed to functions you can define
anywhere and call anywhere.
