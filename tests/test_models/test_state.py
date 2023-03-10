#!/usr/bin/python3
"""Test for State model module"""
import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """
    Test cases for the State class
    """

    def setUp(self):
        """
        this method executes before each test methods
        """
        self.state = State()

    def test_inheritance(self):
        """
        this tests if state class inherits from basemodel class
        """
        self.assertIsInstance(self.state, BaseModel)

    def test_class_attribute(self):
        """
        this tests if the class has a class attribute 'name'
        """
        self.assertTrue(hasattr(self.state, "name"))

    def test_class_attribute_valid_type(self):
        """
        this tests if the class attribute is of type 'string'
        """
        self.assertIs(type(self.state.name), str)
        self.assertFalse(bool(self.state.name))

if __name__ == "__main__":
    unittest.main()