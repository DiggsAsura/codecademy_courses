/* The infamous pig calculator!
 *
 * Half your age + 7... The classic check if your a pig or not for dating this chick. */

#[derive(Clone, Copy)]
struct Person {
    name: &'static str,
    age: u8,
}

impl Person {
    fn present(&self) {
        println!("My name is {}, and I'm {} years old!", self.name, self.age);
    }
}

fn age_diff(a: Person, b: Person) -> u8 {
    a.age - b.age
}

// The fabolous pig calculator
fn pig_calc(a: Person, b: Person) -> bool {
    if (a.age / 2 + 7) >= b.age {
        true
    } else {
        false
    }
}

fn main() {
    println!("Welcome to the Pig Calculator!\n");

    // Person 1 - the older person, Person 2 - the younger person
    let person_1 = Person { name: "Diggs", age: 38 };
    let person_2 = Person { name: "GF", age: 31 };
    person_1.present();
    person_2.present();

    // Age difference bool
    let age_difference = age_diff(person_1, person_2);
    println!("\nThat means the age difference between {} and {} is {} years...", person_1.name, person_2.name, age_difference);
    
    // Treshhold
    let treshhold = person_1.age / 2 + 7;
    println!("{}, your GF needs to be at least {} years old for YOU to avoid being a pig you know?", person_1.name, treshhold);

    // The pig checker
    let answer = pig_calc(person_1, person_2);
    println!("\nAre you a pig: {}", answer);

    // Safety net
    let safety = person_2.age - treshhold;
    println!("Looks like you are {} years safe!", safety);
    
}
