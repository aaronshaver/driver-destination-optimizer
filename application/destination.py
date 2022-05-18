from suitability import Suitability

class Destination():
    """
    -Constructor and helpers to deserialize a string into a Destination object
    -Properties are pre-computed to aid in code readability further down the
    pipeline, and essentially cache results (e.g. don't re-compute factors every
    time the object is used by Suitability calculator methods)
    """

    def __init__(self, raw_destination):
        """Takes in raw string, builds Destination object"""
        self.address = raw_destination.strip()  # remove carriage returns
        self.street_name = self.get_street_name(self.address)
        self.street_name_length = len(self.street_name)
        self.is_even = self.get_is_even(self.street_name_length)
        self.factors = Suitability.get_factors(self.street_name_length)

    def get_street_name(self, address):
        """Extracts street name portion from raw address"""
        return address.split()[1]

    def get_is_even(self, length):
        """Gets parity of street name length, e.g. 2 == True, 3 == False"""
        return length % 2 == 0
