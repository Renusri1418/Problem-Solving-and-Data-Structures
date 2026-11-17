
"""
Day 1 - Set 2 - Task 4
Queue for Manual Review Backlog
Stack for Reversing Last Adjustment

Both structures are implemented from scratch without
using library collections.
"""


# ---------------- CUSTOM QUEUE ----------------

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

        # Reset storage when all items have been removed.
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

    def display(self):
        return self.items[self.front:]


# ---------------- CUSTOM STACK ----------------

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

    def display(self):
        return self.items.copy()


# ---------------- MAIN PROGRAM ----------------

def main():
    print("=" * 65)
    print("RETAIL BANKING - QUEUE AND STACK")
    print("=" * 65)

    # Queue: manual review backlog
    print("\n--- MANUAL REVIEW QUEUE ---")

    review_queue = CustomQueue()

    review_queue.enqueue("Review TXN101")
    review_queue.enqueue("Review TXN102")
    review_queue.enqueue("Review TXN103")

    print("Review backlog:", review_queue.display())
    print("Next transaction:", review_queue.peek())

    print("Processing:", review_queue.dequeue())
    print("Processing:", review_queue.dequeue())

    print("Remaining backlog:", review_queue.display())

    # Stack: reverse last adjustment
    print("\n--- ADJUSTMENT REVERSAL STACK ---")

    adjustment_stack = CustomStack()

    adjustment_stack.push("Credit +500")
    adjustment_stack.push("Debit -200")
    adjustment_stack.push("Credit +1000")

    print("Adjustment history:", adjustment_stack.display())
    print("Last adjustment:", adjustment_stack.peek())

    reversed_adjustment = adjustment_stack.pop()
    print("Reversing last adjustment:", reversed_adjustment)

    print("Remaining adjustment history:", adjustment_stack.display())

    # Empty structure tests
    print("\n--- EMPTY STRUCTURE TESTS ---")
    empty_queue = CustomQueue()
    empty_stack = CustomStack()

    print("Dequeue from empty queue:", empty_queue.dequeue())
    print("Pop from empty stack:", empty_stack.pop())

    print("\nTask 4 completed successfully.")


if __name__ == "__main__":
    main()
