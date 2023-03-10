#!/usr/bin/python3
"""
Test for City model module
"""
import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """
    test cases for city class
    """

    def setUp(self):
        """
        this method executes before each test methods
        """
        self.city = City()
        self.city_attributes = ["state_id", "name"]

    def test_inheritance(self):
        """
        this tests if city class inherits from basemodel class
        """
        self.assertIsInstance(self.city, BaseModel)

    def test_class_attributes(self):
        """
        this tests if attributes are class attributes with the right type
        """
        for i in self.city_attributes:
            self.assertIs(type(getattr(self.city, i)), str)
            self.assertFalse(bool(getattr(self.city, i)))


if __name__ == "__main__":
    unittest.main()