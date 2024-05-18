import unittest
import os
import sys
from datetime import datetime
from time import sleep

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_instace_creation(self):
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_unique_id(self):
        another_model = BaseModel()
        self.assertNotEqual(self.model.id, another_model.id)

    def test_str_method(self):
        model_str = str(self.model)
        expected_str = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(model_str, expected_str)

    def test_save_method(self):
        old_updated_at = self.model.updated_at
        sleep(1)
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertGreater(self.model.updated_at, old_updated_at)

    def test_to_dict(self):
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_to_dict_contains_correct_keys(self):
        model_dict = self.model.to_dict()
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)

if __name__ == '__main__':
    unittest.main()