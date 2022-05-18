from suitability import Suitability


class Driver:
    """
    -Constructor and helpers to deserialize a string into a Driver object
    -Properties are pre-computed to aid in code readability further down the
    pipeline, and essentially cache results (e.g. don't re-compute factors every
    time the object is used by Suitability calculator methods)
    """

    def __init__(self, raw_driver):
        self.name = raw_driver.strip()  # remove carriage returns
        self.name_length = len(self.name)
        self.vowel_count = Suitability.get_vowel_count(self.name)
        self.consonant_count = Suitability.get_consonant_count(self.name)
        self.driver_name_length = len(self.name)
        self.factors = Suitability.get_factors(self.driver_name_length)
