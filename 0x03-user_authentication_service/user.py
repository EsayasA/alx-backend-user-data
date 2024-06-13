#!/usr/bin/env python3
"""Users.
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """A class representing a user in the system.

    Attributes:
        __tablename__ (str): The name of the table in the database 
        id (int):  unique identifier.
        email (str): email.
        hashed_password (str):hashed password.
        session_id (str):  ID of the user, 
        user sessions.
        reset_token (str): The reset token of the user,
        resets.
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
