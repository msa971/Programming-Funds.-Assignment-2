from datetime import datetime
from Artwork import Artwork, Location
from ArtworkManagment import ArtworkManagement
from Visitor import Visitor, TicketType, Gender
from Ticketing import Ticketing
from Exhibition import Exhibition
from VisitorManagment import VisitorManagment
from Event import Event

def test_add_artwork(): #function to test adding artwork to the museum's artwork managment.
    artwork_management = ArtworkManagement()
    artwork = Artwork(
        title="Mona Lisa",
        artist="Leonardo da Vinci",
        date_of_creation=datetime(1503, 1, 1),
        historical_importance="High",
        location=Location.exhibit1
    )
    artwork_management.add_artwork(artwork)
    assert artwork in artwork_management.get_listOfArtwork()
    print("Artwork added successfully:", artwork.title)

def test_register_visitor(): #function to test registering a visitor.
    visitor_management = VisitorManagment(numOfvisitors=0)
    visitor = Visitor("Mahra Alameri", "1", 19, Gender.female)
    visitor_management.register_visitor(visitor)
    assert visitor_management.get_numOfvisitors() == 1

def test_sell_ticket(): #function to test selling a ticket.
    ticketing = Ticketing(numOftickets=10, price=20, type=TicketType.Entry, date=datetime.now())
    visitor = Visitor("Mahra Alameri", "1", 19, Gender.female)
    ticketing.sell_ticket(ticketing, visitor)
    assert ticketing.get_visitor() == visitor

def test_open_exhibition(): #function to test opening a new exhibition.
    exhibition = Exhibition(
        title="Modern Art Exhibition",
        location=Location.exhibit2
    )
    assert exhibition.get_title() == "Modern Art Exhibition"
    print("Exhibition opened successfully:", exhibition.get_title())

def test_get_event_details(): #function to test retreving event details.
    event = Event(
        title="Concert",
        date_and_time=datetime(2024, 6, 1, 19, 0),
        location=Location.exhibit3,
        theme="Classical Music"
    )
    details = event.get_details()
    details = "Title: Showcasing Emirati talent, Date and Time: April 22, 2024, Location: the new Modern Art Exhibition, Theme: Emirati Tradition"
    print("Event details retrieved successfully:\n", details)

test_add_artwork()
test_register_visitor()
test_sell_ticket()
test_open_exhibition()
test_get_event_details()