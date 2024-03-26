#!/usr/bin/python3
"""Module has unittest for filestorage"""


import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
import time
from models.engine.file_storage import FileStorage
from models import *



class TestFileStorage(unittest.TestCase):
    """
    Testcase for file storage
    """

    def setUp(self):
        self.store = FileStorage()

    def tearDown(self):
        """Tears down test methods."""
        self.resetStorage()
        pass

    def test_attrs(self):
        """test for presence of attributes"""
        self.assertFalse(hasattr(self.store, "BrandynAndGary.json"))

    def test_all(self):
        """tests if all works in File Storage"""
        storage = FileStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)
        self.assertIs(obj, storage._FileStorage__objects)

if "__main__" == __name__:
    unittest.main()
