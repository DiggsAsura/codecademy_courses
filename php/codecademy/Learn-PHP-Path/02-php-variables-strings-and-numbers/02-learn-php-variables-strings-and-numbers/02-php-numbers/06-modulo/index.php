<?php
// Modulo / Remainder
// Gives the remainder after the left operand is divided by the right operand.

echo 7 % 3 . "\n"; // 1

// In the code above, 7%3 returns 1. Why? We're tyring to fit 3 into 7 as
// many times as we can. 3 fits into 7 at most twice. What's left over - the
// remainder - is 1, since 7 minus 6 is 1.

// The modulo operator will convert its operands to integers before performing
// the operation. This means 7.9 % 3.8 will perform the same caluclations as
// 7 % 3 - both operations will return 1.

$num_cookies = 27;
$cookies_per_serving = 4;
$leftover_cookies = $num_cookies % $cookies_per_serving;
echo $leftover_cookies . "\n"; // 3


