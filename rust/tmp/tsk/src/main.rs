struct Tsk {
    name: String,
    priority: u32,
    stack: [u8; 1024],
}

impl Tsk {
    fn new(name: &str, priority: u32) -> Tsk {
        Tsk {
            name: name.to_string(),
            priority: priority,
            stack: [0; 1024],
        }
    }
}

fn main() {
    let tsk1 = Tsk::new("tsk1", 1);
    let tsk2 = Tsk::new("tsk2", 2);
    let tsk3 = Tsk::new("tsk3", 3);

    println!("tsk1: {}, {}, {:?}", tsk1.name, tsk1.priority, tsk1.stack);
}
