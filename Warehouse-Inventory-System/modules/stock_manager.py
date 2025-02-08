#Manages low-stock alerts
import heapq
class StockManager:
    def __init__(self, inventory, threshold=5): #inventory reference and low stock threshold
        self.inventory = inventory  # Store reference to the inventory
        self.threshold = threshold  # low stock threshold
        self.low_stock_queue = []  # MinHeap to track low stock items

    def check_low_stock(self):
        self.low_stock_queue=[]
        for product in self.inventory.products.values():  # Loop through all products in inventory
            if product.quantity < self.threshold:  # If product quantity is below threshold
                heapq.heappush(self.low_stock_queue, (product.quantity, product.id, product.name))
                # Add (quantity, id, name) tuple to the Min-Heap (sorted by lowest quantity first)
    
    def get_low_stock_alerts(self):
        """
        Retrieves and prints products that are low in stock.
        """
        if not self.low_stock_queue:
            print("No low stock alerts. All products are sufficiently stocked.")
            return
        
        print("\nLow Stock Alerts")
        print(f"{'Quantity':<10} {'Product ID':<10} {'Product Name':<20}")
        print("-" * 40)

        while self.low_stock_queue:
            quantity, product_id, product_name = heapq.heappop(self.low_stock_queue)  # Get the lowest stock product
            print(f"{quantity:<10} {product_id:<10} {product_name:<20}")