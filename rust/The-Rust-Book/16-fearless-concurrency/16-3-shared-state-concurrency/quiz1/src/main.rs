use std::sync::Mutex;

fn main() {
    let mut data = Vec::new();
    let mx: Mutex = Mutex::new();
    {
        let _guard = mx.lock();
        data.push(0);
    }
}


// Quiz:
// Which of the following best describes why Rust uses Mutex<T> instead of just Mutex?
//
// To prevent accessing a mutex's data without locking the mutex
//
//
// Context: The Mutex<T> design ensures that a mutex's data can only be accessed when the mutex is
// locked, and conversely that the mutex is unlocked once the data is no longer accessible.
