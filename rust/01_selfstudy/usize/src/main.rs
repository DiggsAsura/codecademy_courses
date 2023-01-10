const MY_USIZE: usize   = usize::MAX;
const MY_U128: u128     = u128::MAX;
const MY_U64: u64     = u64::MAX;

fn main() {
    
    let my_usize    = MY_USIZE.to_string(); 
    let my_u128     = MY_U128.to_string();
    let my_u64      = MY_U64.to_string();

/*    match my_usize {
        my_u128 => println!("matched 128"),
        my_u64  => println!("matched 64"),
    };
*/
    // Match just does not work
    
    if my_usize == my_u128 {
        println!("matched u128");
    } else if my_usize == my_u64 {
        println!("matched u64");
    } else {
        println!("No match");
    }


    /*
    let my_u32      = u32::MAX.to_string();
    let my_u16      = u16::MAX.to_string();
    let my_u8       = u8::MAX.to_string(); 
    
    println!("usize:    {my_usize}");
    println!("u128:     {my_u128}");
    println!("u64:      {my_u64}");
    println!("u32:      {my_u32}");
    println!("u16:      {my_u16}");
    println!("u8:       {my_u8}");
    
    // Match
    match MY_USIZE {
        MY_U128 => println!("usize mathed u128"),
        MY_U64  => println!("usize mathed u64"),
        my_u32  => println!("usize mathed u32"),
        my_u16  => println!("usize mathed u16"),
        my_u8   => println!("usize mathed u8"),
        _       => println!("no match"),
    };
    */


    // Apparently just forget about the match
}
