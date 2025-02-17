// Encapsulation that Hides Implementation Details
// ==================================================
//
// Another aspect commonly associated with OOP is the idea of encapsulation, which means that the
// implementation details of an object aren't accessible to code using that object. Therefore, the
// only way to interact with an object is through its public API; code using the object shouldn't
// be able to reach into the objects's internals and change data or behavior directly. This enables
// the programmer to change and refactor an object's internals without needing to change the code
// that uses the object.
//
// We discussed how to control encapsulation in Chapter 7: we can use the pub keyword to decide
// which modules, types, functions, and methods in our code should be public, and by default
// everything else is private. For example, we can define a struct AveragedCollection that has
// field containing a vector of i32 values. The struct can also have a field that contains the
// average of the values in the vector, meaning the average doesn't have to be computed on demand
// whenever anyone needs it. In other words, AveragedCollection will cache the calculated average
// for us.
//
// Listing 17-1 has the definition of the AveragedCollection struct:

pub struct AveragedCollection {
    list: Vec<i32>,
    average: f64,
}

// Listing 17-1: An AveragedCollection struct that maintains a list of integers and the average of
// the items in the collection

// The struct is marked pub so that other code can use it, but the fields within the struct remain
// private. This is important in this case because we want to ensure that whenever a value is added
// or removed from the list, the average is also updated. We do this by implementing add, remove,
// and average methods on the struct, as shown in Listing 17-2:

impl AveragedCollection {
    pub fn add(&mut self, value: i32) {
        self.list.push(value);
        self.update_average();
    }

    pub fn remove(&mut self) -> Option<i32> {
        let result = self.list.pop();
        match result {
            Some(value) => {
                self.update_average();
                Some(value)
            }
            None => None,
        }
    }

    pub fn average(&self) -> f64 {
        self.average
    }

    fn update_average(&mut self) {
        let total: i32 = self.list.iter().sum();
        self.average = total as f64 / self.list.len() as f64;
    }
}

fn main() {}
// Listing 17-2: Implementations of the public method add, remove and average on AveragedCollection

// The public methods add, remove, and average are the only ways to access or modify data in an
// instance of AveragedCollection. When an item is added to list using the add method or removed
// using the remove method, the implmentations of each call the private update_average method that
// handles updating the average field as well.
//
// We leave the list and average fields private so there is no way for external code to add or
// remove items to or from the list field directly; otherwise, the average field might becaome out
// of sync when the list changes. The average method returns the value in the average field,
// allowing external code to read the average but not modify it.
//
// Because we've encapsulated the implementation details of the struct AveragedCollection, we can
// easily change aspects, such as the data structure, in the future. For instance, we could use a
// HashSet<i32> instead of a Vec<i32> for the list field. As long as the signatures of the add,
// remove and average public methods stay the same, code using AveragedCollection wouldn't need to
// change. If we made list public instead, this wouldn't necessarily be the case: HashSet<i32> and
// Vec<i32> have different methods for adding and removing items, so the external code would likely
// have to change if tit were modifying list directly.
//
// If encapsulation is a required aspect for a language to be considered object-oriented, then Rust
// meets that requirement. The option to use pub or not for different parts of code enables
// encapsulation of implementation details.
