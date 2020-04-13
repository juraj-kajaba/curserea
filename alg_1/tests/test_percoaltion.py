import pytest
from alg import percolation as per


def test_per():
    p = per.Percolation(3)

    p.openSite(1, 2)
    assert not p.percolates()

    p.openSite(1, 1)
    assert not p.percolates()

    p.openSite(2, 0)
    assert not p.percolates()

    p.openSite(0, 0)
    assert not p.percolates()

    p.openSite(1, 0)
    assert p.percolates()

    p.openSite(0, 2)
    assert p.percolates()

    p.openSite(2, 2)
    assert p.percolates()


def test_per2():
    p = per.Percolation(10)

    for i in range(6):
        p.openSite(i, 0)

    assert not p.percolates()

    for i in range(9, 5, -1):
        p.openSite(i, 1)

    assert not p.percolates()

    p.openSite(5, 1)

    assert p.percolates()


# test_per()
test_per2()
