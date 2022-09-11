'''
test_binary_search.py - 

    PyTest Script that checks binary_search.py script
'''
import binary_search as bs
import pytest


@pytest.fixture
def create_sample_setup():
    target = 9
    haystack = [-1, 0, 3, 5, 9, 12]
    return (target, haystack)


def test_binary_search_returns_neg_1_not_found(create_sample_setup):
    target, haystack = create_sample_setup
    target = 10
    index = bs.binary_search_recursive(target, haystack, 0, len(haystack)-1)
    assert index == -1


def test_binary_search(create_sample_setup):
    target, haystack = create_sample_setup
    index = bs.binary_search_recursive(target, haystack, 0, len(haystack)-1)
    assert index == 4
