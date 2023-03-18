#!/usr/bin/python3
"""
    a script that lists all cities from the database hbtn_0e_4_usa
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
    conn = MySQLdb.connect(
            host='localhost', port=3306,
            user=user_name, passwd=password,
            db=db_name
            )
    cur = conn.cursor()
    cmd = """
                SELECT c.id, c.name, s.name FROM cities AS c
                INNER JOIN states AS s
                ON c.state_id = s.id
                ORDER BY c.id
          """
    cur.execute(cmd)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
