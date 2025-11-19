class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head

        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        elements = []
        current = self.head

        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) if elements else "List is empty"

if __name__ == "__main__":
    linked_list = SinglyLinkedList()
    print(linked_list.display())

    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)
    print("After inserting at end:", linked_list.display())
    
    linked_list.insert_at_beginning(5)
    linked_list.insert_at_beginning(0)
    print("After inserting at beginning:", linked_list.display())
  
