import unittest
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.state import State
from models.base_model import BaseModel

class TestState(unittest.TestCase):
    def setUp(self):
        """Set up for State tests"""
        self.state = State()

    def test_state_inheritance(self):
        """Test that State is a subclass of BaseModel"""
        self.assertIsInstance(self.state, BaseModel)

    def test_state_attributes(self):
        """Test that State attributes are initialized correctly"""
        self.assertEqual(self.state.name, "")

    def test_state_initialization_with_kwargs(self):
        """Test that State can be initialized with kwargs"""
        state = State(name="California")
        self.assertEqual(state.name, "California")

    def test_state_id(self):
        """Test that State has a unique id"""
        self.assertIsNotNone(self.state.id)

    def test_state_created_at(self):
        """Test that State has a created_at attribute"""
        self.assertIsNotNone(self.state.created_at)

    def test_state_updated_at(self):
        """Test that State has an updated_at attribute"""
        self.assertIsNotNone(self.state.updated_at)

if __name__ == "__main__":
    unittest.main()
