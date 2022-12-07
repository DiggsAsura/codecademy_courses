/* 
 * Defining and Instantiating Structs
 *
 * Somewhat like named tuples. Both have sets of related values, but in structs you can name them
 * (and type annotate them)
 */

struct User {
    active: bool,
    username: String,
    email: String,
    sign_in_count: u64,
}

/* When we create an instance, the order does not matter */

fn main() {
    let user1 = User {
        email: String::from("someones@email.com"),
        username: String::from("someonesusername123!"),
        active: true,
        sign_in_count: 1,
    };

    /* To get a specific value from the struct, we use dot notation. 
     * We can also change values IF the whole instance is mutable. Can not have mutable elements
     * inside the struct. */

    let mut user2 = User {
        email: String::from("kenny@b.com"),
        active: false,
        username: String::from("ayaya"),
        sign_in_count: 200230203,
    };
    user2.email = String::from("diggs@asura.com");

    let email = user2.email;
    println!("{email}");


    /* use the below function */
    let mut user3 = build_user("kenny@bjerke.org".to_string(), "kennethbb".to_string());

    println!("{}", user3.email);
}

/* If making struct types via an function like this, it can make sense to use parameter names equal
 * to struct fields. */

fn build_user(email: String, username: String) -> User {
    User {
        email: email,
        username: username,
        active: true,
        sign_in_count: 1,
    }
}

/* HOWEVER! Theres a shorthand way to do this, instead of typing alot of things twice (email:
 * email, username: username etc 
 *
 * check the next part (Using the Field Init Shorthand)
 */

