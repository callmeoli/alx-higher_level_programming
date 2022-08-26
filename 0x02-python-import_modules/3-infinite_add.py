#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    sum1 = 0
    for i in range(1, len(argv)):
        sum1 = sum1 + int(argv[i])
print("{0}".format(sum1))
