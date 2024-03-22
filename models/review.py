#!/usr/bin/python3

"""This module has a class, Review, inherits from BaseModel"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Public class attr"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Review init"""
        super().__init__(*args, **kwargs)
