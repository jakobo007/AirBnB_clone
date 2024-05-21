import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.review import Review
from models.base_model import BaseModel

class TestReview(unittest.TestCase):
    def setUp(self):
        """Set up for Review tests"""
        self.review = Review()

    def test_review_inheritance(self):
        """Test that Review is a subclass of BaseModel"""
        self.assertIsInstance(self.review, BaseModel)

    def test_review_attributes(self):
        """Test that Review attributes are initialized correctly"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_review_initialization_with_kwargs(self):
        """Test that Review can be initialized with kwargs"""
        review = Review(place_id="1234", user_id="5678", text="Great place!")
        self.assertEqual(review.place_id, "1234")
        self.assertEqual(review.user_id, "5678")
        self.assertEqual(review.text, "Great place!")

    def test_review_id(self):
        """Test that Review has a unique id"""
        self.assertIsNotNone(self.review.id)

    def test_review_created_at(self):
        """Test that Review has a created_at attribute"""
        self.assertIsNotNone(self.review.created_at)

    def test_review_updated_at(self):
        """Test that Review has an updated_at attribute"""
        self.assertIsNotNone(self.review.updated_at)

if __name__ == "__main__":
    unittest.main()
