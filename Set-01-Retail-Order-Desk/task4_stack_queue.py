
import time
from collections import deque


# ==========================================
# 1. CUSTOM STACK IMPLEMENTATION
# ==========================================

class CustomStack:

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0


# ==========================================
# 2. CUSTOM QUEUE IMPLEMENTATION
# ==========================================

class CustomQueue:

    def __init__(self):
        self.items = []
        self.front = 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None

        item = self.items[self.front]
        self.front += 1

        # Clear processed elements when queue is empty
        if self.front == len(self.items):
            self.items = []
            self.front = 0

        return item

    def peek(self):
        if self.is_empty():
            return None
        return self.items[self.front]

    def is_empty(self):
        return self.front >= len(self.items)


# ==========================================
# 3. UNDO LAST ORDER EDIT USING CUSTOM STACK
# ==========================================

def custom_stack_demo():

    print("\n========== CUSTOM STACK: UNDO ORDER EDIT ==========")

    order = {
        "orderId": "ORD001",
        "amount": 500
    }

    history = CustomStack()

    print("Original Order:", order)

    # First edit
    history.push(order.copy())
    order["amount"] = 700
    print("After first edit:", order)

    # Second edit
    history.push(order.copy())
    order["amount"] = 900
    print("After second edit:", order)

    # Undo last edit
    previous = history.pop()

    if previous is not None:
        order = previous

    print("After first undo:", order)

    # Undo again
    previous = history.pop()

    if previous is not None:
        order = previous

    print("After second undo:", order)


# ==========================================
# 4. DISPATCH LINE USING CUSTOM QUEUE
# ==========================================

def custom_queue_demo():

    print("\n========== CUSTOM QUEUE: DISPATCH LINE ==========")

    dispatch = CustomQueue()

    dispatch.enqueue("ORD001")
    dispatch.enqueue("ORD002")
    dispatch.enqueue("ORD003")

    print("First order waiting:", dispatch.peek())

    while not dispatch.is_empty():
        print("Dispatched:", dispatch.dequeue())


# ==========================================
# 5. BUILT-IN STACK USING PYTHON LIST
# ==========================================

def builtin_stack_demo():

    print("\n========== BUILT-IN STACK ==========")

    stack = []

    stack.append("Edit 1: Amount = 500")
    stack.append("Edit 2: Amount = 700")
    stack.append("Edit 3: Amount = 900")

    print("Latest edit:", stack[-1])

    print("Undo:", stack.pop())
    print("Undo:", stack.pop())

    print("Remaining history:", stack)


# ==========================================
# 6. BUILT-IN QUEUE USING DEQUE
# ==========================================

def builtin_queue_demo():

    print("\n========== BUILT-IN QUEUE ==========")

    dispatch = deque()

    dispatch.append("ORD001")
    dispatch.append("ORD002")
    dispatch.append("ORD003")

    print("First order waiting:", dispatch[0])

    while dispatch:
        print("Dispatched:", dispatch.popleft())


# ==========================================
# 7. PERFORMANCE COMPARISON
# ==========================================

def performance_comparison():

    print("\n========== PERFORMANCE COMPARISON ==========")

    n = 100000

    # Custom stack
    stack = CustomStack()

    start = time.perf_counter()

    for i in range(n):
        stack.push(i)

    for i in range(n):
        stack.pop()

    custom_stack_time = time.perf_counter() - start

    # Built-in stack
    stack = []

    start = time.perf_counter()

    for i in range(n):
        stack.append(i)

    for i in range(n):
        stack.pop()

    builtin_stack_time = time.perf_counter() - start

    # Custom queue
    queue = CustomQueue()

    start = time.perf_counter()

    for i in range(n):
        queue.enqueue(i)

    for i in range(n):
        queue.dequeue()

    custom_queue_time = time.perf_counter() - start

    # Built-in queue
    queue = deque()

    start = time.perf_counter()

    for i in range(n):
        queue.append(i)

    for i in range(n):
        queue.popleft()

    builtin_queue_time = time.perf_counter() - start

    print("Operations per implementation:", n, "insertions +", n, "removals")

    print("\nSTACK")
    print("Custom Stack:", round(custom_stack_time, 6), "seconds")
    print("Built-in Stack:", round(builtin_stack_time, 6), "seconds")

    print("\nQUEUE")
    print("Custom Queue:", round(custom_queue_time, 6), "seconds")
    print("Built-in Queue:", round(builtin_queue_time, 6), "seconds")


# ==========================================
# 8. MAIN PROGRAM
# ==========================================

if __name__ == "__main__":

    custom_stack_demo()

    custom_queue_demo()

    builtin_stack_demo()

    builtin_queue_demo()

    performance_comparison()

    print("\nAll Stack and Queue operations completed!")
