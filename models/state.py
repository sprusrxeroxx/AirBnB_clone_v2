#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import ForeignKey, String, Column


class State(BaseModel, Base):
    __tablename__ = "states"
    name = Column("name", String(128), nullable=False)
    """ State class """
    name = ""
