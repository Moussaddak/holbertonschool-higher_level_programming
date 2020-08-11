#!/usr/bin/python3
"""
  Takes in an argument and displays all values in the states table
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
        cursor.execute("SELECT * FROM states WHERE name=('{}') ORDER BY id"
                       .format(argv[4]))
        rows = cursor.fetchall()
        for row in rows:
            if row[1] == argv[4]:
                print(row)
