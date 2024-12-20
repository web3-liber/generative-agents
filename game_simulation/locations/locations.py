class Location:
    """
    A class to represent a location in the simulated environment.

    Attributes:
    ----------
    name : str
        The name of the location.
    description : str
        A brief description of the location.

    Methods:
    -------
    describe():
        Prints the description of the location.
    """

    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return self.name
    
    def describe(self):
        print(self.description)

class Locations:
    """
    A class to represent a collection of locations in the simulated environment.

    Attributes:
    ----------
    locations : dict
        A dictionary of locations, with keys as the location names and values as Location objects.

    Methods:
    -------
    add_location(name, description):
        Adds a new location to the collection.
    
    get_location(name):
        Returns the Location object with the given name.
    
    __str__():
        Returns a string representation of the collection of locations.
    """
    
    def __init__(self):
        self.locations = {}

    def add_location(self, name, description):
        self.locations[name] = Location(name, description)

    def get_location(self, name):
        return self.locations.get(name)

    def __str__(self):
        return '\n'.join([str(location) for location in self.locations.values()])

if __name__ == "__main__":
    print("---- test: Locations ----")    

    # Create an instance of Locations to manage a collection of locations
    location_manager = Locations()

    # Add some locations to the manager
    location_manager.add_location("Forest", "A dense and mysterious forest full of tall trees and wildlife.")
    location_manager.add_location("Cave", "A dark and damp cave, home to bats and other creatures.")
    location_manager.add_location("Village", "A small, peaceful village at the foot of a mountain.")
    
    # Print out all locations
    print("All Locations:")
    print(location_manager)  # Should list the names of all locations

    # Get a specific location and describe it
    forest = location_manager.get_location("Forest")
    if forest:
        print("\nDescription of Forest:")
        forest.describe()  # Should print description of the Forest
    
    # Get a location that doesn't exist
    unknown_location = location_manager.get_location("Desert")
    if unknown_location:
        unknown_location.describe()
    else:
        print("\nNo such location: Desert")

