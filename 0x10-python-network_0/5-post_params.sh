#!/bin/bash
# Displays the body of the response
curl -sX POST -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD" "$1"
