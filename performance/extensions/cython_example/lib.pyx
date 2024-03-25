def sum_list_cython(list lst):
    cdef int s = 0
    cdef int item
    for item in lst:
        s += item
    return s
