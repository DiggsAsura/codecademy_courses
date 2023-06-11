<?php
$last_month = 1187.23;
$this_month = 1089.98;
/*
echo $last_month - $this_month . "\n";
*/

$testing = $last_month + 1;

echo $testing;
echo "\n\n";

$testing2 =& $last_month;

$testing2 = $testing2 + 1;
echo "\n\n";
echo $last_month;

echo $testing2;
