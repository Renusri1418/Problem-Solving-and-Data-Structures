
"""
Day 1 - Set 2 - Task 2
Insertion Sort vs Merge Sort
Sort a customer's bank statement by posting date.
Demonstrate sorting stability.
"""

from datetime import datetime
from copy import deepcopy
import time


transactions = [
    {"transaction_id": "TXN105", "posting_date": "2026-11-15 10:30:00",
     "description": "Grocery payment", "amount": -850},

    {"transaction_id": "TXN102", "posting_date": "2026-11-14 09:15:00",
     "description": "Salary credit", "amount": 25000},

    {"transaction_id": "TXN103", "posting_date": "2026-11-15 10:30:00",
     "description": "Electricity bill", "amount": -1200},

    {"transaction_id": "TXN101", "posting_date": "2026-11-13 14:45:00",
     "description": "ATM withdrawal", "amount": -2000},

    {"transaction_id": "TXN104", "posting_date": "2026-11-14 16:20:00",
     "description": "Online shopping", "amount": -1500},

    {"transaction_id": "TXN106", "posting_date": "2026-11-15 10:30:00",
     "description": "Fuel payment", "amount": -1000},
]


def date_key(transaction):
    return datetime.strptime(
        transaction["posting_date"], "%Y-%m-%d %H:%M:%S"
    )


def insertion_sort(data):
    result = deepcopy(data)
    comparisons = 0
    shifts = 0

    for i in range(1, len(result)):
        current = result[i]
        j = i - 1

        while j >= 0:
            comparisons += 1

            # Strictly greater: equal timestamps keep their original order.
            if date_key(result[j]) > date_key(current):
                result[j + 1] = result[j]
                shifts += 1
                j -= 1
            else:
                break

        result[j + 1] = current

    return result, comparisons, shifts


def merge_sort(data):
    comparisons = [0]
    result = deepcopy(data)

    def divide(items):
        if len(items) <= 1:
            return items

        middle = len(items) // 2
        left = divide(items[:middle])
        right = divide(items[middle:])

        return merge(left, right)

    def merge(left, right):
        merged = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            comparisons[0] += 1

            # <= ensures the left item wins ties: stable merge.
            if date_key(left[i]) <= date_key(right[j]):
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    sorted_data = divide(result)
    return sorted_data, comparisons[0]


def display_transactions(title, data):
    print(f"\n{title}")
    print("-" * 75)

    for transaction in data:
        print(
            f"{transaction['transaction_id']} | "
            f"{transaction['posting_date']} | "
            f"{transaction['description']} | "
            f"Amount: {transaction['amount']}"
        )


def main():
    print("=" * 75)
    print("RETAIL BANKING - CUSTOMER STATEMENT SORTING")
    print("=" * 75)

    display_transactions("ORIGINAL STATEMENT", transactions)

    # Insertion Sort
    start = time.perf_counter()
    insertion_result, insertion_comparisons, shifts = insertion_sort(
        transactions
    )
    insertion_time = time.perf_counter() - start

    # Merge Sort
    start = time.perf_counter()
    merge_result, merge_comparisons = merge_sort(transactions)
    merge_time = time.perf_counter() - start

    display_transactions("INSERTION SORT RESULT", insertion_result)
    display_transactions("MERGE SORT RESULT", merge_result)

    print("\n--- PERFORMANCE COMPARISON ---")
    print(f"Insertion Sort comparisons: {insertion_comparisons}")
    print(f"Insertion Sort shifts:      {shifts}")
    print(f"Insertion Sort time:        {insertion_time:.8f} seconds")

    print(f"\nMerge Sort comparisons:     {merge_comparisons}")
    print(f"Merge Sort time:            {merge_time:.8f} seconds")

    # Verify both algorithms give the same chronological order.
    insertion_dates = [date_key(t) for t in insertion_result]
    merge_dates = [date_key(t) for t in merge_result]

    print("\n--- STABILITY CHECK ---")
    same_timestamp_ids = [
        t["transaction_id"]
        for t in insertion_result
        if t["posting_date"] == "2026-11-15 10:30:00"
    ]

    print("Original order at 10:30:")
    print("TXN105, TXN103, TXN106")
    print("Insertion Sort order at 10:30:", same_timestamp_ids)

    merge_same_timestamp_ids = [
        t["transaction_id"]
        for t in merge_result
        if t["posting_date"] == "2026-11-15 10:30:00"
    ]

    print("Merge Sort order at 10:30:", merge_same_timestamp_ids)

    print("\n--- CORRECTNESS ---")
    print("Both algorithms produce the same dates:",
          insertion_dates == merge_dates)
    print("Insertion Sort is stable:",
          same_timestamp_ids == ["TXN105", "TXN103", "TXN106"])
    print("Merge Sort is stable:",
          merge_same_timestamp_ids == ["TXN105", "TXN103", "TXN106"])

    print("\nTask 2 completed successfully.")


if __name__ == "__main__":
    main()
