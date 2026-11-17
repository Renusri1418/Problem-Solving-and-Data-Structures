
# Task 3 – Duplicate Order Detection

## Objective
Identify duplicate retail orders using a hash-based
data structure.

## Duplicate Conditions

Two or more orders are considered duplicates when:
1. Customer ID is identical.
2. Order amount is identical.
3. Orders were created within the same minute.

## Data Structure Used

Python Dictionary (HashMap).

The dictionary uses a composite key consisting of:
- customerId
- amount
- Created date and time rounded down to the minute.

## Algorithm

1. Read all orders from orders.csv.
2. Extract customer ID and order amount.
3. Convert the creation timestamp into a datetime object.
4. Remove seconds and microseconds to obtain the minute.
5. Construct a composite dictionary key.
6. Store orders sharing the same key.
7. Identify dictionary entries containing more than one order.

## Test Case

| Order ID | Customer | Amount | Time |
|---|---|---:|---|
| TEST001 | CUST99999 | 1500 | 10:30:10 |
| TEST002 | CUST99999 | 1500 | 10:30:45 |
| TEST003 | CUST99999 | 1500 | 10:30:55 |

Expected result: One duplicate group containing
three orders.

## Complexity Analysis

Average Time Complexity: O(n)

Each order is processed once, with average
constant-time dictionary insertion and lookup.

Space Complexity: O(n)

The dictionary stores information about the orders.

Worst-case time complexity can reach O(n^2)
if severe hash collisions occur.

## Conclusion

A HashMap is suitable for detecting duplicate orders
because it provides efficient average-time insertion
and lookup.

It avoids repeatedly scanning the entire list for
every order.
