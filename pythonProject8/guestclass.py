from enum import Enum

class TicketType(Enum):
    Regular = 1
    Child = 2
    Teacher_Student = 3
    Senior = 4
    Group = 5

class Guest:
    def __init__(self, name, age, national_id, ticket_type, ticket_price, ticket_location, ticket_details):
        self.name = name
        self.age = age
        self.national_id = national_id
        self.ticket_type = ticket_type
        self.ticket_price = ticket_price
        self.ticket_location = ticket_location
        self.ticket_details = ticket_details

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_national_id(self):
        return self.national_id

    def set_national_id(self, national_id):
        self.national_id = national_id

    def get_ticket_type(self):
        return self.ticket_type

    def set_ticket_type(self, ticket_type):
        self.ticket_type = ticket_type

    def get_ticket_price(self):
        return self.ticket_price

    def set_ticket_price(self, ticket_price):
        self.ticket_price = ticket_price

    def get_ticket_location(self):
        return self.ticket_location

    def set_ticket_location(self, ticket_location):
        self.ticket_location = ticket_location

    def get_ticket_details(self):
        return self.ticket_details

    def set_ticket_details(self, ticket_details):
        self.ticket_details = ticket_details

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, National ID: {self.national_id}, Ticket Type: {self.ticket_type.name}, Ticket Price: {self.ticket_price}, Ticket Location: {self.ticket_location}, Ticket Details: {self.ticket_details}"