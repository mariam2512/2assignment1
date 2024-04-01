class PriceCalculator:
    def __init__(self, base_price, discount_rate, taxes, total_price):
        self.base_price = base_price
        self.discount_rate = discount_rate
        self.taxes = taxes
        self.total_price = total_price

    def get_base_price(self):
        return self.base_price

    def set_base_price(self, base_price):
        self.base_price = base_price

    def get_discount_rate(self):
        return self.discount_rate

    def set_discount_rate(self, discount_rate):
        self.discount_rate = discount_rate

    def get_taxes(self):
        return self.taxes

    def set_taxes(self, taxes):
        self.taxes = taxes

    def get_total_price(self):
        return self.total_price

    def set_total_price(self, total_price):
        self.total_price = total_price