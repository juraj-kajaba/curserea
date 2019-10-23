from alg import matrix_union_find as muf


class Percolation:
    """ Uses matrix union find algorithm. First and last row of matrix are initially connected
        (these are artifitiall layers) to be able to find out percolation with test if some element 
        of first and last row are connected.        
    """
    def __init__(self, n:int):
        """ Initializes instance for matrix union find and site statuses.

            Parameters:
            n: size of the matrix
        """
        self.__n = n
        # First and last row are artificial rows
        self.__muf = muf.MatrixUnionFind(n+2, n)
        # Matrix of site statuses. Initially are all sites closed
        self.__siteStates = [[False for x in range(n)] for y in range(n+2)]


        # First and last layer are connected and sites are open
        for i in range(0,n):
            self.__siteStates[0][i] = True
            self.__muf.doUnion([0, 0],[0, i])
            self.__siteStates[n+1][i] = True
            self.__muf.doUnion([n+1, 0],[n+1, i])            



    def openSite(self, row:int, col:int) -> None:
        """ Opens site and do unions with neighbors which are open.

            Parameters:
            row: row of cell to be open
            col: column of cell to be open

            Returns:
            None
        """

        row += 1 # hence first row is artificial
        self.__siteStates[row][col] = True

        # Check all connection along the site
        if row > 0 and self.__siteStates[row-1][col]: # Upper site is open ?
            self.__muf.doUnion([row, col], [row-1, col])

        if row < self.__n+1 and self.__siteStates[row+1][col]: # Bottom site is open ?
            self.__muf.doUnion([row, col], [row+1, col])

        if col > 0 and self.__siteStates[row][col-1]: # Left site is open ?
            self.__muf.doUnion([row, col], [row, col-1])

        if col < self.__n-1 and self.__siteStates[row][col+1]: # Right site is open ?
            self.__muf.doUnion([row, col], [row, col+1])


    def percolates(self) -> bool:
        """ Does the system percolate?
            Parameters:
            None

            Returns:
            boolean: True if system percolates
        """
        return self.__muf.isConnected([0, 0], [self.__n + 1, 0])


