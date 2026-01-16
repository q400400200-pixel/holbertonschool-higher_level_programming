#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys


if __name__ == "__main__":
    # arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    # execute query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # fetch and print results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
