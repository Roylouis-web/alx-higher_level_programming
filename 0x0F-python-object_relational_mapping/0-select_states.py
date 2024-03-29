#!/usr/bin/python3
"""
    a script that lists all states from the database hbtn_0e_0_usa
"""


import sys
import MySQLdb


if __name__ == '__main__':
    argv = sys.argv
    if len(argv) < 4:
        print("Usage: {} username password database_name".format(argv[0]))
        exit(1)
    username = argv[1]
    password = argv[2]
    db_name = argv[3]
    conn = MySQLdb.connect(
            host="localhost", port=3306,
            user=username, passwd=password, db=db_name
            )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
