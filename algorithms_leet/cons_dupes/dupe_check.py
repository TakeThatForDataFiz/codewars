

def sorted_solution(nums):
    temp = sorted(nums)
    for i in range(len(temp)-1):
        if temp[i] != temp[i+1]:
            continue
        else:
            return True
    return False


def hash_solution(nums):
    hashset = set()
    for num in nums:
        if num in hashset:
            return True
        hashset.add(num)
    return False
