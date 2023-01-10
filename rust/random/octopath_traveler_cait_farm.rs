// Just a random script to print out the Cait strat

// Should have a Do you have have HC Or not. Maybe add later. 


fn main() {
    let cait_shield = 15;
    let cait_hp = 45;

    let viola_a = 4; // atk
    let hc_a = 3;    // atk
    let fiore_a = 3; // skill
    let scare_a = 4; // skill
    let round_one = viola_a + hc_a + fiore_a + scare_a;

    println!("Cait 15 shield\n");

    println!("ROUND 1");
    println!("----------");
    println!("Viola: 4 atk");
    println!("HC:    3 atk");
    println!("Fiora: 3 skill");
    println!("Scare: 4 skill");
    println!("---DMG dealt ---> {round_one}");
    println!("---Cait shield: {:?}", cait_shield-round_one);
    let cait_hp = cait_hp - round_one;
    println!("---Cait HP: {cait_hp}");


    println!("\n----------------------\n");


    println!("ROUND 2 - HC Break now!");
    println!("------------------------");
    println!("Viola:  3 skill");
    println!("HC:     1 JAB");
    println!("Fiore:  4 atk");
    println!("Scare:  4 atk");   
    let round_two = 3 + 1 + 4 + 4;
    println!("---DMG dealt ---> {round_two}");
    let cait_hp = cait_hp - round_two;
    println!("---Cait HP: {cait_hp}");
    
    
    println!("\n-----------------------\n");


    println!("ROUND 3 - Remember ALLI!!!");
    println!("----------------------------");

    println!("Carry1: 4 atk");
    println!("Carry2: 4 atk");
    println!("Carry3: 4 atk");
    println!("Carry4: 4 atk");
    println!("ALLI!!!: 3 atk");
    let round_three = 4 + 4 + 4 + 4 + 3;
    println!("---DMG dealt ---> {round_three}");
    let cait_hp = cait_hp - round_three;
    if cait_hp <= -1 {
        println!("---Overkill! Cait HP: {cait_hp}");
    } else {
        println!("---Kill! Cait HP:{cait_hp}");
    }

}
