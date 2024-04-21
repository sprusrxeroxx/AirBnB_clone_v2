#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import ForeignKey, String, Column
from sqlalchemy.orm import relationship
import os 
class City(BaseModel, Base):
    """A city class, defines all cities in db"""
    __tablename__ = "cities"
    if os.environ.get("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities",
                              cascade="delete")
    else:
        state_id = ""
        name = ""