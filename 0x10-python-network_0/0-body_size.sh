#!/usr/bin/env bash
# Bash script that send request to url desplaysize of response

curl -sI "$1" | grep -i 'Content-Length' | awk '{print $2}'