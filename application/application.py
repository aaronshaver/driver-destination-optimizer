#!/usr/bin/env python3

import sys
from destination import Destination
from file_system import FileSystem
from driver import Driver

def ingest_destinations(path):
    destinations = set()
    for raw_destination in FileSystem.get_lines(destinations_path):
        destination = Destination(raw_destination)
        destinations.add(destination)
    return destinations

def ingest_drivers(path):
    drivers = set()
    for raw_driver in FileSystem.get_lines(path):
        driver = Driver(raw_driver)
        drivers.add(driver)
    return drivers

drivers_path = sys.argv[1]
destinations_path = sys.argv[2]

drivers = ingest_drivers(drivers_path)
destinations = ingest_destinations(destinations_path)

print(drivers)
print(destinations)