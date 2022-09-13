'''
binary_search.py -
   Script that implements basic binary search algorithm in Python 3.10.4
   algorithm must have O(log n) runtime complexity

Author: John Lunz
'''


def binary_search_recursive(target, haystack, start, end):
    '''
    function that finds and returns index of target in
    haystack, returns -1 if not found
    '''
    if start <= end:
        midpoint = (start+end)//2

        if haystack[midpoint] == target:
            return midpoint
        if haystack[midpoint] > target:
            return binary_search_recursive(target, haystack, start, midpoint - 1)
        elif haystack[midpoint] < target:
            return binary_search_recursive(target, haystack, midpoint + 1, end)
    return -1
