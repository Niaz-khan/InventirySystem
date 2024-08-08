class Item:
    def __init__(self, name, price, quantity):
        self.item_name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Item: {self.item_name}, Price: {self.price}, Quantity: {self.quantity}"
