#!/usr/bin/python3
def uppercase(str):
    for elements in str:
        if ord(elements) >= 97 and ord(elements) <= 122:
            n = (chr(ord(elements) - 32))
        else:
            n = elements
        print("{}".format(n), end="")
    print("{}".format("\n"), end="") 
