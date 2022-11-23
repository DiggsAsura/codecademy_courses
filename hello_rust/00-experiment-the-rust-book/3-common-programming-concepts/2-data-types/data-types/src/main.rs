#![allow(unused_variables)]
#![allow(dead_code)]
#![allow(unreachable_patterns)]

fn main() {
//    let to_string: String = 42i32.to_string();
//    println!("{to_string}");

//    let guess: u32 = "42".trim().parse().expect("Not a number");
//    println!("{guess}");

    ex1();      // Scalar Types
    ex2();      // Integers 
    ex3();      // Number literals
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

    // isize usize
    let my_size = usize::MAX;
    println!("max usize: {my_size}");

    let max_u128: u128 = u128::MAX;
    println!("max u128: {max_u128}");

    let max_u64: u64 = u64::MAX;
    println!("max u64:  {max_u64}");
    
    let max_u32: u32 = u32::MAX;
    println!("max u32:  {max_u32}");
    
    let max_u16: u16 = u16::MAX;
    println!("max u16:  {max_u16}");


    let usize_str:  String = my_size.to_string();
    let u128_str:   String = max_u128.to_string();
    let u64_str:    String = max_u64.to_string();
    let u32_str:    String = max_u32.to_string();
    let u16_str:    String = max_u16.to_string();
    let u8_str:     String = my_u8_max.to_string();

    match usize_str {
        u128_str    => println!("usize is same as u128"),
        u64_str     => println!("usize is same as u64"),
        u32_str     => println!("usize is same as u32"),
        u16_str     => println!("usize is same as u16"),
        u8_str      => println!("usize is same as u8"),
    }

}


fn ex2() {      // wtf. why is usize changing? 
    let max_usize: String   = usize::MAX.to_string();
    let max_u64: String     = u64::MAX.to_string();
    let max_u128: String    = u128::MAX.to_string();

    println!("\n");
    println!("Ex2");
    println!("usize {max_usize} vs u64 {max_u64}");
    println!("usize {max_usize} vs u128 {max_u128}");


    match max_usize {
        max_u128    => println!("Same as u128"),
        max_u64     => println!("Same as u64"),
        _           => println!("Neither"),
    }

    println!("WTf why is it u128??!?!?!?!?!?!?!?!?!?!???!?!?!!?!? It's obviously 64!?");
    println!("Testing a normal match statement");
    
    let a = 2;

    match a {
        3   => println!("nope"),
        2   => println!("nope"),
        1 => println!("bingo"),
        _ => println!("nope"),
    }
}


fn ex3() {      // Number literals

    println!(r" 
                Number literals         | Example
                ------------------------|-------------
                Decimal                 | 09_222
                Hex                     | 0xff
                Octal                   | 0o77
                Binary                  | 0b1111_0000
                Byte (u8 only)          | b'A'

                ");

}

