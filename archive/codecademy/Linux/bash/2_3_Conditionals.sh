#!/bin/bash

# Equal: -eq
# Not equal: -ne
# Less than or equal: -le
# Less than: -lt
# Greater than or equal: -ge
# Greater than: -gt
# Is null: -z

# Comparing strings best practice
# Equal: ==
# Not equal: !=

first_greeting="Nice to meet you!"
later_greeting="How are you?"
greeting_occasion=1

if [ $greeting_occasion -lt 1 ]
then
  echo $first_greeting
else
  echo $later_greeting
fi

