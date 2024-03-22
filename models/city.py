#!/usr/bin/python3

"""This module has a class, City, inherits from BaseModel"""

from models.base_model import BaseModel


class City(BaseModel):
    """Public class attr"""
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """Amenity init"""
        super().__init__(*args, **kwargs)
