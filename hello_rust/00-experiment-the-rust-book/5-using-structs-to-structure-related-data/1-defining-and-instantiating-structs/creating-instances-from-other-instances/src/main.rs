/* Creating Instances from Other Instances with Struct Update Syntax
 *
 * This is about reusing info from other instances of the struct.
 *
 */
struct User<'a> {
    active: bool,
    username: &'a str,
    email: &'a str,
    sign_in_count: u32
}

fn main() {
    let user1 = User {
        active: true,
        username: "Kenneth",
        email: "ken@bje.com",
        sign_in_count: 1,
    };

    // Heres the real example. see how we call f.x user1.active,

    let user2 = User {
        active: user1.active,
        username: user1.username,
        email: "another@example.com",
        sign_in_count: user1.sign_in_count,
    };

    //println!("{}", &user1.username); // can't compile, because String does not implement copy
    println!("{}", &user2.username);


    /* Using struct update syntax, we can achieve the same effect with less code, as shown here.
     * The syntax .. specifies that the remaining fields not explicitly set should have the same
     * value as the fields in the given instance.  */

    let user3 = User {
        email: "bjejbe@ken.com",
        ..user1
    };

    println!("{}", user3.active);
    println!("{}", user2.email);
}

/* Note that the struct update syntax uses = like an assignment; this is because it moves the data,
 * just as we saw in the "Ways Variables and Data Interact: Move" section. In this example, we can
 * no longer use user1 after creating user2 because the String in the username field of user1 was
 * moved into user2. If we had given user2 new String values for both email and username, and thus
 * only used the active and sign_in_count values from user1, then user1 would still be valid after
 * creating user2. The types of active and sign_in_count are types that implement the Copy trait,
 * so the behavoior we discussed in the "Stack-Only Data: Copy" section would apply.
 */

