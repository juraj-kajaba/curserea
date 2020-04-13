import pytest
from alg import merge_sort_bu as ms


def test_ms1():
    a = [2, 5, 6, 5, 4, 2, 1, 1, 3, 8, 7, 8, 8, 8, 8, 4,
         5, 7, 8, 7, 4, 5, 47, 4, 1, 2, 1, 2, 1, 2, 1, 2]
    b = ms.merge_sort_bu(a)
    assert sorted(a) == b


def test_ms2():
    a = [1] * 200
    b = ms.merge_sort_bu(a)
    assert sorted(a) == b


test_ms2()
