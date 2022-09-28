fn main() {
    println!("This blows my mind, but prinln! does not require semicolon");
    println!("Hello, world!"); // OK so the LAST statement (println) does not need semicolon ;
    let answer = expressions();
    println!("{answer}");
    
//    patterns();
    println!("{:?}", patterns());
}

fn expressions() -> String {
    let answer = "this is an expression".to_string();
    answer
}

fn patterns() -> i32 {
    let (x, y) = (5, 10);
    println!("{x}");
    println!("{y}");
    return x+y
}

