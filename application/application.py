#!/usr/bin/env python3

import sys
from destination import Destination
from file_system import FileSystem

def ingest_destinations(self):
    destinations = set()
    for raw_destination in FileSystem.get_lines(destinations_path):
        destination = Destination(raw_destination)
        destinations.add(destination)
    return destinations

destinations_path = sys.argv[1]
drivers_path = sys.argv[2]

destinations = ingest_destinations(destinations_path)

print(destinations)