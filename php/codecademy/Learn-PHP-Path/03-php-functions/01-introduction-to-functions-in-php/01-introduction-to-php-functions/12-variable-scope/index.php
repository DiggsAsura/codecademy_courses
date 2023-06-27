<?php
/*
function calculateDaysLeft($feed_quantity, $number, $rate) {
    $result = $feed_quantity / ($number * $rate);
    return $result . "\n";
}
echo calculateDaysLeft(300, 2, 30);
*/
//

// global scope

$feed_quantity = 300;

function calculateDaysLeft($number, $rate) {
    global $feed_quantity;
    $result = $feed_quantity / ($number * $rate);
    return $result . "\n";
}
echo calculateDaysLeft(2, 30);

// When using this pattern, it becomes slightly more difficult to determine what
// information this function depends on. Make sure to consider this trade-off
// when implementing your own functions.
//
// Note that the global keyword is not used when invoking functions. Once a
// function has been defined, it can be used within the same code block or
// even within other function clode blocks. This code will print "This works!"
// to the console.

function first() {
    echo "This works!\n";
}

function second() {
    first();
}
second();

//
//

$language = "PHP";
$topic = "scope";

function generateLessonName($concept) {
    global $language;
    return $language . ": " . $concept;
}

echo generateLessonName($topic) . "\n";
