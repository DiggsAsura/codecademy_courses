fn main() {
    let my_vec = vec!["one", "two", "three", "four", "five"];
    let my_vec_two = vec!["1", "2", "3", "4", "5"];

    for item in my_vec {
        println!("{item} from the first vec (my_vec)");
        for item_two in &my_vec_two { // for some reason they want &my_vec_two
            println!("{item_two} from the second vec (my_vec_two)");
        }
    }
}
