#!/usr/bin/python3
"""Displays all values in states where name matches the argument."""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv.__getitem__(1),
        passwd=sys.argv.__getitem__(2),
        db=sys.argv.__getitem__(3)
    )
    cur = db.cursor()
    query = ("SELECT * FROM states WHERE name LIKE BINARY '{}' "
             "ORDER BY id ASC".format(sys.argv.__getitem__(4)))
    cur.execute(query)
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
