from Person import Person, Gender
from enum import Enum

class TicketType(Enum):
    Entry = 'Standard'
    tour = 'tour'
    VIPtour = 'VIP'

class Visitor(Person):
    """class to represent a visitor"""
    def __init__(self, name, id, age, gender):
        super().__init__(name, id, age, gender) #attributes inherited from the parent class "Person".
        self.ticket_num = None
        self.ticket_type = None

    #setter getter functions:
    def set_ticket_num(self, ticket_num):
        self.ticket_num = ticket_num

    def get_ticket_num(self):
        return self.ticket_num

    def set_ticket_type(self, ticket_type):
        self.ticket_type = ticket_type

    def get_ticket_type(self):
        return self.ticket_type