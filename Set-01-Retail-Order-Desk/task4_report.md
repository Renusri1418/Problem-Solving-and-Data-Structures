
# Task 4 – Stack and Queue Implementation

## Objective
Implement a custom Stack and Queue to support order
editing and warehouse dispatch operations. Compare
them with Python's built-in equivalents.

## 1. Stack – Undo Last Order Edit

A Stack follows LIFO (Last In, First Out).

Operations:
- Push: Add an edit to the history.
- Pop: Remove and retrieve the latest edit.
- Peek: View the latest edit.
- Is Empty: Check whether the stack is empty.

Application:
The previous order state is stored before each edit.
When undo is performed, the previous state is restored.

Time Complexity:
- Push: O(1) amortized
- Pop: O(1) amortized
- Peek: O(1)

Space Complexity: O(n)

## 2. Queue – Warehouse Dispatch

A Queue follows FIFO (First In, First Out).

Operations:
- Enqueue: Add an order to the dispatch line.
- Dequeue: Remove the first order.
- Peek: View the next order.
- Is Empty: Check whether the queue is empty.

Application:
Orders are dispatched in the same order in which
they enter the warehouse dispatch line.

Time Complexity:
- Enqueue: O(1) amortized
- Dequeue: O(1) amortized in our implementation
- Peek: O(1)

Space Complexity: O(n)

## 3. Built-in Equivalents

Stack:
Python List using append() and pop().

Queue:
Python collections.deque using append() and popleft().

## 4. Comparison

| Feature | Custom | Built-in |
|---|---|---|
| Stack | CustomStack | Python List |
| Queue | CustomQueue | Deque |
| Stack insertion | O(1) amortized | O(1) amortized |
| Stack removal | O(1) amortized | O(1) amortized |
| Queue insertion | O(1) amortized | O(1) |
| Queue removal | O(1) amortized | O(1) |

## Conclusion

The Stack supports undo functionality by restoring
the most recent previous order state.

The Queue ensures that warehouse orders are dispatched
in first-in-first-out order.

Python's built-in data structures provide convenient
and efficient implementations. Custom implementations
help demonstrate the underlying data structure logic.
