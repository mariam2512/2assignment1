class Ticket:
    def __init__(self, visitor, event, price):
        self.visitor = visitor
        self.event = event
        self.price = price

    def get_visitor(self):
        return self.visitor

    def set_visitor(self, visitor):
        self.visitor = visitor

    def get_event(self):
        return self.event

    def set_event(self, event):
        self.event = event

    def get_price(self):
        return self.price

    def set_price(self, price):
        self.price = price

    def __str__(self):
        return f"Visitor: {self.visitor}, Event: {self.event}, Price: {self.price}"