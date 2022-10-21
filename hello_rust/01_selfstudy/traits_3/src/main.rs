// OK, doing some more structs and traits. 

pub struct Player {
    name: String,
    class: String,
    job: String,
    lvl: u8,       // max 255
    hp: u16,
    mp: u16,
    atk: u16,
}

pub trait Representation {
    fn repr(&self) -> String {
//        String::from("{}", self.name)     This won't work apparently
       format!("This is a default trait thingy")
    }
}

impl Representation for Player {}

fn main() {
    let player = Player {
        name: String::from("Diggs"),
        class: String::from("Taru"),
        job: String::from("Black Mage"),
        lvl: 1,
        hp: 15,
        mp: 20,
        atk: 10,
    };

    println!("Hello, {}!", player.name);
    println!("{}", player.repr());
    println!("Seems like it's a bit tricky to use struct fields inside a trait");
}
