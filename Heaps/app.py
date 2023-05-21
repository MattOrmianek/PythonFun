#heap queue algorithm


# heapify - converts a regular list to a heap
# heappush - function adds an element to the heap without altering the current heap
# heappop - function returns the smalles data element from the heap
# heapreplace - function replaces the smalles data element with a new value supplied in the function

import heapq

A = [21,1,45,78,3,5]
B = [17,17,2,3,4]
heapq.heapify(A)
heapq.heapify(B)

print(f"A: {A}")
print(f"B: {B}")

heapq.heappop(A)

print(f"A: {A}")
heapq.heappush(A,2)
print(f"A: {A}")

