// Unsing a panic! Backtrace
// =========================
//
// Let's look at another example to see what it's like when a panic! call comes from
// a library because of a bug in our code instead of from our code calling the macro
// directly. Listing 9-1 has some code that attempts to access an index in a vector
// beyond the range of valid indexes.

fn main() {
    let v = vec![1, 2, 3];

    v[99];
}
// 9-1: Attempting to access an alement beyond the end of a vector

// Here, we're attempting to access the 100th element of our vector (which is at index 99
// because indexint starts at zero), but the vector has only 3 elements. In this
// situation, Rust will panic. Using [] is supposed to return an element, but
// if you pass an invalid index, there's no element that Rust could return here that would
// be correct.
//
// In C, attempting to read beyond the end of a data structure is undefined behavior. You
// might get whatever is at the location in memory that would correspond to that element
// in the data structure, even though the memeory doesn't belong to that structure. This
// is called a buvver ovverread and can lead to security vulnerabilities if an
// attacker is able to manipulate the index in such a way as to read data they
// shouldn't be allowed to that is stored after the data structure.
//
// To protect your program from this sort of vulnerability, if you try to read an
// element at an index that doesn't exist, Rust will stop execution and refuse to
// continue. Let's try it and see:


/*
$ cargo run
   Compiling panic v0.1.0 (file:///projects/panic)
    Finished dev [unoptimized + debuginfo] target(s) in 0.27s
     Running `target/debug/panic`
thread 'main' panicked at 'index out of bounds: the len is 3 but the index is 99', src/main.rs:4:5
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
*/


// This error points at line 4 of our main.rs where we attempted to access index 99. The
// next note line tells us that we can set the RUST_BACKTRACE environment variable to get a
// backtrace of exactly what happend to cause the error. A backtrace is a list of all the
// functions that have been called to get to this point. Backtraces in Rust work as they do
// in other languages: the key to reading the backtrace is to start from the top and read
// until you see files you wrote. That's the spot where the problem originated. The lines above
// that spot are code that your code has called; the lines below are code that called
// your code. These before-and-after lines might include core Rust code, standard Library
// code, or crates that you're using. Let's try getting a backtrace by setting the
// RUST_BACKTRACE environment variable to any value except 0. Listing 9-2 shows output
// similar to what you'll see.

/*
$ RUST_BACKTRACE=1 cargo run
thread 'main' panicked at 'index out of bounds: the len is 3 but the index is 99', src/main.rs:4:5
stack backtrace:
   0: rust_begin_unwind
             at /rustc/7eac88abb2e57e752f3302f02be5f3ce3d7adfb4/library/std/src/panicking.rs:483
   1: core::panicking::panic_fmt
             at /rustc/7eac88abb2e57e752f3302f02be5f3ce3d7adfb4/library/core/src/panicking.rs:85
   2: core::panicking::panic_bounds_check
             at /rustc/7eac88abb2e57e752f3302f02be5f3ce3d7adfb4/library/core/src/panicking.rs:62
   3: <usize as core::slice::index::SliceIndex<[T]>>::index
             at /rustc/7eac88abb2e57e752f3302f02be5f3ce3d7adfb4/library/core/src/slice/index.rs:255
   4: core::slice::index::<impl core::ops::index::Index<I> for [T]>::index
             at /rustc/7eac88abb2e57e752f3302f02be5f3ce3d7adfb4/library/core/src/slice/index.rs:15
   5: <alloc::vec::Vec<T> as core::ops::index::Index<I>>::index
             at /rustc/7eac88abb2e57e752f3302f02be5f3ce3d7adfb4/library/alloc/src/vec.rs:1982
   6: panic::main
             at ./src/main.rs:4
   7: core::ops::function::FnOnce::call_once
             at /rustc/7eac88abb2e57e752f3302f02be5f3ce3d7adfb4/library/core/src/ops/function.rs:227
note: Some details are omitted, run with `RUST_BACKTRACE=full` for a verbose backtrace.
*/


// That's a lot of output! The exact output you see might be different depending on your
// operating system and Rust version. In order to get backtrace with this information,
// debug symbols must be enabled. Debug symbols are enabled by default when using
// cargo build or cargo run without the --release flag, as we have here.
//
// In the output in Listing 9-2, line 6
