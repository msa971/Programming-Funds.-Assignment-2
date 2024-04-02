from Visitor import Visitor, TicketType

class Ticketing:
    """class to represent the ticketing process"""

    #constructor:
    def __init__(self, numOftickets, price, type, date):
        #the attributes are public meaning they can be seen and known by anyone.
        self.numOftickets = numOftickets #This refers to the number of tickets sold.
        self.price = price
        self.type = type
        self.date = date
        self.visitor = None  # Initialize visitor attribute as None as their is an association relation.

    #setter getter functions:
    def set_numOftickets(self, numOftickets):
        self.numOftickets = numOftickets

    def get_numOftickets(self):
        return self.numOftickets

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def set_type(self, type):
        self.type = type

    def get_type(self):
        return self.type

    def set_date(self, date):
        self.date = date

    def get_date(self):
        return self.date

    def set_visitor(self, visitor):
        self.visitor = visitor

    def get_visitor(self):
        return self.visitor

    def sell_ticket(self, ticket, visitor): #function to sell a ticket
        self.set_visitor(visitor)
        print(f"Ticket sold to {visitor.get_name()} for {self.price}$")