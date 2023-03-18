#!/usr/bin/python3
"""
    a script that prints the State object with the name
    passed as argument from the database hbtn_0e_6_usa
"""


import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import Session


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format
                           (sys.argv[1], sys.argv[2],
                            sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    state = session.query(State)\
        .filter(State.name == '%s' % (sys.argv[4], )).first()
    if not state:
        print("Not found")
    else:
        print(state.id)
    session.close()
