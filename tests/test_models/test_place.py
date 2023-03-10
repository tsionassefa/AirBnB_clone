#!/usr/bin/python3
"""
Test for place model module
"""
import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """
    test cases for Place class
    """

    def setUp(self):
        """
        this method executes before each test methods
        """
        self.place = Place()
        self.place_attributes = ["name", "user_id", "city_id", "description",
                          "number_bathrooms", "max_guest", "number_rooms",
                          "price_by_night", "latitude", "longitude",
                          "amenity_ids"]

    def test_inheritance(self):
        """
        this tests if city class inherits from basemodel class
        """
        self.assertIsInstance(self.place, BaseModel)

    def test_class_attributes(self):
        """
        this tests if attributes are class attributes
        """
        for i in self.place_attributes:
            self.assertTrue(hasattr(Place, i))

    def test_class_attributes_type(self):
        """
        this tests if attributes are of a particular type
        """
        self.assertIs(type(self.place.name), str)
        self.assertIs(type(self.place.city_id), str)
        self.assertIs(type(self.place.user_id), str)
        self.assertIs(type(self.place.description), str)
        self.assertIs(type(self.place.number_bathrooms), int)
        self.assertIs(type(self.place.max_guest), int)
        self.assertIs(type(self.place.number_rooms), int)
        self.assertIs(type(self.place.price_by_night), int)
        self.assertIs(type(self.place.latitude), float)
        self.assertIs(type(self.place.longitude), float)
        self.assertIs(type(self.place.amenity_ids), list)

        for i in self.place_attributes:
            self.assertFalse(bool(getattr(self.place, i)))


if __name__ == "__main__":
    unittest.main()