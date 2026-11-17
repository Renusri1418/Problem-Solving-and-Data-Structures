
"""
Day 1 - Set 3 - Task 4
Custom Queue for Walk-in Patients
Custom Stack for Recently Viewed Patients

Both are implemented from scratch.
"""


# ---------------- CUSTOM QUEUE ----------------

class PatientQueue:
    def __init__(self):
        self.items = []
        self.front = 0

    def enqueue(self, patient):
        self.items.append(patient)

    def dequeue(self):
        if self.is_empty():
            return None

        patient = self.items[self.front]
        self.front += 1

        if self.front == len(self.items):
            self.items = []
            self.front = 0

        return patient

    def peek(self):
        if self.is_empty():
            return None
        return self.items[self.front]

    def is_empty(self):
        return self.front >= len(self.items)

    def display(self):
        return self.items[self.front:]


# ---------------- CUSTOM STACK ----------------

class PatientStack:
    def __init__(self):
        self.items = []

    def push(self, patient):
        self.items.append(patient)

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
    print("=" * 70)
    print("HOSPITAL APPOINTMENT DESK - QUEUE AND STACK")
    print("=" * 70)

    # Queue: walk-in patient token line
    print("\n--- WALK-IN PATIENT QUEUE ---")

    walk_in_queue = PatientQueue()

    walk_in_queue.enqueue("PAT001 - Ramesh")
    walk_in_queue.enqueue("PAT002 - Priya")
    walk_in_queue.enqueue("PAT003 - Kumar")

    print("Current queue:", walk_in_queue.display())
    print("Next patient:", walk_in_queue.peek())

    print("\nCalling patients:")
    print("Called:", walk_in_queue.dequeue())
    print("Called:", walk_in_queue.dequeue())

    print("Remaining queue:", walk_in_queue.display())

    # Stack: recently viewed patient history
    print("\n--- RECENTLY VIEWED PATIENTS STACK ---")

    viewed_stack = PatientStack()

    viewed_stack.push("PAT001 - Ramesh")
    viewed_stack.push("PAT004 - Anitha")
    viewed_stack.push("PAT005 - Suresh")

    print("Viewing history:", viewed_stack.display())
    print("Most recently viewed:", viewed_stack.peek())

    print("\nGoing back through history:")
    print("Previous patient:", viewed_stack.pop())
    print("Previous patient:", viewed_stack.pop())

    print("Remaining history:", viewed_stack.display())

    # Empty structure checks
    print("\n--- EMPTY STRUCTURE TESTS ---")

    empty_queue = PatientQueue()
    empty_stack = PatientStack()

    print("Dequeue from empty queue:", empty_queue.dequeue())
    print("Pop from empty stack:", empty_stack.pop())

    print("\nTask 4 completed successfully.")


if __name__ == "__main__":
    main()
