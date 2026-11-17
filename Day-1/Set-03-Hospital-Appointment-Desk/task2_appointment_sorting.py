
"""
Day 1 - Set 3 - Task 2
Selection Sort vs Quick Sort
Sort appointments by urgency and then arrival time.

Urgency 1 = highest priority.
"""

import random
import time
from copy import deepcopy


def appointment_key(appointment):
    return (
        appointment["urgency"],
        appointment["arrival_time"]
    )


# ---------------- SELECTION SORT ----------------

def selection_sort(data):
    appointments = deepcopy(data)
    swaps = 0
    comparisons = 0

    n = len(appointments)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            comparisons += 1

            if appointment_key(appointments[j]) < appointment_key(
                appointments[min_index]
            ):
                min_index = j

        if min_index != i:
            appointments[i], appointments[min_index] = (
                appointments[min_index],
                appointments[i]
            )
            swaps += 1

    return appointments, comparisons, swaps


# ---------------- QUICK SORT ----------------

def quick_sort(data):
    appointments = deepcopy(data)
    swaps = [0]
    comparisons = [0]

    def partition(low, high):
        # Use the middle appointment as pivot.
        pivot = appointment_key(appointments[(low + high) // 2])

        i = low - 1
        j = high + 1

        while True:
            i += 1
            while True:
                comparisons[0] += 1
                if appointment_key(appointments[i]) >= pivot:
                    break
                i += 1

            j -= 1
            while True:
                comparisons[0] += 1
                if appointment_key(appointments[j]) <= pivot:
                    break
                j -= 1

            if i >= j:
                return j

            appointments[i], appointments[j] = (
                appointments[j],
                appointments[i]
            )
            swaps[0] += 1

    def sort(low, high):
        if low < high:
            split = partition(low, high)
            sort(low, split)
            sort(split + 1, high)

    sort(0, len(appointments) - 1)

    return appointments, comparisons[0], swaps[0]


# ---------------- MAIN PROGRAM ----------------

def main():
    print("=" * 75)
    print("HOSPITAL APPOINTMENT DESK - APPOINTMENT SORTING")
    print("=" * 75)

    random.seed(42)

    # Generate 1,000 sample appointments.
    appointments = []

    for i in range(1, 1001):
        hour = random.randint(8, 17)
        minute = random.choice([0, 15, 30, 45])

        appointments.append({
            "patient_id": f"PAT{i:05d}",
            "urgency": random.randint(1, 5),
            "arrival_time": f"{hour:02d}:{minute:02d}"
        })

    print(f"\nTotal appointments: {len(appointments)}")

    print("\n--- ORIGINAL APPOINTMENTS (FIRST 10) ---")
    for appointment in appointments[:10]:
        print(appointment)

    # Selection Sort
    start = time.perf_counter()
    selection_result, selection_comparisons, selection_swaps = (
        selection_sort(appointments)
    )
    selection_time = time.perf_counter() - start

    # Quick Sort
    start = time.perf_counter()
    quick_result, quick_comparisons, quick_swaps = (
        quick_sort(appointments)
    )
    quick_time = time.perf_counter() - start

    print("\n--- SELECTION SORT RESULT (FIRST 10) ---")
    for appointment in selection_result[:10]:
        print(appointment)

    print("\n--- QUICK SORT RESULT (FIRST 10) ---")
    for appointment in quick_result[:10]:
        print(appointment)

    print("\n--- PERFORMANCE COMPARISON ---")
    print(f"Selection Sort comparisons: {selection_comparisons}")
    print(f"Selection Sort swaps:       {selection_swaps}")
    print(f"Selection Sort time:        {selection_time:.8f} seconds")

    print(f"\nQuick Sort comparisons:     {quick_comparisons}")
    print(f"Quick Sort swaps:           {quick_swaps}")
    print(f"Quick Sort time:            {quick_time:.8f} seconds")

    # Verify both algorithms use the same ordering.
    selection_keys = [appointment_key(a) for a in selection_result]
    quick_keys = [appointment_key(a) for a in quick_result]

    print("\n--- CORRECTNESS CHECK ---")
    print("Selection Sort correctly ordered:",
          selection_keys == sorted(selection_keys))
    print("Quick Sort correctly ordered:",
          quick_keys == sorted(quick_keys))
    print("Both algorithms produce the same order:",
          selection_keys == quick_keys)

    print("\nTask 2 completed successfully.")


if __name__ == "__main__":
    main()
