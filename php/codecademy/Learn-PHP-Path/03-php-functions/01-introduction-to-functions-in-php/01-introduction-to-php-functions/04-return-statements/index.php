<?php
function countdown() {
    echo "4, 3, 2, 1, ";
    return "blastoff!";
}

$return_value = countdown();

//countdown();
echo $return_value . "\n";

function printStringReturnNumber() {
    echo "Hello World!\n";
    return 5;
}

$my_num = printStringReturnNumber();
echo $my_num . "\n";
