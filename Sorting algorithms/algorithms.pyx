# %%cython -a
#cython: language_level=3
import cython
import numpy as np

@cython.cdivision(True)
@cython.boundscheck(False)
cpdef list sorted_cython(list array):
    return sorted(array)

@cython.cdivision(True)
@cython.boundscheck(False)
cpdef list bubble_sort_cython(list array):
    cdef int n = len(array)
    cdef int i,j
    cdef int already_sorted = 1

    for i in range(n):
        already_sorted = 1

        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                already_sorted = 0
        if already_sorted == 1: break
    return array

@cython.cdivision(True)
@cython.boundscheck(False)
cpdef list insertion_sort_cython(list array):
    cdef int i,j, key_item

    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item
    return array


