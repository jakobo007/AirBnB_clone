import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.city import City
from models.base_model import BaseModel

class TestCity(unittest.TestCase):
    def setUp(self):
        """Set up for City tests"""
        self.city = City()

    def test_city_inheritance(self):
        """Test that City is a subclass of BaseModel"""
        self.assertIsInstance(self.city, BaseModel)

    def test_city_attributes(self):
        """Test that City attributes are initialized correctly"""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_city_initialization_with_kwargs(self):
        """Test that City can be initialized with kwargs"""
        city = City(state_id="1234", name="San Francisco")
        self.assertEqual(city.state_id, "1234")
        self.assertEqual(city.name, "San Francisco")

    def test_city_id(self):
        """Test that City has a unique id"""
        self.assertIsNotNone(self.city.id)

    def test_city_created_at(self):
        """Test that City has a created_at attribute"""
        self.assertIsNotNone(self.city.created_at)

    def test_city_updated_at(self):
        """Test that City has an updated_at attribute"""
        self.assertIsNotNone(self.city.updated_at)

if __name__ == "__main__":
    unittest.main()