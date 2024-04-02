from Artwork import Artwork

class ArtworkManagement:
    """class to represent artwork managment"""

    #constructor:
    def __init__(self):
        self.listOfArtwork = []  # List to hold instances of Artwork

    #setter getter functions:
    def set_listOfArtwork(self):
        self.listOfArtwork = listOfArtwork

    def get_listOfArtwork(self):
        return self.listOfArtwork

    def add_artwork(self, new_artwork): #function to add artwork to the museum's artwork managment.
        self.listOfArtwork.append(new_artwork)

    def remove_artwork(self, artwork): #function to remove artwork from the museum's artwork managment
        self.listOfArtwork.remove(new_artwork)

    def update_location(self, new_location): #function to update the location of the artwork.
        self.location = new_location