#!/usr/bin/python3
"""Module for City unitests test"""

import os
import unittest
import models
from datetime import datetime
from time import sleep
from models.amenity import Amenity

class TestCity(unittest.TestCase):
    """Tests for the City class"""
    def destroy(self):
        """Destroys test methods"""
        self.resetStorage()
        pass

    def setUp(self):
        """Sets up the test methods"""
        pass

    def test_docstr(self):
        """Tests the string format of City"""
        self.assertIsNot(City.__doc__, None,
                         "City needs a docstring")
        self.assertTrue(len(City.__doc__) >= 1,
                        "City  needs a docstring")

    def test_city_inst(self):
        """Tests for city class instantiation"""

        st = City()
        self.assertEqual(str(type(st)), "<class 'models.city.City'>")
        self.assertIsInstance(st, City)
        self.assertTrue(issubclass(type(st), BaseModel))

    if __name__ == "__main__":
        unittest.main()


