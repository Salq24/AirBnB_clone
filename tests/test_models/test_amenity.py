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

    def testattr(self):
        """Tests for the attributes of Amenity instance"""
        self.assertTrue(hasattr(self.amenity, "id"))
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertTrue(hasattr(self.amenity, "updated_at"))
        self.assertFalse(hasattr(self.amenity, "random_attr"))
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.__class__.__name__, "Amenity")
        self.assertEqual(self.amenity.name, "")

    def teststr(self):
        """Tests the string format of Amenity"""
        st = "[{}] ({}) {}".format(self.amenity.__class__.__name__,
                                   str(self.amenity.id),
                                   self.amenity.__dict__)
        self.assertEqual(print(st), print(self.amenity))

    def test_amenity_inst(self):
        """Tests for Amenity class instantiation"""

        st = Amenity()
        self.assertEqual(str(type(st)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(st, Amenity)
        self.assertTrue(issubclass(type(st), BaseModel))

    if __name__ == "__main__":
        unittest.main()
