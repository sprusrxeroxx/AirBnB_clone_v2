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

    # Getter for cities (for FileStorage)
    from os import getenv

    if getenv('HBNB_TYPE_STORAGE') != "db":
            name = ""

            @property
            def cities(self):
                """ returns list of City instances related to state """
                from models import storage
                list_cities = []
                for city in storage.all(City).values():
                    if city.state_id == self.id:
                        list_cities.append(city)
                return list_cities
    else:
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete-orphan")