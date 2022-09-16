use std::io::stdin;

fn main() {
    let mut choose = String::new();
    stdin().read_line(&mut choose).expect("Fail");
    println!("\nParis trip 2022\n");
    
    let choose = choose.trim().parse().unwrap();
    
    match choose {
        1 => day_one(),
        2 => day_two(),
        3 => day_three(),
        4 => day_four(),
        5 => day_five(),
        6 => day_six(),
        7 => day_seven(),
        8 => day_eight(),
        0 => {
            day_one();
            day_two();
            day_three();
            day_four();
            day_five();
            day_six();
            day_seven();
            day_eight();
        },
        _ => println!("Unknown"),
    };
}

fn day_one() {
    println!("Day 1, August 2. 2022");
    println!("Arrived at an appartment that smells bad. No AC and 30+ degrees even 2100 in the evening. Gonna change for a hotel tomorrow...\n");
}

fn day_two() {
    println!("Day 2, August 3. 2022");
    println!("Starting to headache. The appartement has really bad air. And no AC. We have booked another place. Trying to get some breakfest then we're out of here.");
    println!("Ending good in a new hotel. Able to get some sleep and relax in clean enviroment. Also close to Paris version of China town which is godsend for my GF!\n");
}

fn day_three() {
    println!("Day 3, August 4. 2022");
    println!("Had breakfest in the hotel. Super basic, but ok. Waiting on the girls, before we head to Disneyland!");
    println!("Fantastic day in Disneyland. See a lot of the park, and also did three-four rides. Good times.\n");
}

fn day_four() {
    println!("Day 4, August 5, 2022");
    println!("Went to Louvre, then made our way up throgh Chans Elyse (or how you write it)");
    println!("Also a tivoli in the park, so ended up taking tons of rides there too. For the kid this was awesome.");
    println!("Today too very warm! But def another good day!\n");
}

fn day_five() {
    println!("Day 5, August 6, 2022");
    println!("Plan for the day, Eiffel Tower and a shoppeing mall. No feet can walk too much today, even the kid needed massage from her mother last night.");
    println!("Yet another great day. Eiffel and shopping center mostly, but not much more to expect with a kid. That being said, she's making it really easy going on a trip! Oh and bought some new Nike Air Max. Not the ones I have been looking for but I'm still happy. \n");
}

fn day_six() { 
    println!("Day 6, August 7, 2022");
    println!("Starting the day with going out to bring the girls some premade breakfest from a local bakery. The kid of course didnt like any of it, and GF gives me a hard time for poor choice for kid. Haha. Great start..");
    println!("Stayed in the hotel area (Choisey) whole day, and it was really worth it. The China Town is really really good here!");
    println!("");
}

fn day_seven() {
    println!("Day 7, August 8, 2022");
    println!("GF going out to buy us a good breakfest. Last full day coming up. Going boat and a park.");
    println!("Met GF's friend and kid, went for lunch together in Opera area. Very nice japaneese resturant. Later, kiddo got to choose where to eat");
    println!("dinner, so she went with the very first place we was, an asian style buffet right by the hotel. She like too much pick up her own dinner!");
    println!("Besides that, pretty lazy day. Preparing to leave tomorrow.");
    println!("");        
}

fn day_eight() {
    println!("Day 8, August 9, 2022");
    println!("Amazing trip. Amazing family <3");
    println!("Me and the kid went to the tivoli a few hours while GF got a feet massage. Dinner on the airplane and got back home midnight.");
    println!("Very nice trip overall, with 30+ degrees every day!");
    println!("");
}
