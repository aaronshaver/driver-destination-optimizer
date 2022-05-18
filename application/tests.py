import unittest
from file_system import FileSystem
from destination import Destination
from suitability import Suitability
from driver import Driver
from driver_destination import DriverDestination


class AllTests(unittest.TestCase):

    # setup
    def setUp(self):
        subdir = './test_resources/'
        self.one_destination_path = subdir + 'one_destination.txt'
        self.one_driver_path = subdir + 'one_driver.txt'
        self.even_destination_path = subdir + 'even_street_name.txt'
        self.odd_destination_path = subdir + 'odd_street_name.txt'
        self.factor_5_driver_path = subdir + 'factor_5_driver.txt'
        self.factor_16_driver_path = subdir + 'factor_16_driver.txt'
        self.factor_14_driver_path = subdir + 'factor_14_driver.txt'

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

    # Driver tests
    def test_deserialize_driver_has_name(self):
        lines = FileSystem.get_lines(self.one_driver_path)
        driver = Driver(lines[0])
        self.assertEqual('Jill Kawasaki', driver.name)

    def test_deserialize_driver_has_name_length(self):
        lines = FileSystem.get_lines(self.one_driver_path)
        driver = Driver(lines[0])
        self.assertEqual(13, driver.name_length)

    def test_deserialize_driver_has_vowel_count(self):
        lines = FileSystem.get_lines(self.one_driver_path)
        driver = Driver(lines[0])
        self.assertEqual(5, driver.vowel_count)

    def test_deserialize_driver_has_driver_name_length(self):
        lines = FileSystem.get_lines(self.one_driver_path)
        driver = Driver(lines[0])
        self.assertEqual(13, driver.driver_name_length)

    def test_deserialize_driver_has_correct_factors(self):
        lines = FileSystem.get_lines(self.one_driver_path)
        driver = Driver(lines[0])
        self.assertEqual({13}, driver.factors)

    # DriverDestination tests
    def test_driverdestination_has_driver_destination_objects(self):
        lines = FileSystem.get_lines(self.one_driver_path)
        driver = Driver(lines[0])
        lines2 = FileSystem.get_lines(self.one_destination_path)
        destination = Destination(lines2[0])
        driver_destination = DriverDestination(driver, destination)
        self.assertEqual('Jill Kawasaki', driver_destination.driver.name)
        self.assertEqual(
            'Ridgemark',
            driver_destination.destination.street_name
        )

    def test_driverdestination_even_no_factors(self):
        lines = FileSystem.get_lines(self.factor_5_driver_path)
        driver = Driver(lines[0])
        lines2 = FileSystem.get_lines(self.even_destination_path)
        destination = Destination(lines2[0])
        driver_destination = DriverDestination(driver, destination)
        self.assertEqual(3, driver_destination.suitability)

    def test_driverdestination_odd_no_factors(self):
        lines = FileSystem.get_lines(self.factor_5_driver_path)
        driver = Driver(lines[0])
        lines2 = FileSystem.get_lines(self.odd_destination_path)
        destination = Destination(lines2[0])
        driver_destination = DriverDestination(driver, destination)
        self.assertEqual(2, driver_destination.suitability)

    def test_driverdestination_even_yes_factors(self):
        lines = FileSystem.get_lines(self.factor_16_driver_path)
        driver = Driver(lines[0])
        lines2 = FileSystem.get_lines(self.even_destination_path)
        destination = Destination(lines2[0])
        driver_destination = DriverDestination(driver, destination)
        self.assertEqual(11.25, driver_destination.suitability)

    def test_driverdestination_odd_yes_factors(self):
        lines = FileSystem.get_lines(self.factor_14_driver_path)
        driver = Driver(lines[0])
        lines2 = FileSystem.get_lines(self.odd_destination_path)
        destination = Destination(lines2[0])
        driver_destination = DriverDestination(driver, destination)
        self.assertEqual(10.5, driver_destination.suitability)

    # Suitability tests
    def test_get_factors_returns_correct_factors24(self):
        number = 24
        factors = Suitability.get_factors(number)
        self.assertEqual({2, 3, 4, 6, 8, 12, 24}, factors)

    def test_get_factors_returns_correct_factors7(self):
        number = 7
        factors = Suitability.get_factors(number)
        self.assertEqual({7}, factors)

    def test_vowel_count(self):
        name = 'Jill Kawasaki'
        self.assertEqual(5, Suitability.get_vowel_count(name))

    def test_consonant_count(self):
        name = 'Jill Kawasaki'
        self.assertEqual(7, Suitability.get_consonant_count(name))
