#!/usr/bin/python3
"""
     a script that creates the State “California” with the City
     “San Francisco” from the database hbtn_0e_100_usa
"""


from sqlalchemy import create_engine
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy.orm import Session
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format
                           (sys.argv[1], sys.argv[2],
                            sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)

    state = State(name='California')
    city = City(name='San Francisco')
    state.cities.append(city)
    session.add(state)
    session.commit()
    session.close()
