fn match_thingy(age: u16) {
    match age {
        0           => println!("Not yet had my bd!"),
        n @ 1..=12  => println!("In my first years: {n}"),
        n @ 13..=19 => println!("In my teens {n}"),
        n @ 20..=50 => println!("Getting older... ish {n}"),
        n => println!("Old af"),
    }
}
fn main() {
    println!("A pretty neat feature for sure! Binding let you f.x refer to a number in a range!");
    
    match_thingy(12);
    match_thingy(0);
    match_thingy(100);
    match_thingy(22);

}
