#!/bin/bash
#Bash script that send post request to tha passed url
curl -s  -d "email=test@gmail.com&subject=I will always be here for PLD" -H "Content-Type: application/x-www-form-urlencoded" -X POST "$1"