# Unsafe Rust

All the code we've discussed so far has had Rust's memory safety guarantees enforced at compile
time. However, Rust has a second language hidden inside it that doesn't enforce these memory
safety guarantees: it's called *unsafe Rust* and works just like regular Rust, but gives us extra
superpowers.

Unsafe Rust exists because, by nature, static analysis is conservative. When the compiler tries to
determine whether or not code upholds the guarantees, it's better for it to reject some valid
programs than to accept some invalid programs. Although the code *might* be okay, if the Rust
compiler doesn't have enough information to be confident, it will reject the code. In these cases,
you can use unsafe code to tell the compiler, "Trust me, I know what I'm doing." Be warned,
however, that you use unsafe Rust at your own risk: if you use unsafe code incorrectly, problems
can occur due to memory unsafety, such as null pointer dereferencing.

Another reason Rust ahs an unsafe alter ego is that the underlying computer hardware is
inherently unsafe. If Rust didn't let you do unsafe operations, you couldn't do certain tasks. Rust
needs to allow you to do low-level systems programming, such as directly interacting with the
operating system or even writing your own operating system. Working with low-level systems
programming is one of the goals of the language. Let's explore what we can do with unsafe Rust
and how to do it.
