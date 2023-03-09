#!/usr/bin/python3
"""
The User Model Module(inherits from the BaseModel)

"""
from models.base_model import BaseModel


class User(BaseModel):
    """
        It implements the user model
    """
    email = ''
    password = ''
    first_name = ''
    last_name = ''