#!/usr/bin/env python3

import sys
import MySQLdb

"""
    a script that takes in arguments and displays all
    values in the states table of hbtn_0e_0_usa where
    name matches the argument. But this time, write one
    that is safe from MySQL injections!
"""


def main(user_name, password, db_name, state_name):
    conn = MySQLdb.connect(
            host='localhost', port=3306,
            user=user_name, passwd=password,
            db=db_name)
    cur = conn.cursor()
    cmd = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cur.execute(cmd, (state_name, ))
    rows = cur.fetchall()

    for row in rows:
        print(row)
    cur.close()
    conn.close()


if __name__ == '__main__':
    argv = sys.argv
    user_name = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]
    main(user_name, password, db_name, state_name)
