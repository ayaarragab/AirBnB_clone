#!usr/bin/python3

"""
User model (class) module that inherits from base model
"""
from .base_model import BaseModel


class User(BaseModel):
    """
    a class User that inherits from BaseModel
    Public class attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
