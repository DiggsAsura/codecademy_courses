// Destructuring to Break Apart Values
// ===================================
//
// We can also Use patterns to destructure structs, enums, and tuples to use different parts of
// these values. Let's walk through each value.
//
//
//
// p1: Destructuring Strucst
// ---------------------
//
// Listing 18-12 shows a Point struct with two fields, x and y, that we can break apart using a
// pattern with a let statement.

fn p1() {
    struct Point {
        x: i32,
        y: i32,
    }

    let p = Point { x: 0, y: 7 };

    let Point { x: a, y: b } = p;
    assert_eq!(0, a);
    assert_eq!(7, b);

    println!("a: {}, b: {}", a, b);
}

// Listing 18-12: Destructuring a struct's fields into separate variables

// This code creates the variables a and b that match the values of the x and y fields of the p
// struct. This example shows that the names of the variables in the pattern don't have to match
// the field names of the struct. However, it's common to match the variable names to the field
// names to make it easier to remember which variables came from which fields. Because of this
// common usage, and because writing let Point { x: x, y: y } = p; contains a lot of duplication,
// Rust has a shorthand for aptterns that match struct fields: you only need to list the name of
// the struct field, and the variables created from the pattern will have the same names. Listing
// 18-13 behaves in the same way as the code in Listing 18-12, but the variables created in the let
// pattern are x and y instead of a and b.

fn p2() {
    struct Point {
        x: i32,
        y: i32,
    }

    let p = Point { x: 0, y: 7 };

    let Point { x, y } = p;
    assert_eq!(0, x);
    assert_eq!(7, y);

    println!("x: {}, y: {}", x, y);
}

// Listing 18-13: Destructuring struct fields using struct field shorthand

// This code creates the variables x and y that matches the x and y fields of the p variable. The
// outcome is that the variables x and y contain the values from the p struct.
//
// We can also destructure with literal values as part of the struct pattern rather than creating
// variables for all the fields. Doing so allows us to test some of the fields for particular
// values while creating variables to destructure the other fields.
//
// In Listing 18-14, we have a match expression that separates Point values into three cases:
// points that lie directly on the x axis (which is true when y = 0), on the y axis (x = 0), or
// neither.

fn p3() {
    struct Point {
        x: i32,
        y: i32,
    }

    let p = Point { x: 0, y: 7 };

    match p {
        Point { x, y: 0 }   => println!("On the x axis at {}", x),
        Point { x: 0, y }   => println!("On the y axis at {}", y),
        Point { x, y }      => println!("On neither axis: ({}, {})", x, y),
    };
}


fn main() {
    p1();
    p2();
    p3();
}

// Listing 18-14: Destructuring and matching literal values in one pattern

// The first arm will match any point that lies on the x axis by specifying that the y field
// matches if its value matches the literal 0. The pattern still creates an x variable that we can
// use in the code for this arm.
//
// Similarly, the second arm matches any point on the y axis by specifying that the x field matches
// if its value is 0 and creates a variable y for the value of the y field. The ghird arm doesn't
// specify any literals, so it matches any other Point and creates variables for both the x and y
// fields.
//
// In this example, the value p matches the second arm by virtue of x containing a 0, so this code
// will print On the y axis at 7.
//
// Remember that a match expression stops checking arms once it has found the first matching
// pattern, so even though Point { x: 0, y: 0 } is on the x axis and y axis, this code would only
// print On the x axis at 0.
