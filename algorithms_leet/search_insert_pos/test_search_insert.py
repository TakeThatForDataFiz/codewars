'''
test_search_insert.py
    Test Script to check the search insert function for correctness
'''
from search_insert import search_insert
import pytest


@pytest.fixture
def get_nums():
    return [1, 3, 5, 6]


def test_search_insert_existing(get_nums):
    target = search_insert(nums=get_nums, target=5)
    assert target == 2


def test_search_insert_nonexisting(get_nums):
    target = search_insert(nums=get_nums, target=2)
    assert target == 1


def test_search_insert_nonexisting_large(get_nums):
    target = search_insert(nums=get_nums, target=7)
    assert target == 4


def test_search_single_item():
    nums = [1]
    target = search_insert(nums=nums, target=1)
    assert target == 0
