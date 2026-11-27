#!/usr/bin/python3
"""Safe from SQL injection: displays states where name matches argument."""
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
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                (sys.argv.__getitem__(4),))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
