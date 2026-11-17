
import csv
from collections import defaultdict
from datetime import datetime

CSV_FILE = "orders.csv"


# -----------------------------------------
# 1. Load orders from CSV
# -----------------------------------------

def load_orders():
    with open(CSV_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


# -----------------------------------------
# 2. Detect duplicate orders using HashMap
# -----------------------------------------

def detect_duplicates(orders):

    order_map = defaultdict(list)

    for order in orders:

        customer_id = order["customerId"]
        amount = round(float(order["amount"]), 2)

        # Convert timestamp to datetime
        created_at = datetime.fromisoformat(order["createdAt"])

        # Extract date and hour and minute
        minute = created_at.replace(
            second=0,
            microsecond=0
        )

        # Create a hash key
        key = (customer_id, amount, minute)

        # Store order in the dictionary
        order_map[key].append(order)

    # Collect groups containing duplicates
    duplicates = {
        key: records
        for key, records in order_map.items()
        if len(records) > 1
    }

    return duplicates


# -----------------------------------------
# 3. Create deliberate duplicate test data
# -----------------------------------------

def create_test_data(orders):

    test_orders = orders.copy()

    sample_order = {
        "orderId": "TEST001",
        "customerId": "CUST99999",
        "amount": "1500.00",
        "createdAt": "2026-11-17T10:30:10"
    }

    duplicate_order = {
        "orderId": "TEST002",
        "customerId": "CUST99999",
        "amount": "1500.00",
        "createdAt": "2026-11-17T10:30:45"
    }

    third_duplicate = {
        "orderId": "TEST003",
        "customerId": "CUST99999",
        "amount": "1500.00",
        "createdAt": "2026-11-17T10:30:55"
    }

    test_orders.extend([
        sample_order,
        duplicate_order,
        third_duplicate
    ])

    return test_orders


# -----------------------------------------
# 4. Main Program
# -----------------------------------------

if __name__ == "__main__":

    orders = load_orders()

    print("Total original orders:", len(orders))

    # Detect duplicates in original dataset
    original_duplicates = detect_duplicates(orders)

    print("\n========== ORIGINAL DATASET ==========")
    print("Duplicate groups found:", len(original_duplicates))

    # Create controlled test data
    test_orders = create_test_data(orders)

    # Detect duplicates in test dataset
    duplicates = detect_duplicates(test_orders)

    print("\n========== TEST DATASET ==========")
    print("Total test orders:", len(test_orders))
    print("Duplicate groups found:", len(duplicates))

    for key, records in duplicates.items():

        print("\nDuplicate Group:")
        print("Customer ID:", key[0])
        print("Amount:", key[1])
        print("Minute:", key[2])

        for order in records:
            print(
                "Order ID:", order["orderId"],
                "| Created At:", order["createdAt"]
            )

    print("\n========== COMPLEXITY ==========")
    print("Average Time Complexity: O(n)")
    print("Space Complexity: O(n)")

    print("\nDuplicate detection completed successfully!")
