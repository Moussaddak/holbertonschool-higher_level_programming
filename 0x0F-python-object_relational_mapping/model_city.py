#!/usr/bin/python3
"""
First model_city with ORM
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(State):
    """Representation of a city"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer,ForeignKey('states.id'))
