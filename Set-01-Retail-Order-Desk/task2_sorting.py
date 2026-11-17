
import csv
import time
import copy

# -----------------------------------------
# 1. Load 10,000 orders from orders.csv
# -----------------------------------------

CSV_FILE = "orders.csv"
TOTAL_RECORDS = 10000


def load_orders():
    with open(CSV_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)
        orders = list(reader)

    # Select the first 10,000 records
    orders = orders[:TOTAL_RECORDS]

    for order in orders:
        order["amount"] = float(order["amount"])

    return orders


# -----------------------------------------
# 2. Bubble Sort - O(n^2)
# Sort amount in descending order
# -----------------------------------------

def bubble_sort(orders):
    arr = copy.deepcopy(orders)
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(n - 1):
        swapped = False

        for j in range(n - i - 1):
            comparisons += 1

            if arr[j]["amount"] < arr[j + 1]["amount"]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True

        if not swapped:
            break

    return arr, comparisons, swaps


# -----------------------------------------
# 3. Merge Sort - O(n log n)
# Sort amount in descending order
# -----------------------------------------

def merge_sort(orders):
    comparisons = 0

    def divide(arr):
        nonlocal comparisons

        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        left = divide(arr[:mid])
        right = divide(arr[mid:])

        return merge(left, right)

    def merge(left, right):
        nonlocal comparisons

        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            comparisons += 1

            if left[i]["amount"] >= right[j]["amount"]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])

        return result

    sorted_orders = divide(orders)

    return sorted_orders, comparisons


# -----------------------------------------
# 4. Built-in Python Sort
# -----------------------------------------

def builtin_sort(orders):
    return sorted(
        orders,
        key=lambda order: order["amount"],
        reverse=True
    )


# -----------------------------------------
# 5. Main Program and Benchmark
# -----------------------------------------

if __name__ == "__main__":

    orders = load_orders()

    print("Total records loaded:", len(orders))

    # Bubble Sort
    start = time.perf_counter()
    bubble_result, bubble_comparisons, bubble_swaps = bubble_sort(orders)
    bubble_time = time.perf_counter() - start

    # Merge Sort
    start = time.perf_counter()
    merge_result, merge_comparisons = merge_sort(orders)
    merge_time = time.perf_counter() - start

    # Built-in Sort
    start = time.perf_counter()
    builtin_result = builtin_sort(orders)
    builtin_time = time.perf_counter() - start

    # Verify all results
    bubble_amounts = [x["amount"] for x in bubble_result]
    merge_amounts = [x["amount"] for x in merge_result]
    builtin_amounts = [x["amount"] for x in builtin_result]

    print("\n========== SORTING VERIFICATION ==========")

    print("Bubble Sort correct:", bubble_amounts == builtin_amounts)
    print("Merge Sort correct:", merge_amounts == builtin_amounts)
    print("Built-in Sort correct:", builtin_amounts == sorted(
        [x["amount"] for x in orders], reverse=True
    ))

    print("\n========== PERFORMANCE COMPARISON ==========")

    print("\nBUBBLE SORT")
    print("Time:", round(bubble_time, 6), "seconds")
    print("Comparisons:", bubble_comparisons)
    print("Swaps:", bubble_swaps)

    print("\nMERGE SORT")
    print("Time:", round(merge_time, 6), "seconds")
    print("Comparisons:", merge_comparisons)

    print("\nBUILT-IN SORT")
    print("Time:", round(builtin_time, 6), "seconds")

    print("\n========== FIRST 10 SORTED ORDERS ==========")

    for order in builtin_result[:10]:
        print(
            order["orderId"],
            "Amount:", order["amount"]
        )

    print("\n========== COMPLEXITY ==========")
    print("Bubble Sort: O(n^2)")
    print("Merge Sort: O(n log n)")
    print("Built-in Sort: O(n log n) worst case")

    print("\nAll sorting experiments completed successfully!")
