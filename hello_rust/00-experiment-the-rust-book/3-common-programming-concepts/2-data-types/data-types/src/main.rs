fn main() {
//    let to_string: String = 42i32.to_string();
//    println!("{to_string}");

//    let guess: u32 = "42".trim().parse().expect("Not a number");
//    println!("{guess}");

    ex1();      // Scalar Types
}

fn ex1() {          // Saclar Types
    // A scalar type represents a single value. Rust has four primary scalar types: integers,
    // floating-point numbers, Booleans, and characters. You may recognize these from other
    // programming languages.

    // Integer Types
    //
    // Length       Signed      Unsigned
    // 8-bit        i8          u8
    // 16-bit       i16         u16
    // 32-bit       i32         u32
    // 64-bit       i64         u64
    // 128-bit      i128        u128
    // arch         isize       usize
    //

    let base: u16 = 2;   // base.powe(8) will overflow, -1 does not care. so have to use u16
    let my_u8 = base.pow(8)-1;
    println!("my_u8: {my_u8}");

    let my_u8_max: u8 = u8::MAX;
    println!("my_u8_max: {my_u8_max}");

}
