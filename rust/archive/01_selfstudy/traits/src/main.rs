#![allow(deprecated)]
// Ok I somewhat got the hunch about structs, now I need traits and how to implement them into
// structs.. 

pub struct Player { // Unsure if I need pub
    name: String,
    level: u8,
    job: String,
}

pub struct Monster {
    name: String,
    level: u8,
    job: String,
}

// Trying the most basic of basic I guess. Making a method that can be implemented into several
// traits. 
pub trait Presentation {
    fn information(&self) -> String; // REmember &self
    fn presentate(&self) -> String {
        String::from("Just a string nothing more.")
    }
}

// The impl might actually be the harder part!
impl Presentation for Player {
    fn information(&self) -> String {
        format!("Name: {} \nLevel: {}\nJob: {}", self.name, self.level, self.job)
    }
//    fn presentate(&self) -> String {
//        format!("{:?}", self)
//    }
}

impl Presentation for Monster {
    fn information(&self) -> String {
        format!("Name: {}\nLevel: {}\nJob: {}", self.name, self.level, self.job)
    }
}

fn main() {
    let player_1 = Player {
        name: String::from("Diggs"),
        level: 8,
        job: String::from("Warrior"),
    };

    let monster_1 = Monster {
        name: String::from("Nidhogg"),
        level: 99,
        job: String::from("Paladin"),
    };

    println!("{} enters Dragon's Aery", player_1.name);
    std::thread::sleep_ms(1000);
    println!("{} stands in front of you!!", monster_1.name);
    
    std::thread::sleep_ms(300);
    println!("....");
    std::thread::sleep_ms(2000);

    println!("This looks bad... Scanning {} information...", monster_1.name);

    println!("\n{}\n", monster_1.information());

    println!("Rip... Comparing to my own stats...");
    println!("\n{}\n", player_1.information());

    println!("{}", player_1.presentate());

}


