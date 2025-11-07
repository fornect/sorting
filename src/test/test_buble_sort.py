from hypothesis import given
from hypothesis import strategies

from ..sorting.buble_sort import buble_sort

def test_bublesort1():
    assert buble_sort([35, 12, 43, 8, 51]) == [8, 12, 35, 43, 51]
    assert buble_sort([-3, 5, 2, -10, 44, 50, -7]) == [-10, -7, -3, 2, 5, 44, 50]


def test_extrem():
    assert buble_sort([]) == []
    assert buble_sort([0]) == [0]
    assert buble_sort([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]


@given(strategies.lists(strategies.integers(), max_size=100))
def test_property(arr):
    assert buble_sort(arr) == sorted(arr)
