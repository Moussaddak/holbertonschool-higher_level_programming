#!/usr/bin/python3
"""
Get all states
"""

import MySQLdb
from sys import argv


db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                     passwd=argv[2], db=argv[3], charset="utf8")
cursor = db.cursor()
cursor.execute("SELECT * FROM states ORDER BY id ASC")
rows = cursor.fetchall()
for row in rows:
    print(row)
cursor.close()
db.close()
