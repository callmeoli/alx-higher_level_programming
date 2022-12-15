#!/usr/bin/python3
"""
This script will connect to database by
passed user passwd and database
and print elementes orderd by id
filter with name start with N
"""
import MySQLdb
import sys

if __name__ == '__main__':
    """
    Access the database and
    print elments Start with N
    """
    db = MySQLdb.connect(db=sys.argv[3], host="localhost",
                         user=sys.argv[1], passwd=sys.argv[2], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
                    WHERE name LIKE BINARY 'N%' \
                    ORDER BY states.id ASC")

    result = cursor.fetchall()
    for row in result:
        print(row)
    db.close()
