from textbookprogram import person


class textbook():
    def __init__(self,title,first, last, age,edition,ISBN,publisher,year_published,quantity,price):
        self.title = title
        self.author = person(first, last, age)
        self.edition = edition
        self.isbn= ISBN
        self.publisher= publisher
        self.year = year_published
        self.quantity = quantity
        self.price = price


    def add_inventory(self,quantity):
        self.quantity = self.quantity + quantity

    def deduct_inventory(self,quantity):
       if self.quantity >= self.quantity:
           self.quantity = self.quantity - quantity
           return 0
       else:
           return 1

    def low_inventory(self):
        if self.quantity <= 5:
            return "Please reorder"
        else:
            return "Inventory level is adequate"
