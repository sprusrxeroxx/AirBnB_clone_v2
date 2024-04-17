#!/usr/bin/python3
"""""This module contains the engine for the 
    database of the hbnb app"""
import os

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session, relationship, backref
import models
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class DBStorage():
    __engine = None
    __session = None

    """""Initialization of MySql databse interaction"""

    def __init__(self):

        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv("HBNB_MYSQL_HOST")
        database = os.getenv('HBNB_MYSQL_DB')
        env_var = os.getenv('HBNB_ENV', 'none')

        # A connection string using env variables
        connection_string = f'mysql+mysqldb://{user}:{password}@{host}/{database}'

        # Establing a connectiont to the database
        self.__engine = create_engine(connection_string, pool_pre_ping=True)

        # Condition for test environment
        if env_var == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """"Queries all objects from the database based on the provided class or all objects.

            Args:
                cls (class, optional): The class to query for. Defaults to None (all objects).

            Returns:
                dict: A dictionary where the key is "<class-name>.<object-id>" and the value is the object.
        """""
        dic = {}
        if cls :
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)

            for i in query:
                key = "{}.{}".format(type(i).__name__, i.id)
                dict[key] = i
        else:
            c_list = [State, City, User, Place, Review, Amenity]
            for clase in c_list:
                query = self.__session.query(clase)
                for i in query:
                    key = "{}.{}".format(type(i).__name__, i.id)
                    dic[key] = i
        return (dic)
    
    def new(self, obj=None):
        """Adds new object to database
        
        Args:
            obj : The object to add to database
        """
        return self.__session.add(obj)
    
    def save(self): 
        """Commits changes made to database"""
        return self.__session.commit()
    
    def delete(self, obj=None):
        """Deletes object from the current database session 
        
            Args:
                obj : The object to delete from database
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reloads the current database session"""
         # Create all database tables
        self.__session = Base.metadata.create_all(self.__engine)

        # Create a session to the database
        lab = sessionmaker(bind=self.__engine, expire_on_commit=False)

        Session = scoped_session(lab)
        self.__session = Session()

    def close(self):
        # Closes current session
        self.__session.close()
        