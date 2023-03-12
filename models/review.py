#!/usr/bin/python3
"""
The Review Module(inherits from the BaseModel)
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    It implements the review model
    """
    place_id = ''
    user_id = ''
    text = ''