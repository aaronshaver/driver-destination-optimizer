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
* If we wanted to scale this app up (e.g. to millions of destinations and
drivers), it's amenable to a map-reduce kind of processing. Deserializing and
doing the pre-computation of Destinations and Drivers is parallelizable. We
could have a worker whose sole job was to split up the text files. Then a worker
for just ingesting Destinations, and another for just Drivers. And then reduce/
gather that into a set of Destinations and Drivers on the other side. Likewise,
Suitability calculations could easily be map-reduced: simply partition on
Destination (or Driver, doesn't matter, it's commutative) and then feed a worker
with a bundle of Destination + all drivers (or further map into Destination +
Driver "sub-bundles", e.g. Destination1 + Drivers A,B,C on instance,
Destination1 + Drivers D,E,F on another, etc.).
* Above scaling architecture assumes a sort of ETL / batch design, like if we
get Destinations and Drivers only a few times a day. If we're receiving them on
a stream, things would be different as your sets of Destinations and Drivers
would be in constant flux and thus so would be the optimal pairings. If your
total data set is fairly small and/or your workers were very fast, maybe this
would be fine. But you might want to do something like have a "router" early in
the pipeline to segment Destination+Driver bundles by geography or other factors
(source company, trucks' ability to handle certain size loads, etc.). And then
you'd reduce processing time because you'd have different clusters of workers,
e.g. cluster for just "Oregon and Washington standardize size trucks". I'm
making some of this up, since I don't know the industry. You'd want to work
closely with customer + PM to assess where logical divisions are in the business
and thus where you could logically divide up your architecture.