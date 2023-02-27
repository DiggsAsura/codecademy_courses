use std::sync::Mutex;

fn main() {
    let mut data = Vec::new();
    let mx: Mutex = Mutex::new();
    {
        let _guard = mx.lock();
        data.push(0);
    }
}
