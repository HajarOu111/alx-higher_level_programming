#!/bin/bash
# bash script that sends a POST request to a given URL.
curl -s -X POST "email=test@gmail.com&subject=I will always be here for PLD" "$1"
