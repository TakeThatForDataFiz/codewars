import two_sum


def test_two_sum_edge():
    nums = [3, 2, 4]
    target = 6
    assert two_sum.two_sum_n2(nums, target) == [1, 2]


def test_two_sum_hashed():
    nums = [3, 2, 4]
    target = 6
    assert two_sum.two_sum_hashed(nums, target) == [1, 2]


def test_two_sum_hashed_2_elems():
    nums = [3, 3]
    target = 6
    assert two_sum.two_sum_hashed(nums, target) == [0, 1]
