from sqlalchemy import Column, String
from sqlalchemy.orm import backref, relationship

from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """
    Representation of a state in the database.
    """

    __tablename__ = 'states'  # Class attribute for table name

    name = Column(String(128), nullable=False)  # String column for state name (max 128 chars)
    # Getter for cities (for FileStorage)
