// shadowing using the let keyword
fn main() {
    let x = 5;

    let x = x +1;

    {
        let x = x * 2;
        println!("The value of x in the inner scope is: {x}");
    }

    println!("The value of x is: {x}");


    {
        println!("Example 2, change types with shadowing");
        let spaces = "      ";
        let spaces = spaces.len();
        println!("Spaces: {spaces}");

        // Can not with mut spaces though! That will give error when compiling!
    }
}
