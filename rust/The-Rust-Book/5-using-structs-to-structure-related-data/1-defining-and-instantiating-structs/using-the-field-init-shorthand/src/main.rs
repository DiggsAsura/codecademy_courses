#[derive(Debug)]
struct User {
    email: String,
    username: String,
    active: bool,
    sign_in_count: u64,
}


/* Sooo instead of writing a lot of double up like this: 
 */
fn build_user(email: String, username: String) -> User {
    User {
        email: email,
        username: username,
        active: true,
        sign_in_count: 1,
    }
}

/* ...you can do the shorthand version! */
fn build_user_easier(email: String, username: String) -> User {
    User {
        email,
        username,
        active: true,
        sign_in_count: 1,
    }
}
fn main() {
    let user1 = build_user_easier("kenny@bb.com".to_string(), "kennethbb".to_string());
    println!("{:?}", user1);
}

/* Sooo, when the parameter and the struct field has the same name, it can be written only once!
 * Saving some typing */

