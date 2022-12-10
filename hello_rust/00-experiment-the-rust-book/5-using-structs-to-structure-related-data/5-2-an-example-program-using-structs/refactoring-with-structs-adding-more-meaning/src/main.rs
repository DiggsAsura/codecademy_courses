/* Refactoring with Structs: Adding More Meaning
 *
 * We use structs to add meaning by labeling the data. We can transform the tuple we're using into
 * a struct with a name for the whole as well as anmes for the parts. As shown: */

struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!("The area of the rectangle is {} square pixels.", area(&rect1));
}

fn area(rectangle: &Rectangle) -> u32 {
    rectangle.width * rectangle.height
}

/* Here we've defined struct and named it Rectangle. Inside the curly brackets, we defined the
 * fields as width and height, both of which have type u32. Then in main, we created a particular
 * instance of Rectangle that has a width of 30 and a height of 50.
 *
 * Our area function is now defined with one parameter, which we've named rectangle, whose type is
 * an immutable borrow of a struct Rectangle instance. As mentioned in Chapter 4, we want to borrow
 * the struct rather than take ownership of it. This way, main retains its ownership and can
 * continue using rect1, which is the reason we use the & in the function signature and where we
 * call the function. 
 *
 * The area function accesses the width and height fields of the Rectangle instance (note that
 * accessing fields of a borrowed struct insatnce does not move the fields values, which is why you
 * often see borrows of structs). Our function signature for area now says exactly what we mean:
 * calculate the are of Rectangle, using its width and height fields. This conveys that the width
 * and height are related to each other, and it gives descriptive names to the value rather than
 * using the tuple index values of 0 and 1. This is a win for clairity. */
