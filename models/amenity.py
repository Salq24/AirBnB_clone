#!/usr/bin/python3

"""This module has a class, Amenity, inherits from BaseModel"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Public class attr"""
    name = ""

    def __init__(self, *args, **kwargs):
        """Amenity init"""
        super().__init__(*args, **kwargs)
