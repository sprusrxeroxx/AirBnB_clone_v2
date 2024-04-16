#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import ForeignKey, String, Column




class City(BaseModel, Base):
    __tablename__ = "cities"
    name = Column("name", String(128), nullable=False)
    state_id = Column("state_id", String(60), ForeignKey("states.id"), nullable=False)

    """ The city class, contains state ID and name """
    state_id = ""
    name = ""
