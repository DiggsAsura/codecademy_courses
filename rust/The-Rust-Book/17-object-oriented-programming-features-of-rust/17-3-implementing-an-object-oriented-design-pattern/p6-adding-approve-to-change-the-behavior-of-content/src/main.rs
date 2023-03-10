// Adding approve to Change the Behavior of content
// ===============================================
//
// The approve method will be similar to the request_review method: it will set state to the value
// that the current state says it should have when the state is approved, as shown in Listing
// 17-16:

impl Post {
    //--snip--
    pub fn approve(&mut self) {
        if let Some(s) = self.state.take() {
            self.state = Some(s.approve());
        }
    }

    // 17-17
    pub fn content(&self) -> &str {
        self.state.as_ref().unwrap().content(&self)
    }
}

trait State {
    fn request_review(self: Box<Self>) -> Box<dynState>;
    fn approve(self: Box<Self>) -> Box<dyn State>;

    // 17-18
    fn content<'a>(&self, post: &'a Post) -> &'a str {
        ""
    }
}

struct Draft {}

impl State for Draft {
    // --snip--
    fn approve(self: Box<Self>) -> Box<dyn State> {
        self
    }
}

struct PendingReview {}

impl State for PendingReview {
    // --snip--
    fn approve(self: Box<Self>) -> Box<dyn State> {
        Box::new(Published {})
    }
}

struct Published {}

impl State for Published {
    fn request_review(self: Box<Self>) -> Box<dyn State> {
        self
    }

    fn approve(self: Box<Self>) -> Box<dyn State> {
        self
    }

    // 17-18
    fn content<'a>(&self, post: &'a Post) -> &'a str {
        &post.content
    }
}
// Listing 17-16: Implementing the approve method on Post and the State trait
// Listing 17-17: Updating the content method on Post to delegate to a content method on State
// Listing 17-18: Adding the content method to the State trait

// Why Not An Enum?
// You may have been wondering why we didn't use an enum with the different possible post states as
// variants. That's certainly a possible solution, try it and compare the end results to see which
// you prefer! One disadvantage using an enum is every place that checks the value of the enum will
// need a match expression or similar to handle every possible variant. This could get more
// repetitive than this trait object solution.

