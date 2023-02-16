fn main() {
    
    fn double_first(vec: Vec<&str>) -> i32 {
        let first = vec.first().unwrap();
        2 * first.parse::<i32>().unwrap()
    }

    let my_vec = vec!["20", "30", "40"];
    
    println!("{}", double_first(my_vec));
}
