

class MatrixUnionFind:
    """ Union find for 2D matrix M-by-N 
    """
    def __init__(self, rows:int, cols:int):
        """ Initializes M-by-N matrix.

            Parameters:
            rows: size of the matrix m
            cols: size of the matrix n            
        """
        # Size of matrix
        self.__rowNum = rows
        self.__colNum = cols     
        # Matrix of roots
        self.__roots = [[[] for x in range(cols)] for y in range(rows)]
        # Matrix of sizes of each root
        self.__rootSizes = [[1 for x in range(cols)] for y in range(rows)]
        # Switch, if validation of each input of API will be done
        self.__isInputValidated = False

        # Initialize roots as coordinates of itself element
        for i, a_i in enumerate(self.__roots):
            for j, a_ij in enumerate(a_i):
                a_ij[:] = i, j
           

    @property
    def isInputValidated(self):
        return self.__isInputValidated


    @isInputValidated.setter
    def isInputValidated(self, x):
        self.__isInputValidated = x


    def __getRoot(self, row:int, col:int):
        """ Returns root of the input element with path compression.            

            Parameters:
            row: row number
            col: column number

            Returns:
            Root of the input element as list of row and column coordinates 
        """

        travRow = row
        travCol = col

        while(not self.isRoot(travRow, travCol)):
            r, c = self.__roots[travRow][travCol]
            # Move trav element under its grandparent
            self.__roots[travRow][travCol] = self.__roots[r][c]
            # Traverse the tree up            
            travRow, travCol = self.__roots[travRow][travCol]

        return [travRow, travCol]


    def __validateInput(self, row:int, col:int) -> None:
        """ Validate input values of row and col if parameter validateInput is set to True

            Throw exception in case of violation.

            Parameters:
            row: row number
            col: column number

            Returns:
            None
        """
        if self.__isInputValidated:
            if row >= self.__rowNum:
                raise ValueError(f"Row index {row} is greater than size of matrix {self.__rowNum}")            
            elif col >= self.__colNum:
                raise ValueError(f"Column index {col} is greater than size of matrix {self.__colNum}")
            elif row < 0 or col < 0:
                raise ValueError(f"{row} or {col} is smaller than 0")


    def __validateInputList(self, lst:list) -> None:
        """ Validate input values of row and col provided as list(row, col)

            Throw exception in case of violation.

            Parameters:
            lst: list(row, col) where row and col are array indices

            Returns:
            None
        """
        self.__validateInput(lst[0], lst[1])


    def isRoot(self, row:int, col:int) -> bool:
        """ Return information if input is root

            Parameters:
            row: row number
            col: column number

            Returns:
            True if input element is root otherwise False
        """
        self.__validateInput(row, col)

        return self.__roots[row][col] == [row, col]


    def isConnected(self, firstEl:list, secondEl:list) -> bool:
        """ Check if both input variables has the same root. 
            If roots are same the input elements are connected
            TODO: do it
            Parameters:
            firstEl: first element to be tested if they are connected. It is list of coordinates.
            secondEl: second element to be tested if they are connected. It is list of coordinates.

            Returns:
            True if input elements are connected otherwise False
        """

        self.__validateInputList(firstEl)
        self.__validateInputList(secondEl)

        firstRoot = self.__getRoot(firstEl[0], firstEl[1])
        secondRoot = self.__getRoot(secondEl[0], secondEl[1])

        return firstRoot == secondRoot


    def doUnion(self, firstEl:list, secondEl:list) -> None:
        """ Do union of input elements. At first get roots of both elements then
            check the size of first and second tree and link the smaller tree under
            larger tree.

            Parameters:
            firstEl: first element to be tested if they are connected. It is list of coordinates.
            secondEl: second element to be tested if they are connected. It is list of coordinates.

            Returns:
            None
        """
        self.__validateInputList(firstEl)
        self.__validateInputList(secondEl)

        firstRoot = self.__getRoot(firstEl[0], firstEl[1])
        secondRoot = self.__getRoot(secondEl[0], secondEl[1])

        if self.__rootSizes[secondRoot[0]][secondRoot[1]] <= self.__rootSizes[firstRoot[0]][firstRoot[1]]:
            self.__roots[secondRoot[0]][secondRoot[1]] = firstRoot
            self.__rootSizes[firstRoot[0]][firstRoot[1]] += self.__rootSizes[secondRoot[0]][secondRoot[1]]
        else:
            self.__roots[firstRoot[0]][firstRoot[1]] = secondRoot
            self.__rootSizes[secondRoot[0]][secondRoot[1]] += self.__rootSizes[firstRoot[0]][firstRoot[1]]
