from statistics import multimode

def highest_rank(arr):
    return max(multimode(arr))

print(highest_rank([12, 13, 8, 12, 7, 6, 4, 13, 12, 13]))