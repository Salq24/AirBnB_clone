#!/usr/bin/python3
"""File Storage class definition"""


import json
import os
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
        return type(self).__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        ocnm = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocnm, obj.id)] = obj

    def save(self):
        """ serializes __objects to the JSON file"""
        mdict = FileStorage.__objects
        objdict = {obj: mdict[obj].to_dict() for obj in mdict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)


    def reload(self):
        """Reloads the stored objects"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
