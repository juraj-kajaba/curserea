# isRoot
# isConnected
# union


class unionFindMat:
    """ Union find for 2D matrix N-by-N 
    Matrix will be internally 3D matrix. First two elemnts contains coordinates of root and third 
    element is size of respecting subtree.
    """
    def __init__(self, n):
        self._array = [[[1]*3 for x in range(n)] for y in range(n)]

        for i, a_i in enumerate(self._array):    
            for j, a_ij in enumerate(a_i):
                a_ij[0:2] = i, j
        
    


# a = [[None]*3]*3

n = 3



print(a)
