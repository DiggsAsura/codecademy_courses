<?php
function addX ($param) {
    $param .= "X\n";
    echo $param;
}

$str = "Hello";
addX($str);
echo $str . "\n"; // remains "Hello"

// -----

function addXPermanently (&$param) {
    $param .= "X\n";
    echo $param;
};

$word = "Hello";
addXPermanently($word);
echo $word . "\n"; // now it's "HelloX"


// Is this the exact opposite of Rust?
// ok so it does in fact do the same thing in Rust.
/*
//translate the functionaddXPernamently(&param)into Rust
fn add_x_permanently(param: &mut String) {
    param.push_str("X\n");
    println!("{}", param);
}

fn main() {
    let mut word = String::from("Hello");
    add_x_permanently(&mut word);
    println!("{}", word);
}
*/
