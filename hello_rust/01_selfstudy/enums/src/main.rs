// Same, neeeeed to get into enums too
#[derive(Debug)]
enum Jobs {
    Warrior,
    Thief,
    Ninja,
    Paladin,
    WhiteMage,
}

struct Player {
    name: String,
    job: Jobs,
}

trait Present {
    fn present(&self) -> String {
        String::from("Just testing")
    }
}

impl Present for Player {}


fn main() {
    let player = Player {
        name: String::from("DiggsAsura"),
        job: Jobs::Warrior,
    };

    println!("{} has job: {:?}", player.name, player.job);

    match player.job {
        Jobs::Warrior => println!("Job is Warrior"),
        Jobs::Thief => println!("Job is Thief"),
        Jobs::Ninja => println!("Job is Ninja"),
        Jobs::Paladin => println!("Job is Paladin"),
        Jobs::WhiteMage => println!("Job is WhiteMage"),
    };
    
    println!("{}", player.present());
}
