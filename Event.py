class Event:
    """Class to represent an event"""

    #constructor:
    def __init__(self, title, date_and_time, location, theme):
        # the attributes are public meaning they can be seen and known by anyone.
        self.title = title
        self.date_and_time = date_and_time
        self.location = location
        self.theme = theme

    #setter getter functions:
    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_date_and_time(self, date_and_time):
        self.date_and_time = date_and_time

    def get_date_and_time(self):
        return self.date_and_time

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def set_theme(self, theme):
        self.theme = theme

    def get_theme(self):
        return self.theme

    def get_details(self): #function to get the details of an event.
        details = f"Title: {self.title}, Date and Time: {self.date_and_time}, Location: {self.location}, Theme: {self.theme}"
        return details

    def update_details(self, new_details): #function to update the details of an event.
        if "title" in new_details:
            self.title = new_details["title"]
        if "date_and_time" in new_details:
            self.date_and_time = new_details["date_and_time"]
        if "location" in new_details:
            self.location = new_details["location"]
        if "theme" in new_details:
            self.theme = new_details["theme"]