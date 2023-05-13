struct Happening {
    name: String,
    description: String,
    year: u32,
}

trait Summary {
    fn summarize(&self) -> String;
}

impl Summary for Happening {
    fn summarize(&self) -> String {
        format!("{} happened in {} - {}", self.name, self.year, self.description)
    }
}

fn main() {
    let snus_slutt = Happening {
        name: "Sluttet med snus.".to_owned(),
        description: "Etter mange år, sluttet jeg rett og slett på dagen.".to_owned(),
        year: 2022,
    };

    let trening = Happening {
        name: "Trenings rutine".to_owned(),
        description: "Etter sukksessull snusslutt 13 mai i fjor, la oss prøve innføre en annen sunn rutine 13 mai i år:)".to_owned(),
        year: 2023,
    };

    let snus = snus_slutt.summarize();
    let tren = trening.summarize();

    println!("{}", snus);
    println!("{}", tren);
}





