#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models.engine.file_storage import FileStorage
import os


class State(BaseModel, Base):
    __tablename__ = "states"
    name = Column("name", String(128), nullable=False)

    if 'DBStorage' == os.getenv("HBNB_TYPE_STORAGE"):
        cities = relationship("City", backref="state", cascade="all, delete-orphan", single_use=True)

    # Getter for FileStorage
    else:
        @property
        def cities(self):
            """
            Returns a list of City instances linked to the current State.
            """
            from models.city import City  # Import City to avoid circular imports
            all_cities = FileStorage.all()  # Assuming all_objects is available in FileStorage
            return [city for city in all_cities if city.__class__ == City and city.state_id == State.id]