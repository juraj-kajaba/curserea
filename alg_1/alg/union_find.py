


class UnionFind:
    """ Simple union find implementation 
    """
    def __init__(self, n):
        """ 
        Parameters:
        n: number of possible elements
        """
        self.__array = [x for x in range(n)]
        self.__rootSizes = [1]*n
        self.__rootDepths = [1]*n        
        self.__maxRootSize = 1
        self.__maxRootDepth = 1        


    def getMaxRootSize(self):
        return self.__maxRootSize


    def getMaxRootDepth(self):
        return self.__maxRootDepth


    def __getRoot(self, element:int):
        """ Returns root of the input element

        Parameters:
        element: input whose root is returned

        Returns:
        Root of the input element
        """
        trav = element

        while(not self.isRoot(trav)):
            trav = self.__array[trav]

        return trav



    def isRoot(self, element:int) -> bool:
        """ Return information if input is root

            Parameters:
            element: input to be tested

            Returns:
            True if input element is root otherwise False
        """
        return self.__array[element] == element


    def isConnected(self, firstEl:int, secondEl:int) -> bool:
        """ Check if both input variables has the same root. 
            If roots are same the input elements are connected

            Parameters:
            firstEl: first element to be tested if they are connected
            secondEl: second element to be tested if they are connected

            Returns:
            True if input elements are connected otherwise False
        """
        firstRoot = self.__getRoot(firstEl)
        secondRoot = self.__getRoot(secondEl)

        return firstRoot == secondRoot

    def doUnion(self, firstEl:int, secondEl:int) -> None:
        """ Do union of input elements. At first get roots of both elements and
            afterwards make root of secondEl to be the root of firstEl

            Parameters:
            firstEl: first element to be tested if they are connected
            secondEl: second element to be tested if they are connected

            Returns:
            None
        """
        firstRoot = self.__getRoot(firstEl)
        secondRoot = self.__getRoot(secondEl)

        self.__array[firstRoot] = secondRoot
        self.__rootSizes[secondRoot] += self.__rootSizes[firstRoot]
        newDepth = self.__rootDepths[secondRoot] + 1
        self.__rootDepths[secondRoot] = max(self.__rootDepths[secondRoot], newDepth)
        # self.__rootDepths[secondRoot] += 1
        self.__maxRootSize = max(self.__maxRootSize, self.__rootSizes[secondRoot])
        self.__maxRootDepth = max(self.__maxRootDepth, self.__rootDepths[secondRoot])


    def getArray(self):
        """ Temporary test method, will be deleted
        """
        return self.__array

    def getRootSizes(self):
        """ Temporary test method, will be deleted
        """
        return self.__rootSizes

    def getRootDepths(self):
        """ Temporary test method, will be deleted
        """
        return self.__rootDepths


