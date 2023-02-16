// Cases in Which You Have More Information Than the Compiler
// =========================================================
//
// It would also be appropriate to call unwrap or expect when you have some other
// logic that ensures the Result will have an Ok value, but the logic isn't something
// the compiler understands. You'll still have a Result value that you need to handle:
// whatever operation you're calling still has the possibility of failing in general,
// even though it's logically impossible in your particular situation. If you can
// ensure by manually inspecting the code that you'll never have an Err variant, it's
// perfectly acceptable to call unwrap, and even better to document the reason you think
// you'll never han an Err variant in the expect text. Here's an example:

use std::net::IpAddr;

fn main() {
    let home: IpAddr = "127.0.0.1"
        .parse()
        .expect("Hardcoded IP address should be valid");

    println!("Home IP address: {}", home);
}

// We're creating an IpAddr instance by parsing a hardcoded string. We can see that
// 127.0.0.1 is a valid IP address, so it's acceptable to use expect here. However,
// haveing a hardcoded, valid string doesn't change the reutrn type of the parse method:
// we still get a Result value, and the compiler will still make us handle the Result
// as if the Err variant is a possiblity because the compiler isn't smart enough to see
// that this string is always a valid IP address. If the IP address string came from
// a user rather than being hardcoded into the program and therefore did have a
// possibility of failure, we'd definetly want to handle the Result in a more robust
// way instead. Mentioning the assumption that this IP address is hardcoded will
// prompt us to change expect to better error handling code if in the future, we
// need to get the IP address form some other source instead.
