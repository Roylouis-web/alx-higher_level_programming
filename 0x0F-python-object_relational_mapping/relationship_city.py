#!/usr/bin/python3
"""
    Module for a class called City
"""


from sqlalchemy import (Column, Integer, String, ForeignKey)
from relationship_state import Base, relationship


class City(Base):
    """
       a Python file similar to model_state.py named model_city.py
       that contains the class definition of a City.
    """

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship('State', back_populates='cities')
