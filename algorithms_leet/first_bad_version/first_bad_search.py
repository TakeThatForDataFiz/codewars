'''
first_bad_search.py - 

    A python Script that utilizes Binary Search to find the first bad
    Product Version
Author: John Lunz
'''


def isBadVersion(n):
    '''Dummy Function created to prevent Syntax Errors'''
    return True


def find_first_bad_version(n):
    '''Function that finds the first Bad Version of a Product

    PARAMS
    ======
    n - int
      Number of Product Versions

    RETURNS
    =======
    version - int
       First Bad Version, returns -1 if no bad version exists
    '''
    # versions begin with 1 --> shift 1
    left, right = 1, n

    index = -1
    cond = True

    while cond:
        cond = left < right
        middle = left + (right - left) // 2
        if isBadVersion(middle) is True:
            index = middle
            right = middle
        else:
            left = middle + 1

    return index
