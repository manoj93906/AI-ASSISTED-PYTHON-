class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the end of the queue"""
        self.items.append(item)

    def dequeue(self):
        """Remove and return the front item of the queue"""
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)

    def peek(self):
        """Return the front item without removing it"""
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.items[0]

    def is_empty(self):
        """Check if the queue is empty"""
        return len(self.items) == 0

    def size(self):
        """Return the number of items in the queue"""
        return len(self.items)


# 🔹 Testing the Queue class
q = Queue()

# Scenario 1: Enqueue elements
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
print("Queue after enqueues:", q.items)

# Scenario 2: Peek at the front
print("Peek:", q.peek())  # Expected: 10

# Scenario 3: Dequeue elements
print("Dequeued:", q.dequeue())  # Expected: 10
print("Queue after dequeue:", q.items)

# Scenario 4: Multiple dequeues
print("Dequeued:", q.dequeue())  # Expected: 20
print("Dequeued:", q.dequeue())  # Expected: 30

# Scenario 5: Edge case - Dequeue from empty queue
try:
    q.dequeue()
except IndexError as e:
    print("Error:", e)

# Scenario 6: Edge case - Peek from empty queue
try:
    q.peek()
except IndexError as e:
    print("Error:", e)
