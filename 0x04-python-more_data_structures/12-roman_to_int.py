#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string.isdigit() or None:
        return 0
    dic = {"M": 1000, "C": 100, "D": 500, "X": 10, "L": 50, "V": 5, "I": 1}
    num = 0
    last = "I"
    for numeral in roman_string[::-1]:
        if dic[numeral] < dic[last]:
            num = num - dic[numeral]
        else:
            num = num + dic[numeral]
        last = numeral
    return num
