<?php
function increaseEnthusiasm($string) {
    return $string . '!' . "\n";
}

echo increaseEnthusiasm('Hello');

function repeatThreeTimes($string) {
    return $string . $string . $string . "\n";
}

echo repeatThreeTimes(increaseEnthusiasm('Yes'));
