class Exhibition:
    """Class to represent an exhibition"""

    #constructor:
    def __init__(self, title, location):
        #the attributes are public meaning they can be seen and known by anyone.
        self.title = title
        self.location = location
        self.artwork = [] # empty list to store artwork in the exhibition.
        self.events = []  # empty list to store events in the exhibition.

    #setter getter functions:
    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def add_event(self, event): #function to add events to the exhibition.
        self.events.append(event)

    def remove_event(self, event): #function to remove events from the exhibition.
        if event in self.events:
            self.events.remove(event)

    def get_events(self):
        return self.events

    def get_details(self): #function to get details about the exhibition.
        details = f"Title: {self.title}, Location: {self.location}, Artwork: {self.artwork}"
        return details

    def update_details(self, new_details): #function to update details about the exhibition.
        for key, value in new_details.items():
            if hasattr(self, key):
                setattr(self, key, value)

    def add_artwork(self, new_artwork): #function to add artwork to the exhibition.
        self.artwork.append(new_artwork)

    def remove_artwork(self, artwork): #function to remove artwork from the exhibition.
        if artwork in self.artwork:
            self.artwork.remove(artwork)
        else:
            print("Artwork not found in the exhibition.")