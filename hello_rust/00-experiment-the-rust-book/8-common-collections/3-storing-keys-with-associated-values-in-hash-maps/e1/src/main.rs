fn main() {
    let mut numbers = vec![2, 7, 11, 3, 55, 102, 23, 23, 30, 1, 0];
    numbers.sort();
    println!("{:?}", numbers);

    // output of numbers: [0, 1, 2, 3, 7, 11, 23, 23, 30, 55, 102]

    let median = numbers.get(numbers.len() / 2).unwrap();
    println!("The median is {}", median);

    use std::collections::HashMap;
    let mut occurances = HashMap::new();
    for number in numbers {
        let count = occurances.get(&number).unwrap_or(&0);
        occurances.insert(number, count +1);
    }
    println!("{:?}", occurances);
}
