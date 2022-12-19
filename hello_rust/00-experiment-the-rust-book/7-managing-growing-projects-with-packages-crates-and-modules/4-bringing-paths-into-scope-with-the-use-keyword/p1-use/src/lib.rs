// Bringing Paths into Scope with the use Keyword

mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

use crate::front_of_house::hosting;
// use crate::folder::folder; // no function

pub fn eat_at_resturant() {
    hosting::add_to_waitlist();
    hosting::add_to_waitlist();
    hosting::add_to_waitlist();
}

// Adding use and a path in a scope is similar to creating a symbolic link in the
// filesystem. By adding use crate::front_of_house::hosting in the crate root, hosting is now
// a valid name in that scope, just as though the hosting module had been defined
// in the crate root. Paths brought into scope with use also check privacy, like any other
// paths.
//
// Note that use only creates the shortcut for the particular scope in which
// the use occurs. Listing below moves the eat_at_resturant function into a new child
// module named customer, which is then a different scope than the use statement,
// so the function body won't compile:

mod front_of_house_2 {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

// this wont work here, as customer is another scope
// use crate::front_of_house_2::hosting;
mod customer {
    use crate::front_of_house_2::hosting;  // this works however, as its moved into scope
    pub fn eat_at_resturant() {
        hosting::add_to_waitlist();
        hosting::add_to_waitlist();
        hosting::add_to_waitlist();
    }
}

// Could also had used super from inside the customer scope.
