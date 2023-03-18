#!/usr/bin/env python3
import sys
import MySQLdb

"""
    a script that lists all states from the database hbtn_0e_0_usa
"""


def main(username, password, db_name):
    conn = MySQLdb.connect(
            host="localhost", port=3306,
            user=username, passwd=password, db=db_name
            )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == '__main__':
    argv = sys.argv
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    main(username, password, db_name)
