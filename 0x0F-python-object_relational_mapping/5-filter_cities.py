#!/usr/bin/env python3
"""
    a script that takes in the name of a state as
    an argument and lists all cities of that state,
    using the database hbtn_0e_4_usa
"""


import sys
import MySQLdb


if __name__ == '__main__':
    argv = sys.argv
    if len(argv) < 4:
        print("Usage: {} username password database_name".format(argv[0]))
        exit(1)
    user_name = argv[1]
    password = argv[2]
    db_name = argv[3]
    state_name = argv[4]
    conn = MySQLdb.connect(
            host='localhost', port=3306,
            user=user_name, passwd=password,
            db=db_name
            )
    cur = conn.cursor()
    cmd = """
                SELECT c.name FROM cities as c
                INNER JOIN states AS s
                ON s.id = c.state_id
                WHERE s.name = %s
          """
    cur.execute(cmd, (state_name, ))
    rows = cur.fetchall()

    i = 0
    for row in rows:
        j = 0
        for item in row:
            if j < len(item) - 1 and i != len(rows) - 1:
                print(item, end=', ')
            else:
                print(item, end='')
            j += 1
        i += 1
    print()

    cur.close()
    conn.close()
