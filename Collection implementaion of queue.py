# Collection implementaion of queue

from queue import Queue

# Create a queue of integers
q = Queue()

# Enqueue elements
q.put(1)
q.put(2)
q.put(3)

# Iterate through and process each element
while not q.empty():
    element = q.get()
    print("Processing element:", element)

# Check if the queue is empty
if q.empty():
    print("Queue is empty")
else:
    print("Queue is not empty")
