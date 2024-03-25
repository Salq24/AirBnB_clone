#!/usr/bin/python3
"""Module for User unitests test"""

import os
import unittest
import models
from datetime import datetime
from time import sleep
from models.user import User

class TestUser(unittest.TestCase):
    """Tests for the User class"""
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

    def test_user_inst(self):
        """Tests for user class instantiation"""

        st = User()
        self.assertEqual(str(type(st)), "<class 'models.user.User'>")
        self.assertIsInstance(st, User)
        self.assertTrue(issubclass(type(st), BaseModel))

    if __name__ == "__main__":
        unittest.main()


