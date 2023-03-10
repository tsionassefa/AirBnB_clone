#!/usr/bin/python3
"""Test for Amenity model module"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """
    Test cases for the amenity class
    """

    def setUp(self):
        """
        this method executes before each test methods
        """
        self.amenity = Amenity()

    def test_inheritance(self):
        """
        this tests if amenity class inherits from basemodel class
        """
        self.assertIsInstance(self.amenity, BaseModel)

    def test_class_attribute(self):
        """
        this tests if the class has a class attribute 'name'
        """
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_class_attribute_valid_type(self):
        """
        this tests if the class attribute is of type 'string'
        """
        self.assertIs(type(self.amenity.name), str)
        self.assertFalse(bool(getattr(self.amenity, "name")))

if __name__ == "__main__":
    unittest.main()