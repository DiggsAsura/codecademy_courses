<?php
function generateStory($singular_noun, $verb, $color, $distance_unit) {
    $story = "The ${singular_noun}s are lovely, ${color}, and deep.\nBut I have promises to keep,\nAnd ${distance_unit} to go before I ${verb},\nAnd ${distance_unit} to go before I ${verb}.\n\n";
    return $story;
}

echo generateStory("dog", "eat", "purple", "meters");
echo generateStory("car", "cook", "vermilion", "inches");
echo generateStory("bar", "run", "teal", "feet");

