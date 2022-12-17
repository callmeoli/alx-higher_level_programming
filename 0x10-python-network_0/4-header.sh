#!/bin/bash
# a script that take url and send get request to the url
curl -s -H "X-School-User-Id" -X GET "$1"