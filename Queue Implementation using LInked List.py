# Linked List Implemetation of Queue 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if not self.rear:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.front:
            return None
        data = self.front.data
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return data

    def is_empty(self):
        return self.front is None

    def peek(self):
        if not self.front:
            return None
        return self.front.data

    def display(self):
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

# Example usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue:")
queue.display()  # Output: 1 2 3

print("Dequeue:", queue.dequeue())  # Output: Dequeue: 1
print("Queue:")
queue.display()  # Output: 2 3
