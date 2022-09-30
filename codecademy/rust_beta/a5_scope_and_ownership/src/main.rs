fn main() {

    println!("{:?}", p1_blocks());
    println!("{:?}", sum());    

    // This part is supposed to work, following Rust Beta course but it's not
    // really doing that or..?
    //let sum = {
    //    let number_1 = 111;
    //    let number_2 = 222;
    //    number_1 + number_2;
    //};
    //println!("{:?}", sum);
}


fn p1_blocks() -> i32 {

    // In Rust, code can be separated into blocks. A block of code is a 
    // collection of statements and an optional expression contained with
    // {}:

    // Statement block
    {
        let number_1 = 11;
        let number_2 = 31;
        let sum = number_1 + number_2;
        println!("{sum}");
    }

    // Expression block
    {
        let number_1 = 1;
        let number_2 = 2;
        number_1 + number_2
    }

    // Blocks can be treated as the single statement or expression they evaluate
    // to. This means we can assign variables to a block of code:

//    let sum = {
//        let number_1 = 11;
//        let number_2 = 200;
//        number_1 + number_2
//    };
//    println!("{sum}");

}

fn sum() -> i32 {
    let number_1 = -11;
    let number_2 = -12;
    number_1 + number_2
}

