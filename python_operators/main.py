"""
link: https://www.youtube.com/watch?v=n9w2U7ImsKI
"""

import numpy as np

a: set[int] = {1, 2, 3}
b: set[int] = {3, 4, 5}

print("union: \n", a | b)
print("intersection: \n", a & b)
print("difference: \n", a - b)
print("symmetric difference: \n", a ^ b)

A = np.array([[1, 2], [4, 5]])
B = np.array([[1, 2], [4, 5]])

print("snail operator: \n", A @ B)  # this is matrix multiplication
print("element-wise multiplication: \n", A * B)  # this is element-wise multiplication


print("bitwise NOT: \n", ~5)
bool_array = np.array([1, 0, 1, 0], dtype=bool)
print("bitwise NOT: \n", ~bool_array)

list_of_numbers = [1, 2, 3, 4, 5]
a, *b = list_of_numbers
print(a, b)
print(type(a), type(b))

# Testing if * varaible is always a list
list_of_numbers.pop()
list_of_numbers.pop()
list_of_numbers.pop()
c, *d = list_of_numbers
print(c, d)
print(type(c), type(d))


a: float = 1.1
b: int = 3
print(a / b)
print(a // b)
print(a % b)


_ = 5
__ = 10
print("what is this: ", _ + __)
print("what is this: ", __ - _ - __ - -_)
