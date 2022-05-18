#!/usr/bin/env python3

import sys
from driver_destination import DriverDestination
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

def construct_driver_destinations(drivers, destinations):
    driver_destinations = []
    for driver in drivers:
        for destination in destinations:
            driver_destination = DriverDestination(driver, destination)
            driver_destinations.append(driver_destination)
    driver_destinations.sort(key=lambda x: x.suitability, reverse=True)
    return driver_destinations

drivers_path = sys.argv[1]
destinations_path = sys.argv[2]

drivers = ingest_drivers(drivers_path)
destinations = ingest_destinations(destinations_path)

driver_destinations = construct_driver_destinations(drivers, destinations)

total_suitability = 0
highest_suitability_pairs = []
for driver_destination in driver_destinations:
    # if both driver and destination are still available, we can pair them and
    # then remove them both from future consideration
    if driver_destination.driver in drivers and driver_destination.destination \
        in destinations:
        drivers.remove(driver_destination.driver)
        destinations.remove(driver_destination.destination)
        total_suitability += driver_destination.suitability
        highest_suitability_pairs.append(driver_destination)

print("Total suitability:", total_suitability)
for driver_destination in highest_suitability_pairs:
    print("{} : {}".format(
        driver_destination.destination.address,
        driver_destination.driver.name
    ))
