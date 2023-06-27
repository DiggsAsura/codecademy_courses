<?php

function sayCustomHello($name) {
    echo "Hello $name\n";
};

sayCustomHello("John");


function greetFriend($name = "old chum") {
    echo "Hello, $name!\n";
};

greetFriend("Marvin");
greetFriend();


function calculateTip($total, $tip = 20) {
    return $total + ($total * ($tip/100)) ."\n";
}

echo calculateTip(100, 25);
echo calculateTip(100);


