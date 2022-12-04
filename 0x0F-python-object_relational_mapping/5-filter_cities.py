#!/usr/bin/python3
"""
This script takes in an argument and
displays all values in the states
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
This time the script is safe from
MySQL injections!
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Access to the database and get the states
    from the database.
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute("""
            SELECT
                cities.name
            FROM
                cities
            WHERE
                cities.state_id=( SELECT `id` FROM states WHERE name LIKE BINARY %(state_name)s)
            ORDER BY
                cities.id ASC
        """, {'state_name': argv[4]})

        rows = cur.fetchall()

    if rows is not None:
        print(", ".join([row[1] for row in rows]))
