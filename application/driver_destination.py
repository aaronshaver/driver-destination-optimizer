class DriverDestination():
    """
    An abstraction that models a potential route pairing up a driver with a
    destination
    """

    def __init__(self, driver, destination):
        self.driver = driver
        self.destination = destination
