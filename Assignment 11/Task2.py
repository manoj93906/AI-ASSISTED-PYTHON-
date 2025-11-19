class Queue:
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)

    def is_empty(self):
        return len(self._items) == 0


if __name__ == "__main__":
    queue = Queue()
    print("Is queue empty?", queue.is_empty())

    for value in [1, 2, 3]:
        queue.enqueue(value)
        print(f"Enqueued {value}")

    print("Is queue empty?", queue.is_empty())

    while not queue.is_empty():
        print("Dequeued:", queue.dequeue())

    print("Is queue empty?", queue.is_empty())
  
