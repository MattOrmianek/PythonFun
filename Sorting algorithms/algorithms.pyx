# %%cython -a
#cython: language_level=3
import cython
import numpy as np

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