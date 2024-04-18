from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref



class State(BaseModel, Base):
    """
    Representation of a state in the database.
    """

    __tablename__ = 'states'  # Class attribute for table name

    name = Column(String(128), nullable=False)  # String column for state name (max 128 chars)

    # Relationship with City model (cascade="all, delete-orphan"): for DBStorage
    cities = relationship(
        "City", backref=backref("state", cascade="all, delete-orphan")
    )

    # Getter for cities (for FileStorage)
    from os import getenv
    if getenv('HBNB_TYPE_STORAGE') != "db":
            @property
            def cities(self):
                """ returns list of City instances related to state """
                from models import storage
                list_cities = []
                for city in storage.all(City).values():
                    if city.state_id == self.id:
                        list_cities.append(city)
                return list_cities
