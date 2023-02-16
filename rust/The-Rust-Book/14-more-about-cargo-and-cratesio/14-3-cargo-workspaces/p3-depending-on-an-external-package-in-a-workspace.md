# Depending on an External Package in a Workspace

Notice that the workspace has only one *Cargo.lock* file at the top level, rather than having a
*Cargo.lock* in each crate's directory. This ensures that all crates are using the same version of all
dependencies. If we add the **rand** package to the *adder/Cargo.toml* and *add_one/Cargo.toml* files,
Cargo will resolve both of those to one version of **rand** and record that in the one *Cargo.lock*.
Making all crates in the workspace use the same dependencies means the crates will always be
compatible with each other. Let's add the **rand** crate to the **[dependencies]** section in the
*add_one/Cargo.toml* file so we can use the **rand** crate in the **add_one** crate:


Filename: add_one/Cargo.toml

[dependencies]
rand = "0.8.5"


We can now add **use rand;** to the *add_one/src/lib.rs* file, and building the whole workspace by
running **cargo build** in the *add* directory will bring in and compile the **rand** crate. We will get one
warning because we aren't referring to the **rand** we bought brought into scope:


$ cargo build
    Updating crates.io index
  Downloaded rand v0.8.5
  -- snip --
  Compiling rand v0.8.5
  Compiling add_one v0.1.0 (file:///projects/add/add_one)
warning: unused import: 'rand'
 --> add_one/src/lib.rs:1:5
  |
1 | use rand;
  |     ^^^^
  |
  = note: '#[warn(unused_imports)]' on by default

warning: 'add_one' (lib) generated 1 warning
    Compiling adder v0.1.0 (file:///projects/add/adder)
      Finished dev [unoptimized + debuginfo] target(s) in 10.18s


The top-level *Cargo.lock* now contains information about the dependency of **add_one** on **rand**.
However, even though **rand** is used somewhere in the workspace, we can't use it in other crates in
the workspace unless we add **rand** to their *Cargo.toml* files as well. For example, if we add **use rand;**
to the *adder/src/main.rs* file for the **adder** package, we'll get an error:


$ cargo build
  --snip--
  Compiling adder v0.1.0 (file:///projects/add/adder)
error[E0432]: unresolved import 'rand'
 --> adder/src/main.rs:2:5
  |
2 | use rand;
  |     ^^^^ no external crate `rand`


To fix this, edit the *Cargo.toml* file for the **adder** package and indicate that **rand** is a dependency for
it as well. Building the **adder** package will add **rand** to the list of dependencies for **adder** in
*Cargo.lock*, but no additional copies of **rand** will be downloaded. Cargo has ensured that every crate
in every package in the workspace using the **rand** package will be using the same version, saving us
space and ensuring that the crates in the workspace will be compatible with each other.
