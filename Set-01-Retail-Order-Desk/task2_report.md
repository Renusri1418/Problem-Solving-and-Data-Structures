
# Task 2 – Sorting Algorithms

## Objective
Implement and compare Bubble Sort, Merge Sort and
Python's built-in sorting function to rank retail orders
by amount in descending order.

## Dataset
- Total records: 10,000
- Sorting field: amount
- Sorting order: Descending

## Algorithms Implemented

### 1. Bubble Sort
Bubble Sort repeatedly compares adjacent elements
and swaps them when they are in the wrong order.

Time Complexity:
- Best: O(n) with early termination
- Average: O(n^2)
- Worst: O(n^2)

Space Complexity: O(n) in our implementation
because a copy of the input is created.
The sorting algorithm itself uses O(1) extra space.

### 2. Merge Sort
Merge Sort divides the dataset into smaller parts,
sorts them and merges the sorted parts.

Time Complexity:
- Best: O(n log n)
- Average: O(n log n)
- Worst: O(n log n)

Auxiliary Space Complexity: O(n)

### 3. Python Built-in Sort
Python's sorted() function uses Timsort to sort data.

Time Complexity:
- Best: O(n)
- Average: O(n log n)
- Worst: O(n log n)

Space Complexity: O(n)

## Benchmark Results

| Metric | Bubble Sort | Merge Sort | Built-in Sort |
|---|---:|---:|---:|
| Execution time | 12.712480 s | 0.032414 s | 0.001897 s |
| Comparisons | 49982280 | 120480 | Not measured |
| Swaps | 25193596 | N/A | N/A |

## Bubble Sort – First Three Passes

Original:
120, 450, 200, 800, 350

Pass 1:
450, 200, 800, 350, 120

Pass 2:
450, 800, 350, 200, 120

Pass 3:
800, 450, 350, 200, 120

## Observations

Bubble Sort required significantly more comparisons
and execution time than Merge Sort.

Merge Sort improved performance through its
divide-and-conquer approach.

Python's built-in sorting function was the fastest
in this experiment.

All three algorithms produced correctly sorted results.

## Conclusion

For large retail datasets, Merge Sort and Python's
built-in sorting function are more suitable than
Bubble Sort.

The built-in sorting function provided the best
execution time in this experiment.
