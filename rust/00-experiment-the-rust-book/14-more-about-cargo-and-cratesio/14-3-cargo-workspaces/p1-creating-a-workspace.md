# Creating a Workspace

A *workspace* is a set of packages that shre the same *Cargo.lock* and output directory. Let's make a
project using a workspace - we'll use trivial code so we can concentrate on the structure of the
workspace. There are multiple ways to structure a worksapce, so we'll just show one commone way.
We'll ahve a workspace containing a binary and two libraries. The binary, which will provide the main
functionality, will depend on the two libraries. One library will provide an **add_one** function, and a
second library an **add_two** function. These three crates will be part of the same workspace. We'll
start by creating a new directory for the workspace:

$ mkdir add
$ cd add


Next, in the *add* directory, we create the *Cargo.toml* file that will configure the entire workspace. This
file won't have a **[package]** section. Instead, it will start with a **[workspace]** section that will allow
us to add members to the workspace by specifying the path to the package with our binary crate; in
this case, that path is *adder*:

Filename: Cargo.toml


