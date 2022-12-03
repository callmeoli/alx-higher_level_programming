#!/usr/bin/python3
import MySQLdb
import sys

db = MySQLdb.connect(db=sys.argv[3], host="localhost",
                     user=sys.argv[1], passwd=sys.argv[2], port=3306)
cursor = db.cursor()
cursor.execute("SELECT * FROM states ORDER BY states.id")

result = cursor.fetchall()
for row in result:
    print(row)
db.close()
