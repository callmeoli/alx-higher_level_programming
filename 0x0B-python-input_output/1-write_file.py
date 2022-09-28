 #!/usr/bin/python3
""" This module contain functions write file and return number of character written """


def write_file(filename="", text=""):
	""" This function write file and return number of character written"""

	with open(filename, 'w', encoding="UTF-8") as f:
		read_f = f.write(text)
		return (read_f)
