import unittest
import os
import sys


current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, ".."))


sys.path.append(project_root)

from repository.text_repository import TextFileRepository


class TestTextFileRepository(unittest.TestCase):
    def setUp(self):
        self.file_path = "test_data.txt"
        self.repository = TextFileRepository(self.file_path)
        self.repository.create("Test data 1")
        self.repository.create("Test data 2")

    def tearDown(self):
        import os

        os.remove(self.file_path)

    def test_read_all(self):
        result = self.repository.read_all()
        self.assertEqual(len(result), 2)
        self.assertEqual(result, ["Test data 1\n", "Test data 2\n"])

    def test_create(self):
        self.repository.create("Test data 3")
        result = self.repository.read_all()
        self.assertEqual(len(result), 3)
        self.assertEqual(result[2], "Test data 3\n")

    def test_update(self):
        self.repository.update(1, "Updated test data")
        result = self.repository.read_all()
        self.assertEqual(result[1], "Updated test data\n")

    def test_delete(self):
        self.repository.delete(0)
        result = self.repository.read_all()
        self.assertEqual(len(result), 1)
        self.assertEqual(result, ["Test data 2\n"])


if __name__ == "__main__":
    unittest.main()
