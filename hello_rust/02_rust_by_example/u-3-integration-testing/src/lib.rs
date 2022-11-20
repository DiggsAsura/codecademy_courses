// Define this in a crate called 'adder'
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[test]
fn test_add() {
    assert_eq!(adder::add(3,2), 5);
}
