#!/usr/bin/python3
"""
    a script that takes in arguments and displays all
    values in the states table of hbtn_0e_0_usa where
    name matches the argument.
"""


import sys
import MySQLdb


if __name__ == '__main__':
    argv = sys.argv
    if len(argv) < 5:
        print("Usage: {} username password database_name".format(argv[0]))
        exit(1)
    user_name = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]
    conn = MySQLdb.connect(
            host='localhost', port=3306,
            user=user_name, passwd=password,
            db=db_name)
    cur = conn.cursor()
    cmd = "SELECT * FROM states WHERE name = '{}' ORDER BY id"
    cur.execute(cmd.format(state_name))
    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    conn.close()
