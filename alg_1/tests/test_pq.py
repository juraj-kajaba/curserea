from alg import pq as pq

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

    assert sorted(l) == list(reversed(z))



test_maxPQ()
test_minPQ()
