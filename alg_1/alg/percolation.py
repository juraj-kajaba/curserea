import random
import math
import time
from alg import matrix_union_find as muf


class Percolation:
    """ Uses matrix union find algorithm. First and last row of matrix are initially connected
        (these are artifitiall layers) to be able to find out percolation with test if some element 
        of first and last row are connected.        
    """

    def __init__(self, n: int):
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
        for i in range(0, n):
            self.__siteStates[0][i] = True
            self.__muf.doUnion([0, 0], [0, i])
            self.__siteStates[n+1][i] = True
            self.__muf.doUnion([n+1, 0], [n+1, i])

    def openSite(self, row: int, col: int) -> None:
        """ Opens site and do unions with neighbors which are open.

            Parameters:
            row: row of cell to be open
            col: column of cell to be open

            Returns:
            None
        """

        row += 1  # hence first row is artificial
        self.__siteStates[row][col] = True

        # Check all connection along the site
        if row > 0 and self.__siteStates[row-1][col]:  # Upper site is open ?
            self.__muf.doUnion([row, col], [row-1, col])

        # Bottom site is open ?
        if row < self.__n+1 and self.__siteStates[row+1][col]:
            self.__muf.doUnion([row, col], [row+1, col])

        if col > 0 and self.__siteStates[row][col-1]:  # Left site is open ?
            self.__muf.doUnion([row, col], [row, col-1])

        # Right site is open ?
        if col < self.__n-1 and self.__siteStates[row][col+1]:
            self.__muf.doUnion([row, col], [row, col+1])

    def percolates(self) -> bool:
        """ Does the system percolate?
            Parameters:
            None

            Returns:
            boolean: True if system percolates
        """
        return self.__muf.isConnected([0, 0], [self.__n + 1, 0])


class PercolationStats:
    """ Calculates statistical attributes of Percolation system
    """

    def __init__(self, n: int, trials: int):
        """ perform independent trials on an n-by-n grid
        """
        self.__n = n
        self.__results = []
        self.__mean = 0
        self.__stdDev = 0
        self.__confIntLow = 0
        self.__confIntHigh = 0

        for _ in range(trials):
            self.__results.append(self.__getCountToPercolation() / (n * n))

        self.__calculateStats()

    def getResults(self):
        return self.__results

    def __initBlockedSites(self) -> list:
        """ Return initialized block sites list.
            Initially are all sites blocked

            Returns:
            initialized block sites list
        """
        blockedSites = []

        for i in range(self.__n):
            for j in range(self.__n):
                blockedSites.append((i, j))

        return blockedSites

    def __getCountToPercolation(self) -> int:
        """ Randomly the sites are open till the system percolated

            Returns:
            Number of open sites till system percolated
        """
        retVal = 0
        per = Percolation(self.__n)
        blockedSites = self.__initBlockedSites()

        while True:
            c = self.__getRandomBlockedSite(blockedSites)
            per.openSite(c[0], c[1])
            retVal += 1
            if per.percolates():
                break

        return retVal
    def __getRandomBlockedSite(self, blockedSites: list) -> tuple:
        """ Returns randomly some of the blocked sites

            Returns:
            randomly some of the blocked sites
        """
        idx = random.randint(0, len(blockedSites)-1)
        return blockedSites.pop(idx)

    def __calculateStats(self) -> None:
        """ Calculates all statistical attributes
        """
        self.__mean = sum(self.__results)/len(self.__results)

        sm = 0
        for i in self.__results:
            sm += (i - self.__mean) ** 2

        self.__stdDev = math.sqrt(sm / (self.__n - 1))
        self.__confIntLow = self.__mean - 1.96 * \
            self.__stdDev / math.sqrt(self.__n)
        self.__confIntHigh = self.__mean + 1.96 * \
            self.__stdDev / math.sqrt(self.__n)

    def getMean(self) -> float:
        """ Sample mean of percolation threshold

            Returns:
            float: returns mean of percolation threshold
        """
        return self.__mean

    def getStdDev(self) -> float:
        """ Sample standard deviation of percolation threshold

            Returns:
            float: standard deviation of percolation threshold
        """
        return self.__stdDev

    def getConfidenceLow(self) -> float:
        """ Low endpoint of 95% confidence interval

            Returns:
            float: low endpoint of 95% confidence interval
        """
        return self.__confIntLow

    def getConfidenceHigh(self) -> float:
        """ High endpoint of 95% confidence interval

            Returns:
            float: high endpoint of 95% confidence interval
        """
        return self.__confIntHigh


# Calculate and print statistics
t = time.process_time()
st = PercolationStats(200, 10)
elapsed_time = time.process_time() - t

print(f"Mean\t\t\t{st.getMean()}")
print(f"Standard deviation\t{st.getStdDev()}")
print(
    f"95% confidence interval [{st.getConfidenceLow()}, {st.getConfidenceHigh()}]")
print(f"Time elapsed\t\t{elapsed_time:.2f} s")
