<?php
function returnNothing() {
    echo "I'm running! I'm running\n";
}

$result = returnNothing();

echo "Result is: $result\n";


//
//

function createVacuum() {
}

echo createVacuum() + 10 . "\n\n";
