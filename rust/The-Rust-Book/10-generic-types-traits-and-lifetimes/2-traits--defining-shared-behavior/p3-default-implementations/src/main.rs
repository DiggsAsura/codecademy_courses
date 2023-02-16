// Default Implementations
// =======================
//
// Sometimes it's useful to have default behavior for some or all of the methods in a trait instead
// of requiring implementations for all methods on every type. Then, as we implement the trait on a
// particular type, we can keep or override each method's default behavior.
//
// In Listing 10-14 we specify a default string for the summarize method of the Summary trait
// instead of only defining the method signature, as we did in Listing 10-12.

// simulating a lib.rs file with mod

fn main() {
    ex1();
    ex2();
}
mod listing_10_14 {
    pub trait Summary {
        fn summarize(&self) -> String {
            String::from("(Read more...)")
        }
    }

    pub trait Summary2 {
        fn summarize_author(&self) -> String;
        fn summarize(&self) -> String {
            format!("(Read more from {}...)", self.summarize_author())
        }
    }

    impl Summary2 for Tweet {
        fn summarize_author(&self) -> String {
            format!("@{}", self.username)
        }
    }

    pub struct Tweet {
        pub username: String,
        pub content: String,
        pub reply: bool,
        pub retweet: bool,
    }
    pub struct NewsArticle {
        pub headline: String,
        pub location: String,
        pub author: String,
        pub content: String,
    }

    impl Summary for NewsArticle {
    }
}
// 10-14: Defining a Summary trait with a default implementation of the summarize method

// To use a default implementation to summarize instances of NewsArticle, we specify an empty impl
// block with impl Summary for NewsArticle {}.
//
// Even though we're no longer defining the summarize method on NewsArticle directly, we've
// provided a default implementation and specified that NewsArtivcle implements the Summary trait.
// As a result, we can still call the summarize method on an instance of NewsArticle like this:

fn ex1() {
    use listing_10_14::{NewsArticle, Summary};

    let article = NewsArticle {
        headline: String::from("Penguins win the Stanley Cup Championship!"),
        location: String::from("Pittsburgh, PA, USA"),
        author: String::from("Iceburgh"),
        content: String::from("The Pittsburgh Penguins once again are the best \
                              hockey team in the NHL.",
        ),
    };

    println!("New article available! {}", article.summarize());
}
// This code prints New article available! (Read more...).
//
// Creating a default implementation doesn't require us to change anything about the implementation
// of Summary on Tweet in Listing 10-13. The reason is that the syntax for overriding a default
// implementation is the same as the syntax for implememting a trait method that doesn't have a
// default implementation.
//
// Default implementations can call other methods in the same trait, even if those other methods
// don't have a default implementation. In this way, a trait can provide a lot of useful
// functionality and only require implementors to specify a small part of it. For example, we could
// define the Summary trait to have a summarize_author method whose implementation is required, and
// then define a summarize method that is a default implementation that calls the summarize_author
// method.

// see the mod above

// After we define summarize_author, we can call summarize on instances of the Tweet struct, and
// the default implementation of summarize will call the definition of summarize_author that we've
// provided. Because we've implemented summarize_author, the Summary trait has given us the
// behavior of the summarize method without requiring us to write any more code.

fn ex2() {
    use listing_10_14::{Summary2, Tweet};

    let tweet = Tweet {
        username: String::from("horse_ebooks"),
        content: String::from(
            "of course, as you probably already know, people",
        ),
        reply: false,
        retweet: false,
    };

    println!("1 new tweet: {}", tweet.summarize());
}

// This code prints 1 new tweet: (Read more from @horse_ebooks...).

// Note that it isn't possible to call the dfault implementation from an overriding implementation
// of that same method.

