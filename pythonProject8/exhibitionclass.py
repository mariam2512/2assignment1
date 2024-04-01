class Exhibition:
    def __init__(self, name, location, items_displayed):
        self.name = name
        self.location = location
        self.items_displayed = items_displayed

    def __str__(self):
        return f"Exhibition: {self.name}, Location: {self.location}, Items Displayed: {self.items_displayed}"