
"""
Day 1 - Set 2 - Task 5
Find Highest and Lowest Transaction Amounts
Using Divide and Conquer and Brute Force
"""

import random
import time


# ---------------- BRUTE FORCE ----------------

def brute_force_min_max(amounts):
    if not amounts:
        return None, None, 0

    minimum = amounts[0]
    maximum = amounts[0]
    comparisons = 0

    for amount in amounts[1:]:
        comparisons += 1
        if amount < minimum:
            minimum = amount

        comparisons += 1
        if amount > maximum:
            maximum = amount

    return minimum, maximum, comparisons


# ---------------- DIVIDE AND CONQUER ----------------

def divide_conquer_min_max(amounts, low, high):
    if low == high:
        return amounts[low], amounts[low], 0

    if high == low + 1:
        comparisons = 1

        if amounts[low] < amounts[high]:
            return amounts[low], amounts[high], comparisons
        else:
            return amounts[high], amounts[low], comparisons

    mid = (low + high) // 2

    left_min, left_max, left_count = divide_conquer_min_max(
        amounts, low, mid
    )

    right_min, right_max, right_count = divide_conquer_min_max(
        amounts, mid + 1, high
    )

    comparisons = left_count + right_count

    comparisons += 1
    minimum = min(left_min, right_min)

    comparisons += 1
    maximum = max(left_max, right_max)

    return minimum, maximum, comparisons


# ---------------- MAIN PROGRAM ----------------

def main():
    print("=" * 70)
    print("RETAIL BANKING - MINIMUM AND MAXIMUM TRANSACTION AMOUNTS")
    print("=" * 70)

    # Generate sample transaction amounts
    random.seed(42)
    amounts = [
        random.randint(100, 100000) for _ in range(10000)
    ]

    print(f"\nTotal transactions: {len(amounts)}")
    print(f"Sample amounts: {amounts[:10]}")

    # Brute force
    start = time.perf_counter()
    brute_min, brute_max, brute_comparisons = brute_force_min_max(
        amounts
    )
    brute_time = time.perf_counter() - start

    # Divide and conquer
    start = time.perf_counter()
    dc_min, dc_max, dc_comparisons = divide_conquer_min_max(
        amounts, 0, len(amounts) - 1
    )
    dc_time = time.perf_counter() - start

    print("\n--- BRUTE FORCE RESULT ---")
    print(f"Lowest transaction amount:  {brute_min}")
    print(f"Highest transaction amount: {brute_max}")
    print(f"Comparisons: {brute_comparisons}")
    print(f"Execution time: {brute_time:.8f} seconds")

    print("\n--- DIVIDE AND CONQUER RESULT ---")
    print(f"Lowest transaction amount:  {dc_min}")
    print(f"Highest transaction amount: {dc_max}")
    print(f"Comparisons: {dc_comparisons}")
    print(f"Execution time: {dc_time:.8f} seconds")

    print("\n--- COMPARISON ---")
    print("Brute Force Time Complexity: O(n)")
    print("Divide and Conquer Time Complexity: O(n)")
    print("Both methods use constant auxiliary space for brute force,")
    print("while divide and conquer uses O(log n) recursion stack space.")

    print("\n--- CORRECTNESS CHECK ---")
    print("Minimum values match:", brute_min == dc_min)
    print("Maximum values match:", brute_max == dc_max)

    print("\nTask 5 completed successfully.")


if __name__ == "__main__":
    main()
