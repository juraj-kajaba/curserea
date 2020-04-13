from alg import pq as pq
from alg import dict_pq as dpq
import pytest


def test_minPQ():
    l = [1, 10, 11, 5, 20, 1, 1, 34, 54, 65, 23, 23, 54, 75, 8, 87]

    # Test with HeapSort
    a = pq.MinPQ(l)

    z = []

    while a.getSize() > 0:
        z.append(a.getMin())

    assert sorted(l) == z


def test_maxPQ():
    l = [1, 10, 11, 5, 20, 1, 1, 34, 54, 65, 23, 23, 54, 75, 8, 87]

    # Test with HeapSort
    a = pq.MaxPQ(l)

    z = []

    while a.getSize() > 0:
        z.append(a.getMax())

    assert sorted(l, reverse=True) == z


def test_minDPQ_1():
    l = []
    l.append((1, 'a'))
    l.append((2, 'b'))
    l.append((3, 'c'))
    l.append((3, '1'))

    b = dpq.MinDictPQ(l)

    assert b.getMin()[1] == 'a'
    assert b.getMin()[1] == 'b'

    # Next two elements from PQ has same priority so both result are correct
    res = b.getMin()[1]
    assert res == 'c' or res == '1'

    res = b.getMin()[1]
    assert res == 'c' or res == '1'


def test_maxDPQ_2():
    a = dpq.MinDictPQ()

    a.insert((1, 'a'))
    a.insert((2, 'b'))
    a.insert((3, 'c'))
    a.insert((3, '1'))


def test_minDPQ_3():

    with pytest.raises(ValueError):
        l = []
        l.append((1, 'a'))
        l.append((2, 'b'))
        l.append((3, 'c'))
        l.append((3, '1'))
        l.append((2, 'b'))

        b = dpq.MaxDictPQ(l)


def test_maxDPQ_4():

    with pytest.raises(KeyError):
        a = dpq.MinDictPQ()

        a.insert((1, 'a'))
        a.insert((2, 'b'))
        a.insert((3, 'c'))
        a.insert((3, '1'))
        a.insert((3, '1'))


def test_minDPQ_5():

    b = dpq.MinDictPQ()
    b.insert((1, 'a'))
    b.insert((2, 'b'))
    b.insert((3, 'c'))
    b.insert((3, '1'))

    b.changePriority((0, 'c'))

    assert b.getMin()[1] == 'c'
    assert b.getMin()[1] == 'a'
    assert b.getMin()[1] == 'b'
    assert b.getMin()[1] == '1'

    b = dpq.MinDictPQ()
    b.insert((1, 'a'))
    b.insert((2, 'b'))
    b.insert((3, 'c'))
    b.insert((3, '1'))

    b.changePriority((5, 'b'))
    b.changePriority((2, 'c'))

    assert b.getMin()[1] == 'a'
    assert b.getMin()[1] == 'c'
    assert b.getMin()[1] == '1'
    assert b.getMin()[1] == 'b'


# test_minDPQ_1()
# test_maxDPQ_2()
# test_minDPQ_3()
# test_maxDPQ_4()
test_minDPQ_5()


# test_maxPQ()
# test_minPQ()
