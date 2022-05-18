# driver-destination-optimizer

Optimizes destination + driver combinations for maximum total suitability

## Installation

1. Install Docker if it doesn't exist on your local machine. This will ensure the same dependencies
as when the app was developed. Download here: https://www.docker.com/get-started/
1. On the terminal, clone this repository (`git clone git@github.com:aaronshaver/driver-destination-optimizer.git`) in a local directory
1. `cd` into the new directory, e.g. `cd driver-destination-optimizer`
1. `docker build -t optimizer .`

## Usage

1. `docker container run -it optimizer /bin/bash`
1. Run unit tests: `python3 -m unittest discover .`
1. Run application: `python3 application.py sample_destinations.txt sample_drivers.txt`

## Design considerations

* In reality, address verification is a difficult problem and kind of a science
unto itself. I didn't bother building a complex object for addresses, just did a
tiny simulation of extracting a street name from an address in
Destination.get_street_name() to hint at the complexity involved.
* I thought about abstracting "street name" into its own class but it felt like
over-engineering. If we expected to do much more complex logic with it, an
argument could be made and refactoring done in the future.


