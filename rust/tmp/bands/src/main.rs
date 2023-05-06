use std::fs::File;
use std::io::prelude::*;
use std::io;

struct Artist {
    name: String,
    album: String,
}


fn main() {
    let mut name = String::new();
    println!("Enter band/artist name: ");
    io::stdin().read_line(&mut name).expect("Failed to read line");

    println!("Enter album name: ");
    let mut album = String::new();
    io::stdin().read_line(&mut album).expect("Failed to read line");

    let mut band = Artist {
        name: name,
        album: album,
    };

    // Create a new file, or truncate the existing one
    let mut file = File::create("output.txt");

    let entry = format!("{} - {}", band.name, band.album);

    // Write the band name to the file!
    file.expect("Error").write_all(entry.as_bytes());
}


