import unittest
import os
import sys


current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, ".."))


sys.path.append(project_root)

from repository.text_repository import TextFileRepository
from service.text_service import TextFileService


class TestTextFileService(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_data.txt"
        self.repository = TextFileRepository(self.file_path)
        self.service = TextFileService(self.repository)

    def tearDown(self):
        import os

        os.remove(self.file_path)

    def test_read_all_data(self):
        self.repository.create("Test data 1")
        self.repository.create("Test data 2")
        result = self.service.read_all_data()
        self.assertEqual(len(result), 2)
        self.assertEqual(result, ["Test data 1\n", "Test data 2\n"])

    def test_create_data(self):
        self.service.create_data("Test data 3")
        result = self.repository.read_all()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], "Test data 3\n")

    def test_update_data(self):
        self.repository.create("Test data 1")
        self.repository.create("Test data 2")
        self.service.update_data(1, "Updated test data")
        result = self.repository.read_all()
        self.assertEqual(result[1], "Updated test data\n")

    def test_delete_data(self):
        self.repository.create("Test data 1")
        self.repository.create("Test data 2")
        self.service.delete_data(0)
        result = self.repository.read_all()
        self.assertEqual(len(result), 1)
        self.assertEqual(result, ["Test data 2\n"])

    def test_find_by_id(self):
        self.repository.create("Test data 1")
        self.repository.create("Test data 2")
        found_data = self.service.find_by_id(1)
        self.assertEqual(found_data.strip(), "Test data 2")


if __name__ == "__main__":
    unittest.main()
