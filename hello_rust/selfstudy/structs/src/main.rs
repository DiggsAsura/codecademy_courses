// I'm not sure how to use Structs. I have no clear vision on how to use them. 
// Probably because of my inexperience with programming as a whole. But I feel Structs, and 
// also Traits gonna be extremly important to get around. 
#![allow(dead_code)]
struct Player {
    name: String,
    level: u8,
    job: String,
}

fn main() {
    let player1 = Player { name:"Kenneth".to_string(), level:10, job:"Warrior".to_string() };
    let player2 = Player { name: "Kayi".to_string(), level: 12, job: "Wifu".to_string() };

    println!("Hello {} and {}!", player1.name, player2.name);
    
    let combined_level: u8 = player1.level + player2.level;

    println!("Your combined level is currently {combined_level}");  // So this works, but not
                                                                    // player1.name
}

