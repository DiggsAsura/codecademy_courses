<?php
$riel   = 2103942;  // Cambodia
$kyat   = 19092;    // Myanmar
$krones = 109;      // Norway
$lek    = 9094;     // Albania

echo "Riel: $riel \nKyat: $kyat \nKrones: $krones \nLek: $lek \n";

// Exchange rates
$riel_to_usd = 0.00024 * $riel;
$kyat_to_usd = 0.00048 * $kyat;
$krones_to_usd = 0.093 * $krones;
$lek_to_usd = 0.010 * $lek;

// Pt 4 - echo the amount of USD
echo "\nRiel to USD: $riel_to_usd
    Kyat to USD: $kyat_to_usd
    Krones to USD: $krones_to_usd
    Lek to USD: $lek_to_usd \n";

// Pt 5. Calculate and print final amount
$exchange_fee = 1 * 4; // 1USD per conversion
$total_usd = $riel_to_usd + $kyat_to_usd + $krones_to_usd + $lek_to_usd - $exchange_fee;
echo "\nTotal will get ${total_usd}USD\n";


// Modulo trick to get rid of decimals
$usd            = $total_usd % 100000000;
$change         = $total_usd - $usd;
$rounded_change = $change * 100;
$rounded_change %= 100;
$rounded_change /= 100;
$total_usd = $usd + $rounded_change;


echo "\nTotal will get ${total_usd}USD\n";

