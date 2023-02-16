# Creating the second Package in the Workspace

Next, let's create another member package in the workspace and clal it **add_one**. Change the top-
level *Cargo.toml* to specify the *add_one* path in the **memebers** list:

Filename: Cargo.toml

[workspaces]

members = [
    "adder",
    "add_one",
]


Then generate a new library crate named **add_one**:

$ cargo new add_one --lib
    Created library 'add_one' package


Your *add* direcotyr should now have these directories and files:

├── Cargo.lock
├── Cargo.toml
├── add_one
│   ├── Cargo.toml
│   └── src
│       └── lib.rs
├── adder
│   ├── Cargo.toml
│   └── src
│       └── main.rs
└── target

In the *add_one/src/libr.rs* file, let's add an **add_one** function:

Filename: add_one/src/lib.rs

pub fn add_one(x: i32) -> i32 {
    x + 1
}


Now we can have the **adder** package with our binary depend on the **add_one** package that has our
library. First, we'll need to add a path dependency to **add_one** to *adder/Cargo.toml*.

Filename: adder/Cargo.toml

[dependencies]
add_one = { path = "../add_one" }

Cargo doesnt's assume that crates in a workspace will depend on each other, so we need to be
explicit about the dependency relationships.

Next, let's use the **add_one** function (from the **add_one** crate) in the **adder** crate. Open the
*adder/src/main.rs* file and add a **use** line at the top to bring the new **add_one** library crate into
scope. T-hen change the **main** function to call the **add_one** function, as in Listing 14-7.


Filename: adder/src/main.rs

use add_one;

fn main() {
    let num = 10;
    println!("Hellow World! {num} plus one is {}!", add_one::add_one(num));
}

Listing 14-7: Using the **add_one** library crate from the **adder** crate

Let's build the workspace by running **cargo build** in the top-level *add* directory!


$ cargo build
    Compiling add_one v0.1.0 (file:///projects/add/add_one)
    Compiling adder v0.1.0 (file:///projects/add/adder)
        Finished dev [unoptimized + debuginfo] target(s) in 0.68s

To run the binary crate from the *add* direcotyr, we can specify which package in the workspace we
want to run by using the -p argument and the package name with **cargo run**:


$ cargo run -p adder
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
        Running 'target/debug/adder'

Hello, world! 10 plus one is 11!


This runs the code in *adder/src/main.rs*, which depends on the **add_one** crate.
