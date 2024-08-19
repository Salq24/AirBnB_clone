#!/usr/bin/python3
"""Module for Amenity unitests test"""

import os
import unittest
import models
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests for the Amenity class"""
    def destroy(self):
        """Destroys test methods"""
        self.resetStorage()
        pass

    def setUp(self):
        """Sets up the test methods."""
        pass

    def test_amenity_inst(self):
        """Tests for Amenity class instantiation"""

        st = Amenity()
        self.assertEqual(str(type(st)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(st, Amenity)
        self.assertTrue(issubclass(type(st), BaseModel))

    if __name__ == "__main__":
        unittest.main()
