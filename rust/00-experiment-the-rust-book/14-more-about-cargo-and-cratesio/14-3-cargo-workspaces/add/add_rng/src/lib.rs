use rand::Rng;

pub fn add_rng(x: i32) -> i32 {
    let mut rng = rand::thread_rng();
    let y: i32 = rng.gen();
    x + y
}

