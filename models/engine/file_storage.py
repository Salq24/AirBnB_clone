#!/usr/bin/python3
"""File Storage class definition"""

import importlib
import os
import json
import re
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.review import Review

class FileStorage:

    """Has methods to serialize and deserialize objects"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file"""
        m_dict = {}
        for k, v in FileStorage.__objects.items():
            m_dict[k] = v.to_dict().copy()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(m_dict, f)

    
    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        if (os.path.isfile(self.__file_path)
                and os.path.getsize(self.__file_path) > 0):
            with open(self.__file_path, 'r') as f:
                self.__objects = {k: self.get_class(k.split(".")[0])(**v)
                                  for k, v in json.load(f).items()}

    def get_class(self, name):
        """ returns a class from models module using its name"""
        sub_module = re.sub('(?!^)([A-Z]+)', r'_\1', name).lower()
        module = importlib.import_module(f"models.{sub_module}")
        return getattr(module, name)