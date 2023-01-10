// importing module
mod common;

#[test]
fn test_add() {
    // using commonn code
    common::setup();
    assert_eq!(adder::add(3, 2),5);
}
