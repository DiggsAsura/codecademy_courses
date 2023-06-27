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
