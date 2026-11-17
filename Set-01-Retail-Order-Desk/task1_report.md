
# Task 1 – Linear Search vs Binary Search

## Objective
To implement and compare Linear Search and Binary Search
using a dataset containing 50,000 retail orders.

## Dataset
- Total records: 50,000
- Fields: orderId, customerId, amount, createdAt
- File: orders.csv

## Algorithms Implemented

### 1. Linear Search
Linear Search checks each record sequentially until
the required order ID is found.

Time Complexity:
- Best: O(1)
- Average: O(n)
- Worst: O(n)

Space Complexity: O(1)

### 2. Binary Search
Binary Search repeatedly divides the sorted dataset
into two halves until the target is located.

Time Complexity:
- Best: O(1)
- Average: O(log n)
- Worst: O(log n)

Space Complexity: O(1)

## Benchmark Results

Number of records: 50,000
Number of searches: 200

| Metric | Linear | Binary |
|---|---:|---:|
| Total comparisons | 5359623 | 2935 |
| Average comparisons | 26798.12 | 14.68 |
| Execution time | 0.935625 sec | 0.003025 sec |

Observed speed advantage: 309.3 times.

## Observation

Linear Search examines records sequentially.
Its performance decreases as the dataset grows.

Binary Search eliminates half of the remaining
search space during every iteration. Therefore,
it requires significantly fewer comparisons.

Binary Search performed much faster in this experiment.

## Conclusion

Binary Search is more suitable for retrieving orders
from a large sorted dataset.

However, Binary Search requires sorted data,
whereas Linear Search works on unsorted data.
