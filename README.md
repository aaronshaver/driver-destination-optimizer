# driver-destination-optimizer

Constructs driver + destination combinations (pairs), then optimizes for highest
total suitability, while never using a driver or destination more than once

## Installation

1. Install Docker if it doesn't exist on your local machine. This will ensure the same dependencies
as when the app was developed. Download here: https://www.docker.com/get-started/
1. On the terminal, clone this repository (`git clone git@github.com:aaronshaver/driver-destination-optimizer.git`) in a local directory
1. `cd` into the new directory, e.g. `cd driver-destination-optimizer`
1. `docker build -t optimizer .`

## Usage

1. `docker container run -it optimizer /bin/bash`
1. Run unit tests: `python3 -m unittest discover .`
1. Run application: `python3 application.py sample_drivers.txt sample_destinations.txt`

(NOTE: argument order matters! Since we're not dealing with normalized and typed objects
(Drivers and Destinations are really just string blobs), you can input Drivers as
Destinations or vice-versa and get output, but it'll be wrong)

## Design considerations

* I chose Python because it's the language I typically use for live DS/A code
screens (since it's terse, expressive, and readable with low boilerplate), and
it works fine for small projects too. I could have done Java just as easily.
Maybe it would have been nice to do Stream API stuff where Suitability
calculation could have been a small block of .filter()s and .map()s and we could
use .parallelStream() for high performance. But that'd likely be overkill for a
small project.
* The exercise document said "You do not need to worry about malformed input" so I
didn't bother with a lot of error handling, but normally I'd enumerate all the
error conditions I could think of -- empty files, check for Driver and
Destination being well-formed (i.e. don't trust inputs) and check for zero
lengths or names that don't have vowels or consonants, etc. -- and return nice
error messages to the user (or have logic to skip malformed entities and move
on with partial data)
* Exercise didn't strongly specify output format, so just for fun, I made the
output be in valid CSV format, and include the suitability of individual
driver-destination pairings; this had a nice side benefit of being able to
quickly see if they added up to the correct total
* In reality, address verification is a difficult problem and kind of a science
unto itself. I didn't bother building a complex object for addresses, just did a
tiny simulation of extracting a street name from an address in
Destination.get_street_name() to hint at the complexity involved. Likewise,I
thought about abstracting "street name" into its own class but it felt like
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
Driver "sub-bundles", e.g. Destination1 + Drivers A,B,C on one instance/worker,
Destination1 + Drivers D,E,F on another, etc.).
* Above scaling architecture assumes a sort of ETL / batch design, like if we
get Destinations and Drivers only a few times a day. If we're receiving them on
a stream, things would be different as your sets of Destinations and Drivers
would be in constant flux and thus so would be the optimal pairings. If your
total data set is fairly small and/or your workers were very fast, maybe this
would be fine.
* But you might want to do something like have a "router" early in
the pipeline to segment Destination+Driver bundles by geography or other factors
(source company, trucks' ability to handle certain size loads, etc.). And then
you'd reduce processing time because you'd have different clusters of workers,
e.g. cluster for just "Oregon and Washington standard-size trucks". I'm
making some of this up, since I don't know the industry. You'd want to work
closely with customer + PM to assess where logical divisions are in the business
and thus where you could logically divide up your architecture.
* We could DRY-up the classes a little bit more since there's common
functionality, e.g. Driver and Destination lengths, factors. You could do
something like have an Entity base class and inherit from that, but it feels
over-engineered. I try to follow "Rule of three" when refactoring and there just
isn't enough benefit in this case IMO.
* Stuff like 1.5 for even + vowels Suitability should probably be configurable
in a settings file, but I wasn't sure the exercise called for that level of
customization so I kept it simple
* I tried to use static classes and methods where possible to reduce the amount
of `object = Object(); object.doStuff()` repetitive fluff
* Time complexity would seem to be O(n*m) where n is number of destinations and
m is number of drivers. [Edit: this was incorrect: the naive algorithm is O(n!); the correct way to optimize down from there is to use the Hungarian algorithm (AKA Munkres assignment algorithm) which leads to a worst case of O(n^3).] I keep thinking there must be a way to improve on this.
Obviously even street name Destinations will tend to be more valuable, but you
could just as easily get an odd Destination that just so happened to pair with
a Driver with lots of consonants and/or that plus common factors. If this were
a large-scale data set and for some reason realtime speed were of the essence,
you could maybe do a statistical sampling of the Destinations and Drivers to
get a "good enough" approximiation of best Suitability, sorting even
Destinations, high vowel counts, and high consonant counts toward the top of the
heap. I might be missing something obvious and there could be a clever way to
reduce the number of drivers and/or destinations considered.
