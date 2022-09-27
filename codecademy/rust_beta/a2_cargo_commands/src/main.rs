fn main() {
    println!("Cargo commands: \n");

    println!("cargo new              # Create a new binary executeable crate");
    println!("cargo new --lib        # Create a new library crate");
    println!("");
    println!("cargo build            # Compiles our crate");
    println!("cargo build --release  # Compiles our crate with optimizations");
    println!("cargo run              # Compiles our crate and runs the compiled executeable");

    println!("cargo test             # Run all tests in a crate");
    println!("cargo doc --open       # Build and open our crate's documentation in a web browser");
    println!("cargo clean            # Cleans up temporary files created during compilation");
    println!("cargo publish          # Publish you crate to 'crates.io'");
    println!("");

    println!("cargo install          # Install a binary directly from crates.io");
}
