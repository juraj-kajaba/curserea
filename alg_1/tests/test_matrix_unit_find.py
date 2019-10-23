import pytest
from alg import matrix_union_find as muf


def test_muf_s():
    m = muf.MatrixUnionFind(3, 3)

    assert not m.isInputValidated
    m.isInputValidated = True
    assert m.isInputValidated


def test_muf():
    p = muf.MatrixUnionFind(4, 3)

    assert p.isRoot(1,2) == True

    p.doUnion([1,1],[1,2])

    p.isInputValidated = True
    assert p.isInputValidated

    with pytest.raises(ValueError):
        p.doUnion([1,1],[1,4]) # raised ValueError

    p.doUnion([2,1],[1,1])

    assert not p.isRoot(1,2)

    assert p.isConnected([1,1],[1,2])
    assert p.isConnected([2,1],[1,1])
    assert not p.isConnected([0,1],[1,1])



# test_muf_s()
# test_muf()
