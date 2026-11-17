
import csv
import random
import time
from datetime import datetime, timedelta

# --------------------------------
# 1. Generate 50,000 sample orders
# --------------------------------

TOTAL_ORDERS = 50000
CSV_FILE = "orders.csv"

random.seed(42)

def generate_orders():
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["orderId", "customerId", "amount", "createdAt"]
        )

        writer.writeheader()

        start_date = datetime(2026, 1, 1)

        for i in range(1, TOTAL_ORDERS + 1):
            order = {
                "orderId": f"ORD{i:06d}",
                "customerId": f"CUST{random.randint(1, 10000):05d}",
                "amount": round(random.uniform(100, 10000), 2),
                "createdAt": (
                    start_date + timedelta(minutes=random.randint(0, 50000))
                ).isoformat()
            }

            writer.writerow(order)

    print("50,000 orders generated successfully!")


# --------------------------------
# 2. Load orders from CSV
# --------------------------------

def load_orders():
    with open(CSV_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


# --------------------------------
# 3. Linear Search - O(n)
# --------------------------------

def linear_search(orders, target):
    comparisons = 0

    for order in orders:
        comparisons += 1

        if order["orderId"] == target:
            return order, comparisons

    return None, comparisons


# --------------------------------
# 4. Binary Search - O(log n)
# --------------------------------

def binary_search(orders, target):
    low = 0
    high = len(orders) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if orders[mid]["orderId"] == target:
            return orders[mid], comparisons

        elif orders[mid]["orderId"] < target:
            low = mid + 1

        else:
            high = mid - 1

    return None, comparisons


# --------------------------------
# 5. Benchmark both algorithms
# --------------------------------

def benchmark(orders):
    targets = random.sample(
        [order["orderId"] for order in orders], 200
    )

    linear_comparisons = 0
    binary_comparisons = 0

    start = time.perf_counter()

    for target in targets:
        result, count = linear_search(orders, target)
        linear_comparisons += count

    linear_time = time.perf_counter() - start

    start = time.perf_counter()

    for target in targets:
        result, count = binary_search(orders, target)
        binary_comparisons += count

    binary_time = time.perf_counter() - start

    print("\n========== SEARCH BENCHMARK ==========")
    print("Total orders:", len(orders))
    print("Number of searches:", len(targets))

    print("\nLINEAR SEARCH")
    print("Total comparisons:", linear_comparisons)
    print("Average comparisons:", round(linear_comparisons / len(targets), 2))
    print("Execution time:", round(linear_time, 6), "seconds")

    print("\nBINARY SEARCH")
    print("Total comparisons:", binary_comparisons)
    print("Average comparisons:", round(binary_comparisons / len(targets), 2))
    print("Execution time:", round(binary_time, 6), "seconds")

    print("\n========== CONCLUSION ==========")

    if binary_time > 0:
        print("Binary search speed advantage:",
              round(linear_time / binary_time, 2), "times")

    print("Linear Search Complexity: O(n)")
    print("Binary Search Complexity: O(log n)")


# --------------------------------
# 6. Main program
# --------------------------------

if __name__ == "__main__":

    generate_orders()

    orders = load_orders()

    # Binary search requires sorted data
    orders.sort(key=lambda x: x["orderId"])

    print("\nDataset loaded successfully!")
    print("First order:", orders[0])
    print("Last order:", orders[-1])

    # Demonstrate an individual search
    target = "ORD025000"

    print("\nSearching for:", target)

    result, count = linear_search(orders, target)
    print("Linear Search Result:", result)
    print("Linear Search Comparisons:", count)

    result, count = binary_search(orders, target)
    print("Binary Search Result:", result)
    print("Binary Search Comparisons:", count)

    benchmark(orders)
