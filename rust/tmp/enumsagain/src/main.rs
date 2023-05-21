enum Job {
    Warrior,
    Monk,
    Thief,
    RedMage,
    WhiteMage,
    BlackMage,
}

impl Job {
    fn get_name(&self) -> &str {
        match self {
            Job::Warrior => "Warrior",
            Job::Monk => "Monk",
            Job::Thief => "Thief",
            Job::RedMage => "Red Mage",
            Job::WhiteMage => "White Mage",
            Job::BlackMage => "Black Mage",
        }
    }
}

struct Character {
    name: String,
    job: Job,
    level: u8,
    hp: u16,
    mp: u16,
    strength: u8,
    dexterity: u8,
    intelligence: u8,
    mind: u8,
    luck: u8,
}

struct Monster {
    name: String,
    level: u8,
    hp: u16,
    mp: u16,
    strength: u8,
    dexterity: u8,
    intelligence: u8,
    mind: u8,
    luck: u8,
}

fn main() {
    let mut player1 = Character {
        name: String::from("Cloud"),
        job: Job::Warrior,
        level: 1,
        hp: 100,
        mp: 0,
        strength: 10,
        dexterity: 10,
        intelligence: 10,
        mind: 10,
        luck: 10,
    };

    let mut monster1 = Monster {
        name: String::from("Goblin"),
        level: 1,
        hp: 100,
        mp: 0,
        strength: 10,
        dexterity: 10,
        intelligence: 10,
        mind: 10,
        luck: 10,
    };

    println!("{} is a {}.", player1.name, player1.job.get_name());
    println!("Level {}.\n", player1.level);

    println!("{} is a {}.", monster1.name, monster1.level);
}

