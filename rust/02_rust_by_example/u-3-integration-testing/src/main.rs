/* Integration testing
 * ===================
 *
 * Unit tests are testing one module in isolation at the time: they're small and can test private
 * code. Integration tests are external to your crate and use only its public interface in the same
 * way any other code would. Their purpose is to test that many parts of your library work
 * correctly together. 
 *
 * Cargo looks for integration tests in tests directory next to src.
 *
 * File src/lib.rs 
 */

/* Each Rust source file in the tests directory is compiled as a separate crate. In order to share
 * some code between integration tests we can make a module with public functions, importing and
 * using it within tests. */

/* File tests/common/mod.rs */

fn main() {
    println!("Hello, world!");
}

/* Creating the module as tests/common.rs also works, but is not recommended because the test
 * runner will treat the file as a test crate and try to run tests inside it. */
