#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv 
    length = len(argv) - 1
    if length == 0:
        print("{0} arguments.".format(length))
    elif length == 1:
        print("{0} argument:".format(length))
    else:
        print("{0} arguments:".format(length))
    for i in range(1, len(argv)):
            print("{0}: {1}".format(i, argv[i]))
