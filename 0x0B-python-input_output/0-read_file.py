#!/usr/bin/python3
""" This module contain functions that Read and print the content of file """


def read_file(filename=""):
	""" This function read file and print to stdout"""

	with open(filename, encoding="UTF-8") as f:
		read_f = f.read()
		print(read_f)
