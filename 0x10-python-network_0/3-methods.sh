#!/bin/bash
# Bash script that print options available
curl -sIL -X OPTIONS "$1" | grep -i Allow | awk -F ": " '{print $2}'
