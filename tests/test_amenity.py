import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.amenity import Amenity
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    def setUp(self):
        """Set up for Amenity tests"""
        self.amenity = Amenity()

    def test_amenity_inheritance(self):
        """Test that Amenity is a subclass of BaseModel"""
        self.assertIsInstance(self.amenity, BaseModel)

    def test_amenity_attributes(self):
        """Test that Amenity attributes are initialized correctly"""
        self.assertEqual(self.amenity.name, "")

    def test_amenity_initialization_with_kwargs(self):
        """Test that Amenity can be initialized with kwargs"""
        amenity = Amenity(name="WiFi")
        self.assertEqual(amenity.name, "WiFi")

    def test_amenity_id(self):
        """Test that Amenity has a unique id"""
        self.assertIsNotNone(self.amenity.id)

    def test_amenity_created_at(self):
        """Test that Amenity has a created_at attribute"""
        self.assertIsNotNone(self.amenity.created_at)

    def test_amenity_updated_at(self):
        """Test that Amenity has an updated_at attribute"""
        self.assertIsNotNone(self.amenity.updated_at)

if __name__ == "__main__":
    unittest.main()