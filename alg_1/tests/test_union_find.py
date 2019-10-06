from alg import union_find as uf
from alg import quick_union_find as quf
from alg import quick_union_find2 as quf2

def test_uf_1():
    ufo = uf.UnionFind(20)

    connections = [(1, 2), (1,3), (1,4), (1,5), (2,6)]

    for i in connections:
        ufo.doUnion(i[0], i[1])

    for i in connections:
        assert ufo.isConnected(i[0], i[1]) == True

    print(ufo.getArray())
    print(ufo.getRootSizes())
    print(ufo.getMaxRootSize())


def test_uf_2():
    ufo = uf.UnionFind(10)

    connections = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1), (5, 0), (7, 2), (6,1), (7, 3)]

    for i in connections:
        ufo.doUnion(i[0], i[1])

    for i in connections:
        assert ufo.isConnected(i[0], i[1]) == True

    print(ufo.getArray())
    print(ufo.getRootSizes())
    print(ufo.getRootDepths())    
    print(ufo.getMaxRootSize())
    print(ufo.getMaxRootDepth())


def test_quf():
    ufo = quf.QuickUnionFind(10)

    connections = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1), (5, 0), (7, 2), (6,1), (7, 3)
    ]

    for i in connections:
        ufo.doUnion(i[0], i[1])

    for i in connections:
        assert ufo.isConnected(i[0], i[1]) == True

    print(ufo.getArray())
    print(ufo.getRootSizes())
    print(ufo.getRootDepths())    
    print(ufo.getMaxRootSize())
    print(ufo.getMaxRootDepth())

def test_quf2():
    ufo = quf2.QuickUnionFind2(10)

    connections = [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1), (5, 0), (7, 2), (6,1), (7, 3)
    ]

    for i in connections:
        ufo.doUnion(i[0], i[1])

    for i in connections:
        assert ufo.isConnected(i[0], i[1]) == True

    print(ufo.getArray())
    print(ufo.getRootSizes())
    print(ufo.getMaxRootSize())


test_uf_2()
test_quf()
test_quf2()