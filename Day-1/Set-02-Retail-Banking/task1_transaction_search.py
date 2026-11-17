
"""
Day 1 - Set 2 - Task 1
Binary Search vs Linear Search
Dataset: 100,000 sorted transaction IDs
"""

def linear_search(transaction_ids, target):
    comparisons = 0

    for index, transaction_id in enumerate(transaction_ids):
        comparisons += 1

        if transaction_id == target:
            return index, comparisons

    return -1, comparisons


def binary_search(transaction_ids, target):
    low = 0
    high = len(transaction_ids) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2

        # First comparison: equality
        comparisons += 1
        if transaction_ids[mid] == target:
            return mid, comparisons

        # Second comparison: ordering
        comparisons += 1
        if target < transaction_ids[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1, comparisons


def main():
    # Generate 100,000 sorted transaction IDs
    transaction_ids = [
        f"TXN{i:06d}" for i in range(1, 100001)
    ]

    n = len(transaction_ids)

    print("=" * 65)
    print("RETAIL BANKING - TRANSACTION ID SEARCH")
    print("=" * 65)
    print(f"Total transaction IDs: {n:,}")
    print(f"First ID: {transaction_ids[0]}")
    print(f"Last ID:  {transaction_ids[-1]}")

    # Best case: middle element is found immediately
    best_target = transaction_ids[n // 2]

    # Measure binary search for every existing ID
    binary_counts = []

    for target in transaction_ids:
        _, count = binary_search(transaction_ids, target)
        binary_counts.append(count)

    average_binary = sum(binary_counts) / n
    worst_binary = max(binary_counts)

    worst_index = binary_counts.index(worst_binary)
    worst_target = transaction_ids[worst_index]

    # Linear search comparison counts for successful searches
    linear_best = 1
    linear_average = (n + 1) / 2
    linear_worst = n

    # Display binary search results
    _, best_binary = binary_search(transaction_ids, best_target)

    print("\n--- BINARY SEARCH ---")
    print(f"Best case comparisons:    {best_binary}")
    print(f"Average comparisons:      {average_binary:.2f}")
    print(f"Worst case comparisons:   {worst_binary}")
    print(f"Worst case target:        {worst_target}")

    # Display linear search results
    print("\n--- LINEAR SEARCH ---")
    print(f"Best case comparisons:    {linear_best}")
    print(f"Average comparisons:      {linear_average:.2f}")
    print(f"Worst case comparisons:   {linear_worst}")

    print("\n--- COMPLEXITY COMPARISON ---")
    print("Linear Search: O(n)")
    print("Binary Search: O(log n)")
    print("Binary Search requires sorted data.")

    print("\n--- VERIFICATION ---")
    test_id = "TXN075000"

    linear_result = linear_search(transaction_ids, test_id)
    binary_result = binary_search(transaction_ids, test_id)

    print(f"Test transaction: {test_id}")
    print(f"Linear Search: index={linear_result[0]}, "
          f"comparisons={linear_result[1]}")
    print(f"Binary Search: index={binary_result[0]}, "
          f"comparisons={binary_result[1]}")

    print("\nTask 1 completed successfully.")


if __name__ == "__main__":
    main()
