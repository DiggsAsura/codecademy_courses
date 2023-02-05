struct Api {
    count: usize,
}

impl Api {
    fn some_method(&mut self) {
        // increment count
        // rest of the method..
        self.count += 1;
        println!("count: {}", self.count);
    }
}

fn main() {
    let mut api = Api { count: 0 };
    api.some_method();
}
