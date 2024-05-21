import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.place import Place
from models.base_model import BaseModel

class TestPlace(unittest.TestCase):
    def setUp(self):
        """Set up for Place tests"""
        self.place = Place()

    def test_place_inheritance(self):
        """Test that Place is a subclass of BaseModel"""
        self.assertIsInstance(self.place, BaseModel)

    def test_place_attributes(self):
        """Test that Place attributes are initialized correctly"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_place_initialization_with_kwargs(self):
        """Test that Place can be initialized with kwargs"""
        place = Place(
            city_id="1234", user_id="5678", name="My Place", 
            description="A nice place", number_rooms=2, number_bathrooms=1, 
            max_guest=4, price_by_night=100, latitude=37.7749, longitude=-122.4194, 
            amenity_ids=["wifi", "pool"]
        )
        self.assertEqual(place.city_id, "1234")
        self.assertEqual(place.user_id, "5678")
        self.assertEqual(place.name, "My Place")
        self.assertEqual(place.description, "A nice place")
        self.assertEqual(place.number_rooms, 2)
        self.assertEqual(place.number_bathrooms, 1)
        self.assertEqual(place.max_guest, 4)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ["wifi", "pool"])

    def test_place_id(self):
        """Test that Place has a unique id"""
        self.assertIsNotNone(self.place.id)

    def test_place_created_at(self):
        """Test that Place has a created_at attribute"""
        self.assertIsNotNone(self.place.created_at)

    def test_place_updated_at(self):
        """Test that Place has an updated_at attribute"""
        self.assertIsNotNone(self.place.updated_at)

if __name__ == "__main__":
    unittest.main()