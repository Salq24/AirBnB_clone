#!/usr/bin/python3

"""This module has a class, State, inherits from BaseModel"""

from models.base_model import BaseModel


class State(BaseModel):
    """Public class attr"""
    name = ""

    def __init__(self, *args, **kwargs):
        """State init"""
        super().__init__(*args, **kwargs)
