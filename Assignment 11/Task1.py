class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

if __name__ == "__main__":
    stack = Stack()
    print("Is stack empty?", stack.is_empty())

    for value in [10, 20, 30]:
        stack.push(value)
        print(f"Pushed {value}, top is now {stack.peek()}")

    print("Is stack empty?", stack.is_empty())
    print("Peek:", stack.peek())

    while not stack.is_empty():
        print("Popped:", stack.pop())

    print("Is stack empty?", stack.is_empty())
  
