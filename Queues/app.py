# In a stack, the last item we enter is the first to come out. In a queue, the first item we enter is the first come out.

from collections import deque

# Initializing a queue
q = deque()

# Adding elements to a queue
q.append('a')
q.append('b')
q.append('c')

print("Initial queue")
print(q)

# Removing elements from a queue
print("\nElements dequeued from the queue")
print(q.popleft())
print(q.popleft())
print(q.popleft())

print("\nQueue after removing elements")
print(q)

import queue

L = queue.Queue(maxsize=20)
L.put(10)
L.put(20)
print(L.get())
print(L.full())