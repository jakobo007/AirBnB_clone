import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.user import User
from models.base_model import BaseModel

class TestUser(unittest.TestCase):
    def setUp(self):
        """Set up for User tests"""
        self.user = User()

    def test_user_inheritance(self):
        """Test that User is a subclass of BaseModel"""
        self.assertIsInstance(self.user, BaseModel)

    def test_user_attributes(self):
        """Test that User attributes are initialized correctly"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_user_initialization_with_kwargs(self):
        """Test that User can be initialized with kwargs"""
        user = User(email="user@example.com", password="pass123", first_name="John", last_name="Doe")
        self.assertEqual(user.email, "user@example.com")
        self.assertEqual(user.password, "pass123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_user_id(self):
        """Test that User has a unique id"""
        self.assertIsNotNone(self.user.id)

    def test_user_created_at(self):
        """Test that User has a created_at attribute"""
        self.assertIsNotNone(self.user.created_at)

    def test_user_updated_at(self):
        """Test that User has an updated_at attribute"""
        self.assertIsNotNone(self.user.updated_at)

if __name__ == "__main__":
    unittest.main()
