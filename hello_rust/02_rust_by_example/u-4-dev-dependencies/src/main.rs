/* Developement dependencies
 * ===========================
 *
 * Sometimes there is a need to have dependencies for tests (or examples, or benchmarks) only. 
 * Such dependencies are added to Cargo.toml in the [dev-dependencies] section. These dependencies
 * are not propagated to other pagckages which depends on this package. 
 *
 * One such example is pretty_assertions, which extends standard assert_eq! and assert_ne! macros,
 * to provide coloruf diff.
 *
 * // Cargo.toml - going on to edit that
 */
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;
    use pretty_assertions::assert_eq; // crate for test-only use. Cannot be used in non-test code.

    #[test]
    fn test_add() {
        assert_eq!(add(2, 3), 5);
    }
}

fn main() {
    println!("Hello, world!");
}
