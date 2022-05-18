import unittest
from file_system import FileSystem
from destination import Destination
from suitability import Suitability

class Tests(unittest.TestCase):

    # setup
    def setUp(self):
        subdir = './test_resources/'
        self.one_destination_path = subdir + 'one_destination.txt'

        return super().setUp()

    # file system tests
    def test_basic_deserialization(self):
        lines = FileSystem.get_lines(self.one_destination_path)
        self.assertEqual('16 Ridgemark Seattle, WA 98001', lines[0])

    # Destination tests
    def test_deserialize_destination_has_address(self):
        lines = FileSystem.get_lines(self.one_destination_path)
        destination = Destination(lines[0])
        self.assertEqual('16 Ridgemark Seattle, WA 98001', destination.address)

    def test_deserialize_destination_has_address(self):
        lines = FileSystem.get_lines(self.one_destination_path)
        destination = Destination(lines[0])
        self.assertEqual('16 Ridgemark Seattle, WA 98001', destination.address)

    def test_deserialize_destination_has_street_name(self):
        lines = FileSystem.get_lines(self.one_destination_path)
        destination = Destination(lines[0])
        self.assertEqual('Ridgemark', destination.street_name)

    def test_deserialize_destination_has_street_name_length(self):
        lines = FileSystem.get_lines(self.one_destination_path)
        destination = Destination(lines[0])
        self.assertEqual(9, destination.street_name_length)

    def test_deserialize_destination_has_street_name_length(self):
        lines = FileSystem.get_lines(self.one_destination_path)
        destination = Destination(lines[0])
        self.assertEqual(False, destination.is_even)

    def test_deserialize_destination_has_correct_factors(self):
        lines = FileSystem.get_lines(self.one_destination_path)
        destination = Destination(lines[0])
        self.assertEqual({3, 9}, destination.factors)

    # Suitability tests
    def test_get_factors_returns_correct_factors(self):
        number = 24
        factors = Suitability.get_factors(number)
        self.assertEqual({2, 3, 4, 6, 8, 12, 24}, factors)
