#!/usr/bin/python3
def uppercase(str):
    for elements in str:
        if ord(elements) >= 97 and ord(elements) <= 122:
            print(chr(ord(elements) - 32), end="")
        else:
            print(elements, end="")
    print("\n", end="") 
