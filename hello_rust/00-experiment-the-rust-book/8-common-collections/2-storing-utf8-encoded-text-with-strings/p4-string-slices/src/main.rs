// String Slices
//
// Indexing into a string is often a bad idea because it's not clear what the return type of
// the string-indexing operation should be: a byte value, a character, a grapheme cluster,
// or a string slice. If you really need to use indices to create string slices, therefor,
// Rust asks you to be more specific.
//
// Rather than indexing using [] with a single number, you can use [] with a range to create
// a string slice containing particular bytes:

fn main() {
    let hello = "Здравствуйте";
    let s = &hello[0..4]; // Зд
    println!("{}", s);
}

// Here, s will be a &str that contains the first 4 bytes of the string. Earlier, we
// mentioned that each of these characters was 2 bytes, which means s will be Зд.
//
// If we were to try to slice only part of a character's byte with something like
// &hello[0..1], Rust would panic at runtime in the same way as if an invalid index
// were accessed in a vector:
//
// $ cargo run
//    Compiling collections v0.1.0 (file:///projects/collections)
//     Finished dev [unoptimized + debuginfo] target(s) in 0.25 secs
//      Running `target/debug/collections`
//   thread 'main' panicked at 'byte index 1 is not a char boundary; it is inside 'З' (bytes 0..2) of `Здравствуйте`', src/libcore/str/mod.rs:1989:5
//   note: Run with `RUST_BACKTRACE=1` for a backtrace.
//
// You should use ranges to create string slices with caution, because doing so can crash
// your program.
