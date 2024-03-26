#!/usr/bin/python3
"""Module for City unitests test"""

import os
import unittest
import models
from datetime import datetime
from time import sleep
from models.place import Place


class TestPlace(unittest.TestCase):
    """Tests for the Place class"""
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

    def test_place_inst(self):
        """Tests for place class instantiation"""

        st = Place()
        self.assertEqual(str(type(st)), "<class 'models.place.Place'>")
        self.assertIsInstance(st, Place)
        self.assertTrue(issubclass(type(st), BaseModel))

    if __name__ == "__main__":
        unittest.main()
