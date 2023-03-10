#!/usr/bin/python3
""" FileStorage that serializes instances to a JSON file and deserializes JSON
file to instances:
"""

import json

import models
from models.base_model import BaseModel




class FileStorage():
    """ serializes instances to a JSON file and deserializes JSON"""

    __file_path = "file.json"  # path to the JSON file (ex: file.json)
    __objects = {}  # dictionary - store all objects by <class name>.id

    def all(self):
        """  returns the dictionary __objects """
        return self.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """
        '''get key of the form <obj class name>.id '''
        key = obj.__class__.__name__ + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_data = {}
        for i, j in self.__objects.items():
            json_data[i] = j.to_dict()

        new_data = json.dumps(json_data)
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            f.write(new_data)

    def reload(self):
        """ deserializes the JSON file to __objects """
        if path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r', encoding="utf-8") as f:
                    self.__objects = json.load(f)
                    for key, value in json.load(f).items():
                        class_name = value["__class__"]
                        class_name = models.classes[class_name]
                        self.__objects[key] = class_name(**value)
            except FileNotFoundError:
                pass
