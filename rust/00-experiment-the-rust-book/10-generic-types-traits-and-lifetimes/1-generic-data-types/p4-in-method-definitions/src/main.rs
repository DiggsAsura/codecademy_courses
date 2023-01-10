// In Method Definitions
// =====================
//
// We can implement methods on structs and enums (as we did in Chapter 5) and use generic types in
// their definitions, too. Listing 9-10 shows the Point<T> struct we defined in Listing 10-6 with a
// method named x implemented on it.

fn main() {
    listing_10_9();
    listing_10_10();
    listing_10_11();
}

fn listing_10_9() {
    struct Point<T> {
        x: T,
        y: T,
    }

    impl<T> Point<T> {
        fn x(&self) -> &T {
            &self.x
        }
    }

    let p = Point { x: 5, y: 10 };

    println!("p.x = {}", p.x());
}

// 19-9: Implementing a method named x on the Point<T> struct that iwll return a reference to the x
// field of type T.

// Here, we've defined a method named x on Point<T> that returns a reference to the data in the
// field x.
//
// Note that we have to declare T just after impl so that we can use T to specify that we're
// implementing methods on the type Point<T>. Bey declaring T as a generic type after impl, Rust
// can identify that the type in the angle brackets in Point is a generic type rather than a
// concrete type. We could have chosen a different name for this generic parameter than the generic
// parameter declared in the struct definition, but using the same name is conventional. Methods
// written with an impl that declares the generic type will be defined on any instance of the type,
// no matter what concrete type ends up substituting for the generic type.
//
// We can also specify constraints on generic types when defining methods on the type. We could,
// for example, implement methods only on Point<f32> instances rather than on Point<T> instances
// with a generic type. In Listing 10-10 we use the concrete type f32, meaning we don't declare any
// types after impl.

fn listing_10_10() {
    struct Point<T> {
        x: T,
        y: T,
    }

    impl Point<f32> {
        fn distance_from_origin(&self) -> f32 {
            (self.x.powi(2) + self.y.powi(2)).sqrt()
        }
    }
    let p = Point { x: 5.0, y: 10.0 };
    let y = p.distance_from_origin();
    println!("y = {}", y);
}
// Listing 10-10: An impl block that only applies to a struct with a particular concrete type for
// the generic type parameter T

// This code means the type Point<f32> will have a distance_from_origin method; other instances of
// Point<T> where T is not of type f32 will not ahve this method defined. The method measures how
// far our point is from the point at coordinates (0.0, 0.0) and uses mathematical operations that
// are available only for floating point types.
//
// You cannot simultaneously implement specific and generic methods of the same name this way. For
// example, if you implemented a general distance_from_origin for all types T and a specific
// distance_from_origin for f32, then the compiler will reject your program: Rust does not know
// which implementation to use when you call Point<f32>::distance_from_origin. More generally, Rust
// does not have inheritance-like mechanisms for specializing methods as you might find in an
// object-oriented lanuages, with one exception (Default trait methods) discussed in the next
// section.
//
// Generic types parameters in a struct definition aren't always the same as those you use in that
// same struct's method signatures. Listing 10-11 uses a generic type X1 and Y1 for the Point
// struct and X2 Y2 for the mixup method signature to make the example clearer. The method creates
// a new Point instance with the x value from the self Point (of type X1) and the y value from the
// passed-in Point (of type Y2).

fn listing_10_11() {
    struct Point<X1, Y1> {
        x: X1,
        y: Y1,
    }

    impl<X1, Y1> Point<X1, Y1> {
        fn mixup<X2, Y2>(self, other: Point<X2, Y2>) -> Point<X1, Y2> {
            Point {
                x: self.x,
                y: other.y,
            }
        }
    }

    let p1 = Point { x: 5, y: 10.4 };
    let p2 = Point { x: "Hello", y: 'c' };

    let p3 = p1.mixup(p2);

    println!("p3.x = {}, p3.y = {}", p3.x, p3.y);
}
// 10-11: A method that uses generic types different from its struct's definition

// In main, we've defined a Point that has an i32 for x (with value 5) and an f64 for y (with value
// 10.4). The p2 variable is a Point struct that has a string slice for x (with value "Hello") and
//    a char for y (with value c). Calling mixup on p1 with the arbument p2 gives us p3, which will
//    have an i32 for x, because x came from p1. The p3 variable will have a char for y, because y
//    came from p2. The println! macro call will print p3.x = 5, p3.y = c.
//
//    The purpose of this mixup is to demonstrate situations in which some generic parameters are
//    declared with impl and some are declared with the method definition. Here, the generic
//    parameters X1 and Y1 are declared after impl because they go with the struct definition. The
//    generic parameters X2 and Y2 are declared after fn mixup, because they're only relevant to
//    the method.
