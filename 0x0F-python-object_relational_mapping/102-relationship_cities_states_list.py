#!/usr/bin/python3
"""
    a script that lists all City objects
    from the database hbtn_0e_101_usa
"""


from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from relationship_state import Base, State
from relationship_city import City
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format
                           (sys.argv[1], sys.argv[2],
                            sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    for city in session.query(City).all():
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
