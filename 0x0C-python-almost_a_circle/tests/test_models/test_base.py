#!/usr/bin/python3
"""unittesting the base class"""
import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """testing for the class Base"""
    def test_pattr(self):
        """checks if Base has the private attribute"""
        self.assertIs(hasattr(Base, "_Base__nb_objects"), True)
        Base.__Base__nb_objects = 0

    def test_id_type(self):
        """check if id is an integer"""
        obj = Base()
        self.assertIs(isinstance(obj.id, int), True)


