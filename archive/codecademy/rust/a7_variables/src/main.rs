fn main() {
    println!("{:?}", example_1());
}

// VARIABLES

// In Rust, a variable is an identifier that points to a location in memory.
// This location in memory can be either data or a function.

// Variable Declarations
//
// To assign variables in Rust we utilize the let keyword with the = operator,
// taking the following form: 
//
// let variable = "this is a &str";
//
// We can assign variables to any expression:
//
// This is a closure
// let double = |d| d*2;
//
// This is the outcome of calling the closure
// let var = double(10);
//
// This will re-assign the value of var
// let doubled_var = var;


// INFERRED TYPES
//
// The Rust compiler is good at inferring types based on context. In the 
// following example, the datatype of stars is inferred from the function
// double()'s input parameter signature.

fn example_1() {
    fn double_num(num: u128) -> u128 {
        num * 2
    }

    let stars = 10;  // Now this is of type 'u128' too

    println!("{:?}", stars);
}

// When there is no context for primitive types, Rust will fall back to i32
// for untyped integer literals and f64 for untyped floating literals.

fn example_2() {
    let integer = 10;  // This is of type 'i32'
    let float = 1.2;   // This is of type 'f64'
}


// TYPE SIGNATURE
//
// We can manually annotate types by providing a type signature. Type signatures
// are declared with : Type placed after the variable name and before the
// assigning = :

fn example_3() {
    let small_integer: u16 = 28;

    fn double(num: u128) -> u128 {
        num * 2
    }

    let unsigned_int: u8 = 28;
}


// SHADOWING
// 
// We can assign a new value to the same variable name within the same scope. 
// This is called shadowing and does not alter the original assignment:

fn example_4() {
    let favorite = "orange";
    println!("{favorite}");

    let favorite = "cerulean";
    println!("{favorite}");

    let favorite = "yellow";
    println!("{favorite}");
}

// Shadowing a variable will always allocate memory for the new variable. 


// PATTERN BINDING
//
// let statements accept a pattern on the left-hand side of the = operator. This
// means we can bind multiple variables in a single let statement using a tuple:

fn example_5() {
    let (a, b) = (10, "pie");
}

// We can also construct an array while declaring variables for each member:

fn example_6() {
    let [noun, verb, adjective] = ["arrays", "are", "homogeneous"];
}


// UNUSED VARIABLES
//
// The Rust compiler will give us warnings anytime we have unused variables. We 
// can tell the compiler to not check this requirement by prefixing a variable
// name with _:

fn example_7() {
    let _unused = "never";
    let _used = "sometimes";

    println!("{_used}");
}
