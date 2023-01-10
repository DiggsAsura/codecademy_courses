struct User {
    username: String,
    email: String,
    sign_in_count: u64,
    active: bool,
}


fn main() {
    let mut user1 = User {
        email: String::from("testing@gmail.com"),
        username: String::from("Diggs"),
        active: true,
        sign_in_count: 1,
    };

    let name = user1.username;
    user1.username = String::from("DiggsAsura");

    let user2 = build_user(
        String::from("diggy@diggs.com"),
        String::from("diggi"),
    );

    let user3 = User {
        email: String::from("bb@ken.com"),
        username: String::from("bbken"),
        ..user2
    };

    

    struct Color(i32, i32, i32); // Tuple struct
    struct Point(i32, i32, i32); 


}

fn build_user(email: String, username: String) -> User {
    User {
        email: email,
        username: username,
        active: true,
        sign_in_count: 1,
    }
}

