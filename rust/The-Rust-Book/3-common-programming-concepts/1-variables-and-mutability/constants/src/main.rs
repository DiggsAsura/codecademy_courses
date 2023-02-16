// Constants and immutable variables are similar but Constatns differs a bit:
//  - Always immutable, can not change
//  - const can be declared in ANY scopes, even global. 
//  - const can be set to a constant expression, not the result of a value that could only be
//  computed at runtime. 

const THREE_HOURS_IN_SECONDS: u32 = 60 * 60 * 3;

fn main() {
    println!("{THREE_HOURS_IN_SECONDS}");
}

// NAMING_CONVETION

