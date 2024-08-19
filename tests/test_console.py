#!/usr/bin/python3
"""console testing"""

import console
import unittest
from console import HBNBCommand

class test_console(unittest.TestCase):
    def create(self):
        """tests create class"""
        return HBNBCommand()
    
    def test_do_quit(self):
        """tests do_quit"""
        arg = self.create()
        self.assertTrue(arg.onecmd['quit'])

    def test_do_EOF(self):
        """tests do_EOF"""
        arg = self.create()
        self.assertTrue(arg.onecmd['EOF'])