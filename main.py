from management import *

# Usage example:
if __name__ == "__main__":
    # Create products
    paracetamol = Product("Paracetamol", 8, 100, "Pain relief")
    ibuprofen = Product("Ibuprofen", 3, 200, "Anti-inflammatory")

    # Add products to inventory
    inventory = Inventory()
    inventory.add_product(paracetamol)
    inventory.add_product(ibuprofen)

    # Create a customer
    customer = Customer("Monica Nyamekye", "Plot 5 Block K, Anwomaso-Kumasi", "monicanyamekye45@gmail.com")

    # Process a sale
    sales_software = SalesSoftware(inventory)
    sales_software.process_sale(customer, ["Paracetamol", "Ibuprofen"], [5, 2], "2024-02-11")

    # Generate sales report
    sales_software.generate_sales_report()