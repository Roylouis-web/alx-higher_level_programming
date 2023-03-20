#!/usr/bin/python3
"""
     Module for a class called State
"""


from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import (Column, Integer, String)


Base = declarative_base()


class State(Base):
    """
        a python file that contains the class definition of a
        State and an instance Base = declarative_base()
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship('City',
                        cascade='save-update, merge, delete, delete-orphan',
                        back_populates='state')
