#Manages order processing (FIFO)
from collections import deque
import csv
from modules.file_handler import save_orders, load_orders

class Order:
    def __init__(self,order_id,product_id,quantity):
        self.order_id=order_id
        self.product_id=product_id
        self.quantity=quantity
    def __str__(self):
        return f"Order ID: {self.order_id}, Product ID: {self.product_id}, Quantity: {self.quantity}"

class OrderQueue:
    def __init__(self):
        self.orders=deque() #fifo queue to store orders
        load_orders(self)  # Load orders from CSV on startup

    
    def add_order(self,order_id,product_id,quantity): #every order has order_id, product_id and quantity.
        order= Order(order_id, product_id, quantity) #Calls the Order constructor (__init__) to create an Order object and stores it in a variable called order
        self.orders.append(order) #add order to the queue (FIFO)
        print(f"Order {order_id} has been added to the queue!")
        #orders.add_order("O001", "P001", 5)  # Add first order
        save_orders(self)  # Save orders after adding

    def process_order(self, inventory):
        if not self.orders:
            print("🚫 No pending orders to process.")
            return
        print("📋 Current Order Queue:")  # Debug: Print orders in queue before processing
        for order in self.orders:
            print(f"🔹 Order {order.order_id} -> Product {order.product_id} (Quantity: {order.quantity})")
        order = self.orders.popleft()  # FIFO: Retrieve first order
        print(f"\n🔍 Attempting to process Order: {order.order_id} for Product: {order.product_id}")
        product = inventory.products.get(order.product_id)  # 🔍 Find product by ID
        if product:
            print(f"📦 Found Product: {product.name}, Stock: {product.quantity}")  # Debugging
        else:
            print(f"⚠️ Product ID {order.product_id} not found in inventory!")
        if product and product.quantity >= order.quantity:
            product.quantity -= order.quantity  # Reduce stock
            print(f"✅ Order {order.order_id} processed! {order.quantity} units of {product.name} shipped.")
        else:
            print(f"⚠️ Order {order.order_id} cannot be processed due to insufficient stock.")
            self.orders.appendleft(order)  # Re-add order if failed

    def save_orders(self):    
        save_orders(self)  # Save orders after processing
        #inventory = Inventory()
        #inventory.add_product("P001", "Laptop", 10, "Electronics", 25000)

    def view_pending_orders(self):
        """ Displays all pending orders in the queue. """
        if not self.orders:
            print("No pending orders.")
            return

        print("\n--- Pending Orders ---")
        for order in self.orders:
            print(order)
        print("\n")
    