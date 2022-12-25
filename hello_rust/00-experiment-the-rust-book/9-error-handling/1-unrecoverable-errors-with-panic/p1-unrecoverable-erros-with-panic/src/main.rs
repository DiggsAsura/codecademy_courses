// Unrecoverable Errors with panic!
// ===============================
//
// Sometimes, bad things happen in your code, and there's nothing you can
// do about it. In these cases, Rust has the panic! macro. There are two ways
// to cause a panic in practice: by taking an action that causes our code to panic
// (such as accessing an array past the end) or by explicitly calling the panic!
// macro. In both cases, we cause a panic in our program. By default, these panics will
// print a failure message, unwind, clean up the stack, and quit. Via an environment
// variable, you can also have Rust display the call stack when a panic occurs and make
// easier to track down the source of the panic.
//
//
// Unwinding the Stack or Aborting in Response to a Panic
// ------------------------------------------------------
//
// By default, when a panic occurs, the program starts unwinding, which means Rust
// walks back up the stack and cleans up the data from each function it encounters.
// However, this walking back up and cleanup is a lot of work. Rust, therefore, allows you
// to choose the alternative of immediately aborting, which ends the program
// without cleaning up.
//
// Memory that the program was using will then need to be cleaned up by the operating
// system. If in your project you need to make the resulting binary as small as possible,
// you can switch from unwinding to aborting upon a pnaic by adding panic = 'abort' to
// appropriate [profile] sections in your Cargo.toml file. For example, if you
// want to abort on panic in release mode, add this:
//
// [profile.release]
// panic = 'abort'
// ------------------------------------------------------

// Let's try calling panic! in a simple program:

fn main() {
    panic!("Crash and burn");
}

// The call to panic! causes the error message contained in the last two lines. The first
// line shows our panic message and the place in our source code where the panic occured:
// src/main.rs:17:5. indicates that it't the 17th line, fifth character of our
// src/main.rs file.
//
// In this case, the line indicated is part of our code, and if we go to that line, we see
// the panic! macro call. In other cases, the panic! call might be in code that our code calls,
// and the filename and line number reported by the error message will be someone else's
// code where the panic! macro is called, not the line of our code that eventually
// led to the panic! call. We can use the backtrace of the function the panic! call
// from to figure out the part of our code that is causing the problem. We'll discuss
// Backtraces in more detail next.
