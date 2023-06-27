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

//
// If we DO want to make permanent changes to a variable within a function,
// we can prepend the parameter name with the reference sign (&). In this way,
// we assign the parameter to be an alias for the argument variable. Both will
// refer to the same spot in memory, and changes to the parameter within the
// function will permanently affect the argument variable.
//


// the actual task

$string_one = "you have teeth";
$string_two = "toads are nice";
$string_three = "brown is my favorite color";

function convertToQuestion(&$str) {
    $str = "Do you think " . $str . "?\n";
}

convertToQuestion($string_one);
convertToQuestion($string_two);
convertToQuestion($string_three);

echo $string_one;
echo $string_two;
echo $string_three;

