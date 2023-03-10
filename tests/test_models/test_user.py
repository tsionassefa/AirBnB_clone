#!/usr/bin/python3
"""Test for User model module"""
import unittest
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    """
    Test cases for the User class
    """

    def setUp(self):
        """
        this method executes before each test methods
        """
        self.user = User()
        self.user_attributes = ["first_name", "last_name", "email", "password"]

    def test_inheritance(self):
        """
        this tests if state class inherits from basemodel class
        """
        self.assertIsInstance(self.user, BaseModel)

    def test_class_attribute(self):
        """
        this tests if the class has a class attributes
        """
        for i in self.user_attributes:
            self.assertTrue(hasattr(User, i))

    def test_class_attribute_valid_type(self):
        """
        this tests if the class attribute is of type 'string'
        """
        self.assertIs(type(self.user.first_name), str)
        self.assertIs(type(self.user.last_name), str)
        self.assertIs(type(self.user.email), str)
        self.assertIs(type(self.user.password), str)

if __name__ == "__main__":
    unittest.main()