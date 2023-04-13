# Linked lists are an ordered collection of objects. So what makes them different from normal lists? Linked lists differ from lists in the way that they store elements in memory. While lists use a contiguous memory block to store references to their data, linked lists store references as part of their own elements.

# node contains data and next


# queue - FIFO
# stack - LIFO


#deque - deck - double-ended queue

from collections import deque

test = deque(['a','b','c'])


print(f"{test}")

test.append('d')
print(f"{test}")

test.appendleft('e')
print(f"{test}")

test.pop()
print(f"{test}")

test.popleft()
print(f"{test}")

queue = deque()

queue.append('a')
queue.append('b')
queue.append('c')
print(queue)


class Linked_list:
    def __init__(self):
        self.head = None
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return self.data

ll = Linked_list()
ll.head = Node("a")
ll.head.next = Node("b")
ll.head.next.next = Node("c")
ll.head.next.next.next = Node("d")
print(ll)

for node in ll:
    print(node)