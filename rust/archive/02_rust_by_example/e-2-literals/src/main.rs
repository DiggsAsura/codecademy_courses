/* Literals
 * ==========
 *
 * Numeric literals can be type annotated by adding the type as a suffix. As an example, to specify
 * that the literal 42 should have the type i32, write 42i32.
 *
 * The type of unsuffixed numeric literals will depend on how they are used. If no constraints
 * exists, the compiler will use i32 for integers, and f64 for floating-point numbers. */

fn main() {
    // Suffixed literals, their types are known at initialization
    let x = 1u8;
    let y = 2u32;
    let z = 3f32;

    // Unsuffixed literals, their types depend on how they are used
    let i = 1;
    let f = 1.0;

    let k = f64::MAX;

    // 'size_of_val' returns the size of a variable in bytes
    println!("size of 'x' (u8) in bytes: {}", std::mem::size_of_val(&x));
    println!("size of 'y' (u32) in bytes: {}", std::mem::size_of_val(&y));
    println!("size of 'z' (f32) in bytes: {}", std::mem::size_of_val(&z));
    println!("size of 'i' (i32) in bytes: {}", std::mem::size_of_val(&i));
    println!("size of 'f' (f64) in bytes: {}", std::mem::size_of_val(&f)); 
    println!("size of 'k' {} (f64::MAX) in bytes: {}", k, std::mem::size_of_val(&k)); 
}

/* There are some concepts used in the previous code that haven't been explained yet, here's a
 * brief explanation for the impatient readers:
 *
 * std::mem::size_of_val is a function, but called with its full path. Code can be split in logical
 * units called modules. In this case, the size_of_val function is defined in the mem module, and
 * the mem module is defined in the std crate. For more details, see modules and crates articles.
