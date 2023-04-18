# %%cython -a
#cython: language_level=3
import cython
import numpy as np
from random import randint

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


@cython.cdivision(True)
@cython.boundscheck(False)
cpdef list quicksort_cython(list array):
    cdef list low, same, high
    cdef int pivot
    cdef int len_of_array = len(array)
    cdef int item

    if len_of_array < 2:
        return array

    low, same, high = [], [], []

    # Select your `pivot` element randomly
    pivot = array[randint(0, len_of_array - 1)]

    for item in array:
        # Elements that are smaller than the `pivot` go to
        # the `low` list. Elements that are larger than
        # `pivot` go to the `high` list. Elements that are
        # equal to `pivot` go to the `same` list.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)

    # The final result combines the sorted `low` list
    # with the `same` list and the sorted `high` list
    return quicksort_cython(low) + same + quicksort_cython(high)