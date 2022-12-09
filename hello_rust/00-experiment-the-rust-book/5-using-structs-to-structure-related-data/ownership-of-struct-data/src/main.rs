/* Ownership of Struct Data
 *
 * In the User struct definition earlier, we used the owned String type rather than the &str string
 * slice type. This is deliberate choice because we want each instance of this struct to own all of
 * its data and for that data to be valid for as long as the entire struct is valid.
 *
 * It's also possible for structs to store references to data owned by something else, but to do
 * so require the use of lifetimes, a Rust feature that we'll discuss in Chapter 10. Lifetimes
 * ensure that the data referenced by a struct is valid for as long as the struct is. Let's say you
 * try to store a reference in a struct without specifying lifetimes, like the following won't
 * work:
 */

// I added the lifetime stuff so it work regardless though. 
struct User<'a> {
    active: bool,
    username: &'a str,
    email: &'a str,
    sign_in_count: u64,
}

fn main() {
    let user1 = User {
        email: "someone@example.com",
        username: "someusername123",
        active: true,
        sign_in_count: 1,
    };
}

/* In Chapter 10, we'll discuss how to fix these errors so you can store references in structs, but
 * for now, we'll fix errors like these owned types like String instead of references like &str. */

