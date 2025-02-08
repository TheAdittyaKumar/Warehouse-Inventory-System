#Handles inventory CRUD
import csv

class Product:
    def __init__(self,id,name,quantity,category,price):
        self.id=id
        self.name=name
        self.quantity=quantity
        self.category=category
        self.price=price

    def __str__(self): # Without this printing an object would look like <__main__.Product object at 0x...>
        return f"{self.id}, {self.name}, {self.quantity}, {self.category}, ${self.price:.2f}"

class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self,id,name,quantity,category,price):
        if id in self.products: #self.products is a dictionary so if id exists the product is in there.
            self.products[id].quantity+=quantity #each product id is a key
            print(f"Product ID {id} already exists! So Updated quantity.")
        else:
            self.products[id]= Product(id, name, quantity, category, price)
            print(f"Product {name} added successfully!")
        
    def remove_product(self,id):
        if id not in self.products:
            print(f"Error! Product ID {id} does not exist so it cannot be removed.")
        else:
            del self.products[id]
            print(f"Succcess! Product ID {id} has been removed!")

    def update_product(self,id,name=None,quantity=None,category=None,price=None):
        if id in self.products:
            if name is not None:
                self.products[id].name=name
            if quantity is not None:
                self.products[id].quantity=quantity
            if category is not None:
                self.products[id].category=category
            if price is not None:
                self.products[id].price=price
            print(f"✅ Updated details for product id: {id} successfully")
        else:
            print(f"❌Product id {id} not found!")

    def search_product(self,id):
        return self.products.get(id, "Product not found")

    def list_products(self):
        if not self.products:
            print("No products are in the inventory. Time to restock.")
        print("\n--- Inventory List ---")
        # "<" this means left align for example the "ID" text in a 19 CHARACTER wide space
        print(f"{'ID':<10} {'Name':<20} {'Quantity':<10} {'Category':<15} {'Price':<10}")
        print("-" * 65)

        for product in self.products.values(): # loops through products and prints each one
            warning = " 🔴 LOW STOCK!" if product.quantity < 5 else ""
            print(f"{product.id:<10} {product.name:<20} {product.quantity:<10} {product.category:<15} ${product.price:<10.2f} {warning}")
        print("\n")
    
    ###  SAVE INVENTORY TO CSV ###
    def save_inventory(self, filename="inventory.csv"):
        """ Saves all products in the inventory to a CSV file. """
        confirm = input(f"⚠️ This will overwrite {filename}. Proceed? (yes/no): ").strip().lower()
        if confirm != "yes":
            print("❌ Save operation cancelled.")
            return
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Quantity", "Category", "Price"])  # Header row
            for product in self.products.values():
                writer.writerow([product.id, product.name, product.quantity, product.category, product.price])
        print(f"✅ Inventory saved to {filename}!")


    ### LOAD INVENTORY FROM CSV ###
    def load_inventory(self, filename="inventory.csv"):
        """ Loads products from a CSV file and reconstructs Product objects. """
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header
                for row in reader:
                    if len(row) == 5:  # Ensure correct format
                        id, name, quantity, category, price = row
                        self.products[id] = Product(id, name, int(quantity), category, float(price))
            print(f"✅ Inventory loaded from {filename}!")
        except FileNotFoundError:
            print(f"⚠️ Warning: {filename} not found! Creating a new empty inventory file.")
            open(filename, "w").close()  # Creates an empty CSV if not found
    
    def clear_inventory(self):
        """ Completely clears the inventory. """
        confirm = input("⚠️ Are you sure you want to clear all products? (yes/no): ").strip().lower()
        if confirm == "yes":
            self.products.clear()
            print("✅ Inventory has been cleared!")
        else:
            print("❌ Operation cancelled.")

