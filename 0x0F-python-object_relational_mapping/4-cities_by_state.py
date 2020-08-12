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
        cursor.execute("select cities.id, cities.name, states.name\
                       From cities inner join states\
                       on cities.state_id=states.id\
                       ORDER BY cities.id")
        rows = cursor.fetchall()
        for row in rows:
                print(row)
