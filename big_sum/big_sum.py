import numpy as np


def big_sum(n):
    # use numpy to use C to handle large scale arithmetic
    return np.sum(n)


def big_sum_no_imports(n):
    tot = 0
    for num in n:
        tot += num
    return tot
