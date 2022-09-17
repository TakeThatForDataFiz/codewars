'''
search_insert.py - 
    A python script that uses binary search to
    return index or hypothetical index of target integer
Author: John Lunz
'''


def search_insert(nums, target):
    left, right = 0, len(nums)-1
    while left <= right:
        middle = left + (right - left)//2
        if nums[middle] < target:
            left = middle + 1
        else:
            if nums[middle] == target and nums[middle-1] != target:
                return middle
            else:
                right = middle - 1

    return left
