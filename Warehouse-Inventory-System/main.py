# Entry point CLI
import sys
sys.stdout.reconfigure(encoding='utf-8')  # ✅ Force UTF-8 encoding

import os

# 🔹 Ensure the `modules` directory is added to Python's path
sys.path.append(os.path.join(os.path.dirname(__file__), "modules"))

# Now import modules
from modules.inventory import Inventory
from modules.order_queue import OrderQueue
from modules.stock_manager import StockManager
from modules.warehouse_graph import WarehouseGraph
from modules.file_handler import save_orders, load_orders

# Initialize Components
warehouse = Inventory()
orders = OrderQueue()
stock_alerts = StockManager(warehouse)
warehouse_map = WarehouseGraph()

# Load Data from CSV
load_orders(orders)  # 🔹 Use load_orders() directly

def main_menu():
    """ Displays the main menu and handles user input. """
    while True:
        print("\n📦 WAREHOUSE MANAGEMENT SYSTEM")
        print("1️⃣ Add Product")
        print("2️⃣ View Inventory")
        print("3️⃣ Place Order")
        print("4️⃣ Process Order")
        print("5️⃣ Check Low Stock")
        print("6️⃣ Find Shortest Path to Shelf")
        print("7️⃣ Save & Exit")
        choice = input("Select an option: ")

        if choice == "1":
            id = input("Product ID: ")
            name = input("Product Name: ")
            quantity = int(input("Quantity: "))
            category = input("Category: ")
            price = float(input("Price: "))
            warehouse.add_product(id, name, quantity, category, price)

        elif choice == "2":
            warehouse.list_products()

        elif choice == "3":
            order_id = input("Order ID: ")
            product_id = input("Product ID: ")
            quantity = int(input("Quantity: "))
            orders.add_order(order_id, product_id, quantity)

        elif choice == "4":
            orders.process_order(warehouse)

        elif choice == "5":
            stock_alerts.check_low_stock()
            stock_alerts.get_low_stock_alerts()

        elif choice == "6":
            start_shelf = input("Enter starting shelf: ")
            target_shelf = input("Enter target shelf: ")
            path, distance = warehouse_map.shortest_path(start_shelf, target_shelf)
            if path:
                print(f"📍 Shortest Path: {path}, Distance: {distance}")
            else:
                print("⚠️ No valid path found.")

        elif choice == "7":
            save_orders(orders)  # 🔹 Use save_orders() directly
            print("✅ Data saved. Exiting program.")
            break
        else:
            print("❌ Invalid option. Please try again.")

# Run the Warehouse System
main_menu()
