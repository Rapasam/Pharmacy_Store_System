#A Class for the product
class Product:
    def __init__(self, name, price, quantity, description):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity
    
    def get_details(self):
        return f"{self.name}: {self.description}, ₵{self.price}, {self.quantity} available."

#A Class for taking inventory
class Inventory:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)

    def remove_product(self, product):
        self.products.remove(product)
    
    def search_product(self, name):
        for product in self.products:
            if product.name == name:
                return product
        return None

#A Class for the Customer
class Customer:
    def __init__(self, name, address, contact):
        self.name = name
        self.address = address
        self.contact = contact

    def purchase_product(self, product, quantity):
        if product.quantity >= quantity:
            product.update_quantity(product.quantity - quantity)
            return product.price * quantity
        else:
            return 0

