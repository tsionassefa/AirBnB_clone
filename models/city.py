#!/usr/bin/python3
"""
    The City Module(inherits from the BaseModel)
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
        it implements city model
    """
    state_id = ''
    name = ''