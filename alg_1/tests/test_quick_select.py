import pytest
from alg import quick_select as qs


def test_1():
    arr = [5,4,3,20,1,34,4,21,43,10,23323,32,22]

    assert qs.qsel(arr, 2) == 4



test_1()

