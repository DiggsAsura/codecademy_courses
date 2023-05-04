struct Msg {
    id: i32,
    text: String,
}

trait MsgHandler {
    fn handle(&self, msg: &Msg);
}

impl MsgHandler for Msg {
    fn handle(&self, msg: &Msg) {
        println!("{}: {}", msg.id_to_string(), msg.text);
    }
}

impl Msg {
    fn id_to_string(&self) -> String {
        self.id.to_string()
    }
}

fn main() {
    let msg = Msg {
        id: 1,
        text: "Hello, world!".to_string(),
    };
    msg.handle(&msg);
}
