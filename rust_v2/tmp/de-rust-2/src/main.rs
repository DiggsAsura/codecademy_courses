struct Player {
    name: String,
    health: u64,
    level: u8,
    strength: u8,
    dexterity: u8,
}

fn main() {
    let player = Player {
        name: String::from("Alexy"),
        health: 100,
        level: 1,
        strength: 1,
        dexterity: 1,
    };

    println!("Player name: {}", player.name);
}
