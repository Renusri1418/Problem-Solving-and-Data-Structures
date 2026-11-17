
"""
Day 1 - Set 3 - Task 1
Linear Search vs Binary Search
20,000 patient records and 1,000 lookups
"""

import random
import time


def linear_search(patient_ids, target):
    for index, patient_id in enumerate(patient_ids):
        if patient_id == target:
            return index
    return -1


def binary_search(patient_ids, target):
    low = 0
    high = len(patient_ids) - 1

    while low <= high:
        mid = (low + high) // 2

        if patient_ids[mid] == target:
            return mid
        elif target < patient_ids[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


def main():
    print("=" * 65)
    print("HOSPITAL APPOINTMENT DESK - PATIENT ID SEARCH")
    print("=" * 65)

    # Generate 20,000 sorted patient IDs
    patient_ids = [
        f"PAT{i:05d}" for i in range(1, 20001)
    ]

    # Generate 1,000 reproducible existing patient IDs
    random.seed(42)
    lookup_ids = random.choices(patient_ids, k=1000)

    print(f"\nTotal patient records: {len(patient_ids):,}")
    print(f"Total lookups: {len(lookup_ids):,}")
    print(f"First patient ID: {patient_ids[0]}")
    print(f"Last patient ID: {patient_ids[-1]}")

    # Measure linear search
    start = time.perf_counter()

    linear_results = [
        linear_search(patient_ids, target)
        for target in lookup_ids
    ]

    linear_time = time.perf_counter() - start

    # Measure binary search
    start = time.perf_counter()

    binary_results = [
        binary_search(patient_ids, target)
        for target in lookup_ids
    ]

    binary_time = time.perf_counter() - start

    print("\n--- LINEAR SEARCH ---")
    print(f"Total lookup time: {linear_time:.8f} seconds")
    print(f"Average per lookup: {linear_time / 1000:.8f} seconds")

    print("\n--- BINARY SEARCH ---")
    print(f"Total lookup time: {binary_time:.8f} seconds")
    print(f"Average per lookup: {binary_time / 1000:.8f} seconds")

    print("\n--- PERFORMANCE COMPARISON ---")

    if binary_time > 0:
        print(f"Linear/Binary time ratio: {linear_time / binary_time:.2f}x")

    print("Linear Search Complexity: O(n)")
    print("Binary Search Complexity: O(log n)")

    print("\n--- CORRECTNESS CHECK ---")
    print("All linear searches successful:",
          all(index != -1 for index in linear_results))
    print("All binary searches successful:",
          all(index != -1 for index in binary_results))
    print("Both methods return identical positions:",
          linear_results == binary_results)

    print("\nTask 1 completed successfully.")


if __name__ == "__main__":
    main()
