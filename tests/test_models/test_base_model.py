#!/usr/bin/python3
"""Module for BaseModel unitests test"""

import os
import unittest
import models
from datetime import datetime
from time import sleep
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Tests for the BaseModel class"""
    def destroy(self):
        """Destroys test methods"""
        self.resetStorage()
        pass

    def setUp(self):
        """Sets up the test methods"""
        pass

     def resetStorage(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_BaseModel_inst(self):
        """Tests for user class instantiation"""

        st = BaseModel()
        self.assertEqual(str(type(st)), "<class 'models.base_model.BaseModel'>")
        self.assertIsInstance(st, BaseModel)
        self.assertTrue(issubclass(type(st), BaseModel))

    if __name__ == "__main__":
        unittest.main()


