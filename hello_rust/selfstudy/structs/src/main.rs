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
    let player3 = Player { name: String::from("Sarah"), ..player1 }; // very nice ..player1
    let combined_level: u8 = player1.level + player2.level;

    println!("Hello {} and {}!", player1.name, player2.name);
    println!("Your combined level is currently {combined_level}");  // So this works, but not
                                                                    // player1.name
    // Below is cool. 
    println!("{}, has the same stats as {}! F.x the level {} and the job {}.", player3.name, player1.name, player3.level, player3.job);

    // But did it eat player1.job f.x? 
//    println!("{}", player1.job);
    // UPPS, this value was moved. String does not implement the Copy trait. Bummer. 

    println!("But the level should be ok, no? {}", player1.level); // yup, works. u8 implements the
                                                                   // copy trait. 


}

