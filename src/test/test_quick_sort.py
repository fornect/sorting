from hypothesis import given
from hypothesis import strategies

from ..sorting.quick_sort import quicksort

def test_quicksort1():
    assert quicksort([35, 12, 43, 8, 51]) == [8, 12, 35, 43, 51]
    assert quicksort([-3, 5, 2, -10, 44, 50, -7]) == [-10, -7, -3, 2, 5, 44, 50]


def test_extrem():
    assert quicksort([]) == []
    assert quicksort([0]) == [0]
    assert quicksort([0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0]


@given(strategies.lists(strategies.integers(), max_size=100))
def test_property(arr):
    assert quicksort(arr) == sorted(arr)
