import pytest
from alg import quick_select as qs


def test_1():
    arr = [5,4,3,20,1,34,4,21,43,10,23323,32,22]

    assert qs.qsel(arr, 2) == 4

def test_2():

    arr = [5, 4]
    assert qs.partition_3w(arr, 0, 1) == (1, 1)
    assert arr == [4, 5]

    arr = [4, 5]
    assert qs.partition_3w(arr, 0, 1) == (0, 0)
    assert arr == [4, 5]

    arr = [5, 5]
    assert qs.partition_3w(arr, 0, 1) == (0, 1)
    assert arr == [5, 5]

    arr = [5, 4, 5, 4]
    assert qs.partition_3w(arr, 0, 3) == (2, 3)
    assert arr == [4, 4, 5, 5]

    arr = [5, 4, 3, 20, 1, 34, 4, 5, 43, 5, 4, 5, 5]
    assert qs.partition_3w(arr, 0, 12) == (5, 9)
    assert arr == [4, 3, 1, 4, 4, 5, 5, 5, 5, 5, 43, 34, 20]


def test_3():
    a = [2,5,6,5,4,2,1,1,3,8,7,8,8,8,8,4,5,7,8,7,4,5,47,4,1,2,1,2,1,2,1,2]
    b = a.copy()
    qs.qsort(a)
    assert sorted(b) == a

    a = [5,4,3,20,1,34,4,5,43,10,23323,32,22]
    b = a.copy()
    qs.qsort(a)
    assert sorted(b) == a


# test_3()

