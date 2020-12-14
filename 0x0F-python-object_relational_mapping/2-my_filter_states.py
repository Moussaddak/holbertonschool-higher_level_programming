#!/usr/bin/python3
"""
  Takes in an argument and displays all values in the states table
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")

    with db.cursor() as cursor:
#first solution
      cursor.execute("SELECT * FROM states WHERE name LIKE BINARY ('{}')\
                          ORDER BY id".format(argv[4]))
#second solution:
#        cursor.execute("SELECT * FROM states WHERE name= %(name)s ORDER BY id",
#                       {'name': argv[4]})
        rows = cursor.fetchall()
        for row in rows:
            print(row)
