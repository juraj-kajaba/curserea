from alg import union_find as uf

ufo = uf.UnionFind(20)

connections = [(1, 2), (1,3), (1,4), (1,5), (2,6)]

for i in connections:
    ufo.doUnion(i[0], i[1])

for i in connections:
    assert ufo.isConnected(i[0], i[1]) == True



print(ufo.getArray())
print(ufo.getRootSizes())
