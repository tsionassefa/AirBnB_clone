#!/usr/bin/python3
"""
Test for review model module
"""
import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """
    test cases for review class
    """

    def setUp(self):
        """
        this method executes before each test methods
        """
        self.review = Review()
        self.review_attributes = ["user_id", "place_id", "text"]

    def test_inheritance(self):
        """
        this tests if review class inherits from basemodel class
        """
        self.assertIsInstance(self.review, BaseModel)

    def test_class_attributes(self):
        """
        this tests if attributes are class attributes and of a particular type
        """
        for i in self.review_attributes:
            self.assertIs(type(getattr(self.review, i)), str)
            self.assertFalse(bool(getattr(self.review, i)))


if __name__ == "__main__":
    unittest.main()