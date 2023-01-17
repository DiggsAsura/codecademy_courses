# Customizing Builds with Release Profiles

In Rust, *release profiles* are predefined and customizable profiles with different configurations that
allow a programmer to have more control over various options for compiling code. Each profile is
configured independently of the others.

Cargo has two main profiles: the **dev** profile Cargo uses when you run **cargo build** and the
**release** profile Cargo uses when you run **cargo build --release**. The **dev** profile is defined with
good deafaults for development, and the **release**  profile has good defaults for release builds.

These profile names might be familiar from the output of your builds:

$ cargo build
    Finished dev [unoptimized + debuginfo] target(s) in 0.0s
$ cargo build --release
    Finished release [optimized] target(s) in 0.0s


The **dev** and **release** are these different profiles used by the compiler.

Cargo has default settings for each of the profiles that apply when you haven't explicitly added any
**[profile.*]** sections in the project's *Cargo.toml* file. By adding **[profile.*]** sections for any
profile you want to customize, you override any subset of the default settings. For example, here are the
default values for the **opt-level** setting for the **dev** and **release** profils:

Filename: Cargo.toml

**[profile.dev]**
**opt-level = 0**

**[profile.release]**
**opt-level = 3**


