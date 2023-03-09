#!/usr/bin/python3
"""Model Base """
import uuid
import models
from datetime import datetime


class BaseModel:
    """class Base"""
    def __init__(self):
     self.id = str(uuid.uuid4())  # unique id
     self.created_at = datetime.now()  # datetime when is created
     self.updated_at = datetime.now()  # date when is updated
def __str__(self):
        """ print() __str__ method """
        """" For pep8 validation"""
        className = self.__class__.__name__
        return "[{}] ({}) {}".format(className, self.id, self.__dict__)

def save(self):
        """ updates with the current datetime """
        self.updated_at = datetime.now()
def to_dict(self):
        '''returns a dictionary with all keys/value of the instance'''
        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        dict_copy['__class__'] = self.__class__.__name__
        return dict_cop
