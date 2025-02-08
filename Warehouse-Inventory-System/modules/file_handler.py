import csv
import os

def save_orders(order_queue, filename="data/orders.csv"):
    """ Saves pending orders to a CSV file. """
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["OrderID", "ProductID", "Quantity"])  # Header row
        for order in order_queue.orders:
            writer.writerow([order.order_id, order.product_id, order.quantity])
    print(f"✅ Orders saved to {filename}!")

def load_orders(order_queue, filename="data/orders.csv"):
    """ Loads pending orders from a CSV file safely. """
    from modules.order_queue import Order  # ✅ Import moved inside function to avoid circular import

    if not os.path.exists(filename) or os.stat(filename).st_size == 0:
        print(f"⚠️ {filename} is empty or missing. No orders loaded.")
        return

    try:
        with open(filename, "r") as file:
            reader = csv.reader(file)
            header = next(reader, None)  # ✅ Avoid StopIteration error
            if header is None:
                print(f"⚠️ {filename} is empty. No data to load.")
                return

            for row in reader:
                if len(row) == 3:
                    order_id, product_id, quantity = row
                    order_queue.orders.append(Order(order_id, product_id, int(quantity)))
        print(f"✅ Orders loaded from {filename}!")
    except FileNotFoundError:
        print(f"⚠️ {filename} not found. No data loaded.")
