#!/usr/bin/python3

"""This module has a class, User, inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """Public class attr"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """State init"""
        super().__init__(*args, **kwargs)
