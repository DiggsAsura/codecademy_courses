// Specifying Multiple Trait Bounds with the + Syntax
// =================================================
//
// We can also specify more than one trait bound. Say we wanted notify to use display fomatting as
// well as summarize on item: we specify in the notify definition that item must implement both
// Display and Summary. We can do so using the + syntax:

pub fn notify(item: &(impl Summary + Display)) {}

// The + syntax is also valid with trait bounds on generic types:

pub fn notify<T: Summary + Display>(item: &T) {}

// With the two trait bounds specified, the body of notify can call summarize and use {} to format
// item.
