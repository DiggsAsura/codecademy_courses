/* Methods with More Parameters
 *
 * Let's practice using methods by implementing a second method on the Rectangle struct. This time,
 * we want an instance of Rectangle to take another instance of Rectangle and return true if the
 * second Rectangle can fit completly within self (the first Rectangle); otherwise it should return
 * false. That is, once we've defined the can_hold method, we want to be able to write the program
 * shown here: 
 */
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };
    let rect2 = Rectangle {
        width: 10,
        height: 40,
    };
    let rect3 = Rectangle {
        width: 60,
        height: 45,
    };

    println!("Can rect1 hold rect2? {}", rect1.can_hold(&rect2));
    println!("Can rect1 hold rect3? {}", rect1.can_hold(&rect3));
}

/* We know we want to define a method, so it will be within the impl Rectangle block. The method
 * name will be can_hold, and it will take an immutable borrow of another Rectangle as a parameter.
 * We can tell what type of the parameter will be by looking at the code that calls the method:
 * rect1.can_hold(&rect2) passes in &rect2, which is an immutable borrow to rect2, an instance of
 * Rectangle. This makes sense because we only need to read rect2 (rather than write, which would
 * mean we'd need a mutable borrow), and we want main to retain ownership of the rect2 so w can use
 * it again after calling the can_hold method. The return value of can_hold will be a Boolean, and
 * the implementation will check wheter the width and height of self are both greater than the
 * width and height of the other Rectangle, respectively. Let's add the new can_hold method to the
 * impl block. 
 */

impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }

    fn can_hold(&self, other: &Rectangle) -> bool {
        self.width > other.width && self.height > other.height
    }
}

/* When we run this code with the main function we'll get our desired output. Methods can take
 * multiple parameters that we add to the signature after the self parameter, and those parameters
 * work just like parameters in functions. */

