#!/usr/bin/python3
"""
  Python script
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         charset="utf8")

    with db.cursor() as cursor:
        cursor.execute("SELECT cities.name FROM cities \
        LEFT JOIN states ON cities.state_id = states.id WHERE states.name\
        LIKE BINARY '{}' ORDER BY cities.id".format(argv[4]))
        rows = cursor.fetchall()
        print(rows)
        print(", ".join(row[0] for row in rows))
