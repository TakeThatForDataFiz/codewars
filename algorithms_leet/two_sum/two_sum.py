'''
two_sum.py - 
    Script designed to implement solution to two sum problem
    Author: John Lunz
'''


def two_sum_n2(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            if nums[i] + nums[j] == target:
                return [i, j]


def two_sum_hashed(nums, target):
    prev_hash = dict()
    for i, num in enumerate(nums):
        target_diff = target - num
        if target_diff in prev_hash.keys():
            return [prev_hash[target_diff], i]
        else:
            prev_hash[num] = i
