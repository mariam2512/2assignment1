class Artwork:
    def __init__(self, title, artist, creation_year, historical_significance, location):
        self.title = title
        self.artist = artist
        self.creation_year = creation_year
        self.historical_significance = historical_significance
        self.location = location

    def get_title(self):
        return self.title

    def set_title(self, title):
        self.title = title

    def get_artist(self):
        return self.artist

    def set_artist(self, artist):
        self.artist = artist

    def get_creation_year(self):
        return self.creation_year

    def set_creation_year(self, creation_year):
        self.creation_year = creation_year

    def get_historical_significance(self):
        return self.historical_significance

    def set_historical_significance(self, historical_significance):
        self.historical_significance = historical_significance

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def __str__(self):
        return f"Title: {self.title}, Artist: {self.artist}, Creation Year: {self.creation_year}, Historical Significance: {self.historical_significance}, Location: {self.location}"

artwork = Artwork("Starry Night", "Vincent van Gogh", 1889, "Highly significant in art history", "New York")
print(artwork)
artwork.set_location("Paris")
artwork.set_creation_year(1888)
print(artwork)
