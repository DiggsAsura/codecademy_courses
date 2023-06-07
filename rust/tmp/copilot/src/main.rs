enum Jobs {
    Warrior,
    WhiteMage,
    BlackMage,
    Thief,
}

trait Abilities {
    fn attack(&self) -> u16;
    fn magic(&self) -> u16;
    fn special(&self) -> u16;
}

impl Abilities for Jobs {
    fn attack(&self) -> u16 {
        10
    }
    fn magic(&self) -> u16 {
        0
    }
    fn special(&self) -> u16 {
        0
    }
}

fn main() {
    let warrior = Jobs::Warrior;
    let white_mage = Jobs::WhiteMage;
    let black_mage = Jobs::BlackMage;
    let thief = Jobs::Thief;

    println!("Warrior attack: {}", warrior.attack());
    println!("White Mage attack: {}", white_mage.attack());
    println!("Black Mage attack: {}", black_mage.attack());
    println!("Thief attack: {}", thief.attack());
}
