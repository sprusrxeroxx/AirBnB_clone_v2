from sqlalchemy import Column, String
from sqlalchemy.orm import backref, relationship

from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """
    Representation of a state in the database.
    """

    __tablename__ = 'states'  # Class attribute for table name

    name = Column(String(128), nullable=False)  # String column for state name (max 128 chars)

    # Relationship with City model (cascade="all, delete-orphan"): for DBStorage
    cities = relationship(
        "City", backref=backref("state", cascade="all, delete-orphan"), cascade="all, delete-orphan"
    )

    # Getter for cities (for FileStorage)
    @property
    def cities(self):
        """
        Returns a list of City instances with state_id equal to the current State.id.
        """
        if hasattr(self, "_cities"):
            return self._cities
        self._cities = []
        return self._cities
