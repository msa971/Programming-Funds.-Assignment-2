from enum import Enum
class Location(Enum):
    exhibit1 = 1
    exhibit2 = 2
    exhibit3 = 3
    exhibit4 = 4

class Artwork:
    """class to represent artwork"""

    #constructor:
    def __init__(self, title, artist, date_of_creation, historical_importance, location):
        self.title = title
        self.artist = artist
        self.date_of_creation = date_of_creation
        self.historical_importance = historical_importance
        self.location = location

    #setter getter functions:
    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_artist(self, artist):
        self.artist = artist

    def get_artist(self):
        return self.artist

    def set_date_of_creation(self, date_of_creation):
        self.date_of_creation = date_of_creation

    def get_date_of_creation(self):
        return self.date_of_creation

    def set_historical_importance(self, historical_importance):
        self.historical_importance = historical_importance

    def get_historical_importance(self):
        return self.historical_importance

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location