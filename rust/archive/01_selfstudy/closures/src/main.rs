#![allow(deprecated)]
#![allow(dead_code)]
struct Player {
    name: String,
    level: u8,
    class: Class,
    job: Jobs,
}

#[derive(Debug)]
enum Jobs {
    Warrior,
    Monk,
    Thief,
    WhiteMage,
    BlackMage,
    RedMage,
}

#[derive(Debug)]
enum Class {
    Hume,
    Elv,
    Mithra,
    Galka,
    Tarutaru,
}

trait Presentation {
    fn present(&self) -> String {
        format!("Why can't I call self.stuff here??")
    }
}

impl Presentation for Player {}

fn main() {
    let mut player = Player {
        name: String::from("DiggsAsura"),
        level: 1,
        class: Class::Tarutaru,
        job: Jobs::BlackMage,
    };

    println!("{:?}", player.present());

    //let player_info = || println!(
    //println!(
    let player_info: String = format!(
    "
    Name: {}
    Level: {}
    Class: {:?}
    Job: {:?}
    ", player.name, player.level, player.class, player.job);
   
   // println!("{} just killed the monster for some great 10000 experience points!", name);
    // And now the acutal closure...
    let mut lvl_up = |i: u8| while player.level <= 10-1 { 
        player.level += i; 
        std::thread::sleep_ms(100);
        println!("Ding! Lvl {}", player.level) };

    lvl_up(1);

    println!("Wow, {} is now level {} already! Let's go!", player.name, player.level);

    println!("{player_info}");
//    player_info();
}
