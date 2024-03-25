#!/usr/bin/python3
"""This houses the class BaseModel that defines all common methods
for other classes"""

import models
from datetime import datetime
from uuid import uuid4


class BaseModel:

    """All other objects inherit from this class"""

    def __init__(self, *args, **kwargs):
        """BaseModel class init"""

        if kwargs:
            for k,v in kwargs.items():
                if k != "__class__":
                    setattr(self, k, v)
            if hasattr(self, "created at") and type(self.created_at) is str:
                self.__dict__['created_at'] = datetime.strptime(kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            if hasattr(self, "updated_at") and type(self.updated_at) is str:
                self.__dict__['updated_at'] = datetime.strptime(kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns str rep"""
        return ("[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
        )

    def to_dict(self):
        """Returns a dict that contains all the k/v of __dict__"""
        m_dict = self.__dict__.copy()
        m_dict["__class__"] = self.__class__.__name__
        m_dict["created_at"] = self.created_at.isoformat()
        m_dict["updated_at"] = self.updated_at.isoformat()
        return m_dict

    def save(self):
        """updates the public instance attr"""
        self.updated_at = datetime.now()
        models.storage.save()
