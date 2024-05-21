import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """Set up for FileStorage tests"""
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path
        self.obj = BaseModel()
        self.obj.id = "test_id"
        self.obj_attr = {
            "__class__": "BaseModel",
            "id": "test_id",
            "created_at": self.obj.created_at.isoformat(),
            "updated_at": self.obj.updated_at.isoformat()
        }

    def tearDown(self):
        """Clean up after FileStorage tests"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_initialization(self):
        """Test FileStorage initialization"""
        self.assertTrue(isinstance(self.storage, FileStorage))

    def test_all(self):
        """Test all method"""
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        """Test new method"""
        self.storage.new(self.obj)
        key = f"{self.obj.__class__.__name__}.{self.obj.id}"
        self.assertEqual(self.storage.all()[key].to_dict(), self.obj.to_dict())

    def test_save_and_reload(self):
        """Test save and reload methods"""
        self.storage.new(self.obj)
        self.storage.save()
        new_storage = FileStorage()
        new_storage._FileStorage__file_path = self.file_path
        new_storage.reload()
        key = f"{self.obj.__class__.__name__}.{self.obj.id}"
        self.assertEqual(new_storage.all()[key].to_dict(), self.obj.to_dict())

    def test_get_class_dict(self):
        """Test get_class_dict method"""
        classes = self.storage.get_class_dict()
        self.assertEqual(len(classes), 7)  # Check if all expected classes are loaded
        self.assertTrue("BaseModel" in classes)
        self.assertTrue("User" in classes)
        # Add similar checks for other classes

if __name__ == "__main__":
    unittest.main()