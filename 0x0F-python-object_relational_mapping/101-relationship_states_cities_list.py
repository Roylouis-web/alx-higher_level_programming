#!/usr/bin/python3
"""
     a script that lists all State objects, and
     corresponding City objects, contained in the database hbtn_0e_101_usa
"""


from sqlalchemy import create_engine
from relationship_state import Base, State
from sqlalchemy.orm import Session
import sys


if __name__ == '__main__':
    engine = create_engine("sqlite:///hbtn_0e_101_usa.db")
    Base.metadata.create_all(engine)
    session = Session(engine)

    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))
