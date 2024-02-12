# A Class for the product
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

# A Class for taking inventory
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

# A Class for the Customer
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

# A Class for the Transaction
class Transaction:
    def __init__(self, date, customer, inventory):
        self.date = date
        self.customer = customer
        self.products_bought = {}
        self.inventory = inventory

    def add_product(self, product, quantity):
        if product.name in self.products_bought:
            self.products_bought[product.name] += quantity
        else:
            self.products_bought[product.name] = quantity

    def calculate_total(self):
        total = 0
        for product_name, quantity in self.products_bought.items():
            product = self.search_product_in_inventory(product_name)
            if product:
                total += product.price * quantity
        return total

    def search_product_in_inventory(self, name):
        for product in self.inventory.products:
            if product.name == name:
                return product
        return None

# A Class for Recording Sales
class SalesRecord:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def generate_report(self):
        for transaction in self.transactions:
            print(f"Date: {transaction.date}")
            print(f"Customer: {transaction.customer.name}")
            print("Products Bought: ")
            for product_name, quantity in transaction.products_bought.items():
                print(f"- {product_name}: {quantity}")
            print(f"Total: ₵{transaction.calculate_total()}\n")

# A Class for the Sales Software
class SalesSoftware:
    def __init__(self, inventory=None, sales_record=None):
        self.inventory = inventory if inventory else Inventory()
        self.sales_record = sales_record if sales_record else SalesRecord()

    def process_sale(self, customer, products, quantities, date):
        transaction = Transaction(date, customer, self.inventory)
        for idx in range(len(products)):
            product_name = products[idx]
            quantity = quantities[idx]
            product = self.inventory.search_product(product_name)
            if product:
                cost = customer.purchase_product(product, quantity)
                if cost > 0:
                    transaction.add_product(product, quantity)
                    print(f"Added {quantity} {product.name}(s) to the transaction")
                else:
                    print(f"Not enough stock available for {product_name}")
            else:
                print(f"{product_name} not found in inventory")

        self.sales_record.add_transaction(transaction)

    def generate_receipt(self, transaction):
        print("Receipt:")
        print(f"Date: {transaction.date}")
        print(f"Customer: {transaction.customer.name}")
        print("Products Bought:")
        total_cost = 0
        for product_name, quantity in transaction.products_bought.items():
            product = self.inventory.search_product(product_name)
            if product:
                total_cost += product.price * quantity
                print(f"- {product.name}: {quantity}")
        print(f"Total: ₵{total_cost}")

    def generate_sales_report(self):
        self.sales_record.generate_report()