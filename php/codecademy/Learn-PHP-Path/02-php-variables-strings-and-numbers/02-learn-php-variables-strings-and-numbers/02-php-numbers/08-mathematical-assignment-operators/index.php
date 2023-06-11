<?php
// Standard += -= *= /= %= etc

// Increment / Decrement
$age = 89;
$age++; // 90
echo $age . "\n";

$days_til_vaction = 25-11;
$days_til_vaction--; // 13
echo $days_til_vaction . "\n";


$my_num = 100;
$answer = $my_num;

$answer += 2;
$answer *= 2;
$answer -= 2;
$answer /= 2;
$answer -= $my_num;
echo $answer . "\n";
