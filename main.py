from management import *

# Usage example:
if __name__ == "__main__":
    # Create products
    gebedol_extra = Product("Gebedol Extra", 10, 100, "Pain relief")
    martins_liver_salt = Product("Martins Liver Salt", 5, 200, "Anti-inflammatory")

    # Add products to inventory
    inventory = Inventory()
    inventory.add_product(gebedol_extra)
    inventory.add_product(martins_liver_salt)

    # Create a customer
    customer = Customer("Monica Nyamekye", "Plot 5 Block K, Anwomaso-Kumasi", "monicanyamekye45@gmail.com")

    # Process a sale
    sales_software = SalesSoftware(inventory)
    sales_software.process_sale(customer, ["Gebedol Extra", "Martins Liver Salt"], [5, 3], "2024-02-11")

    # Generate sales report
    sales_software.generate_sales_report()