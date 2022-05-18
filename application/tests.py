import unittest
from file_system import FileSystem

class Tests(unittest.TestCase):

    def test_basic_deserialization(self):
        path = 'sample_destinations.txt'
        lines = FileSystem.get_lines(path)
        self.assertEqual('16 Ridgemark Seattle, WA 98001', lines[0])