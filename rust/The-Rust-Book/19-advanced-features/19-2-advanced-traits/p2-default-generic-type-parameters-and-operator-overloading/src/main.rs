// Default Generic Type Parameters and Operator Overloading
// =======================================================
//
// When we use generic type parameters, we can specify a default concrete type for the generic
// type. This eliminates the need for implementors of the trait to specify a concrete type if the
// default type works. You specify a default type when declaring a generic type with the
// <PlaceholderType=ConcreteType> syntax.
//
// A great example of a situation where this technique is useful is with operator overloading, in
// which you customize the behavior of an operator (such as +) in particular situations.
//
// Rust doesn't allow you to create your own operators or overload arbitrary operators. But you can
// overload the operations and corresponding traits listed in std::ops by implementing the traits
// associated with the operator. For example, in Listing 19-14 we overload the + operator to add
// two Point instances together. We do this by implementing the Add trait on a Point struct:

use std::ops::Add as OtherAdd;

#[derive(Debug, Copy, Clone, PartialEq)]
struct Point {
    x: i32,
    y: i32,
}

impl OtherAdd for Point {
    type Output = Point;

    fn add(self, other: Point) -> Point {
        Point {
            x: self.x + other.x,
            y: self.y + other.y,
        }
    }
}

fn main() {
    assert_eq!(
        Point { x: 1, y: 0 } + Point { x: 2, y: 3 },
        Point { x: 3, y: 3 }
    );
}
// Listing 19-14: Implementing the Add trait to overload the + operator for Point instances

// The add method adds the x values of the two Point instances and the y values of two Point
// instances to create a new Point. The Add trait has an associated type named Output that
// determines the type returned from the add method.
//
// The default generic type in this code is within the Add trait. Here is its definition:

trait Add<Rhs=Self> {
    type Output;

    fn add(self, rhf: Rhs) -> Self::Output;
}

// This code should look generally familiar: a trait with one method and an associated type. The
// new part is Rhs=Self: this syntax is called default type parameters. The Rhs generic type
// parameter (short for "right hand side") defines the type of the rhs parameter in the add method.
// If we don't specify a concrete type for Rhs when we implement the Add trait, the type of Rhs
// will default to Self, which will be the type we're implementing Add on.
//
// When we implemented Add for Point, we used the default for Rhs because we wanted to add two
// Point instances. Let's look at an example of implementing the Add trait where we want to
// customize the Rhs type rather than using the default.
//
// We have two structs, Millimieters and Meters, holding values in different units. This thin
// wrapping of an existing type in another struct is known as the newtype pattern, which we
// describe in more detail in the "Using the Newtype Pattern to Implement External Traits on
// External Types" section. We want to add values in milimeters to values in meters and have the
// implmeentation of Add do the conversion coorrectly. We can implemtn Add for Millimeters with
// Meters as the Rhs, as shown in Listgin 19-15.

/*
use std::ops::Add;
*/

struct Millimeters(u32);
struct Meters(u32);

impl Add<Meters> for Millimeters {
    type Output = Millimeters;

    fn add(self, other: Meters) -> Millimeters {
        Millimeters(self.0 + (other.0 * 1000))
    }
}

// Listing 19-15: Implementing the Add trait on Milimeters to add Millimeters to Meters

// To add Millimeters and Meters, we specify impl Add<Meter> to set the value of the Rhs type
// parameter instead of using the default of Self.
//
// You'll use default type parameters in two main ways:
//
// - To extend a type without breaking 3existing code
// - To allow customization in specific cases most users won't need
//
// The standard library's Add trait is an example of the second purpose: usually, you'll add two
// like types, but the Add trait provides the ability to customize beyond that. Using a default
// type parameter in the Add trait definition means you don't have to specify the extra parameters
// most of the time. In other words, a bit of implementation boilerplate isn't needed, making it
// easier to use the trait.
//
// The first purpose is similar to the second but in reverse: if you want to add a type parameter
// to an existing trait, you can give it a default to allow extension of the functionality of the
// trait without breaking the existing implementation code.
