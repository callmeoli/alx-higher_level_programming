 #!/usr/bin/python3
""" This a function that returns the JSON representation of an object (string)"""


import json

def to_json_string(my_obj):
	""" This function write file and return number of character written"""
	return json.dump(my_obj)
