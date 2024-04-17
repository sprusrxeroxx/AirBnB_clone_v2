#!/usr/bin/python3
"""""This module contains the engine for the 
    database of the hbnb app"""

import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session, relationship, backref

Base = declarative_base()

class DBStorage():
    __engine = None
    __session = None
        # Relationship with City model (cascade="all, delete-orphan"): for DBStorage
    _cities = relationship(
        "City", backref=backref("state", cascade="all, delete-orphan"), cascade="all, delete-orphan"
    )

    """""Initialization of MySql databse interaction"""

    def __init__(self):

        user = os.getenv('HBNB_MYSQL_USER')
        password = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv("HBNB_MYSQL_HOST", "localhost")
        database = os.getenv('HBNB_MYSQL_DB')

        # A connection string using env variables
        connection_string = f'mysql+mysqldb://{user}:{password}@{host}/{database}'

        # Establing a connectiont to the database
        self.__engine = create_engine(connection_string, pool_pre_ping=True)

        # Condition for test environment
        if os.getenv("HBNB_ENV") == "test":
            self.__drop_all_tables()

        # Create all database tables
        Base.metadata.create_all(self.__engine)

        # Create a session to the database
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)

        self.__session = scoped_session(Session)
    
    def __drop_all_tables(self):
        """
        Drops all tables from the database.
        """
        meta = MetaData()
        meta.reflect(self.__engine)
        meta.drop_all(self.__engine)

    def all(self, cls=None):
        """"Queries all objects from the database based on the provided class or all objects.

            Args:
                cls (class, optional): The class to query for. Defaults to None (all objects).

            Returns:
                dict: A dictionary where the key is "<class-name>.<object-id>" and the value is the object.
        """""
        if cls :
            query = self.__session.query(cls)
        else:
            query = self.__session.query()

        objects = query.all()

        return {f"{type(obj).__name__}.{obj.id}:" for obj in objects}
    
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
        if obj :
            self.__session.delete(obj)

    def reload(self):
        """Reloads the current database session"""
        self.__session.close()
        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))


        