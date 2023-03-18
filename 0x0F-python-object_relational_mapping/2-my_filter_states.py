#!/usr/bin/env python3
import sys
import MySQLdb

"""
    a script that takes in an argument and displays all
    values in the states table of hbtn_0e_0_usa where
    name matches the argument.
"""


def main(user_name, password, db_name, state_name):
    conn = MySQLdb.connect(
            host='localhost', port=3306,
            user=user_name, passwd=password,
            db=db_name)
    cur = conn.cursor()
    cur.execute(
            """
                SELECT * FROM states WHERE name = '{:s}'
                ORDER BY id
            """.format(state_name)
            )
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
