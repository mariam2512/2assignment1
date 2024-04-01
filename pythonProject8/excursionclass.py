class Event:
    def __init__(self, title, date, location, duration):
        self.title = title
        self.date = date
        self.location = location
        self.duration = duration

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_date(self):
        return self.date

    def set_date(self, date):
        self.date = date

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_duration(self):
        return self.duration

    def set_duration(self, duration):
        self.duration = duration

    def __str__(self):
        return f"Title: {self.title}, Date: {self.date}, Location: {self.location}, Duration: {self.duration}"

class Occasions(Event):
    def __init__(self, title, date, location, duration, ticket_price):
        super().__init__(title, date, location, duration)
        self.ticket_price = ticket_price

    def get_ticket_price(self):
        return self.ticket_price

    def set_ticket_price(self, ticket_price):
        self.ticket_price = ticket_price

    def __str__(self):
        return super().__str__() + f", Ticket Price: {self.ticket_price}"

class Excursion(Event):
    def __init__(self, title, date, location, duration, guide, group_size):
        super().__init__(title, date, location, duration)
        self.guide = guide
        self.group_size = group_size

    def get_guide(self):
        return self.guide

    def set_guide(self, guide):
        self.guide = guide

    def get_group_size(self):
        return self.group_size

    def set_group_size(self, group_size):
        self.group_size = group_size

    def __str__(self):
        return super().__str__() + f", Guide: {self.guide}, Group Size: {self.group_size}"