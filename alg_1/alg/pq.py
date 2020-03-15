""" Implementation of priority queue as max heap resp. min heap """

class PQ:
     

    def __init__(self, keys: list = None) -> None:
        """ Creates priority queue from given keys.

            Parameters:
            keys: input keys the priority queue is created from. If input
                  parameter is None, empty key array is created. 
        """
        self._keys = [] # input keys

        if keys:
            self._keys.extend(keys)
            self._heapify()
                


    def _compare(self, leftKey, rightKey):
        """ Compare keys in order to implement comaprision 
            according to type of heap.

            Returns:
            -1 : if leftKey is less then rightKey
             0 : if leftKey and rightKey are equal
             1 : if leftKey is greater then rightKey
        """
        raise NotImplementedError("_compare method must be implemented.")


    def _swap(self, index1, index2) -> None:
        """ Swap two keys and values

            Parameters:
            index1: index of first key to be swapped
            index2: index of second key to be swapped

            Returns:
            None
        """
        self._keys[index1], self._keys[index2] = self._keys[index2], self._keys[index1]



    def _sink(self, k) -> None:
        """ Sink the k-th node as deep as is possible.

            Parameters:
            k: index of the node to sink

            Returns:
            None
        """

        # while at least left child is not out of order of keys array
        while 2 * k + 1 < self.getSize():

            # Find the greater child first
            idxToCompare = 2 * k + 1
            if 2 * k + 2 < self.getSize() and self._compare(self._keys[2 * k + 1], self._keys[2 * k + 2]) < 0:
                idxToCompare = 2 * k + 2

            # Compare greater child and parent and swap them eventually
            if self._compare(self._keys[k], self._keys[idxToCompare]) < 0: 
                self._swap(k, idxToCompare)
                k = idxToCompare
            else:
                break



    def _swim(self, k) -> None:
        """ Swim the k-th node as up as is possible.

            Parameters:
            k: index of node to swim

            Returns:
            None
        """

        # while k is not out of array and parent is less then child
        while k > 0 and self._compare(self._keys[k // 2], self._keys[k]) < 0:
            # swap parent with child
            self._swap(k, k // 2)
            k = k // 2



    def _heapify(self):
        """ Make the instance to be valid binary heap.
            Take all nodes (under leaves) and sink them (bottom-up).

            Parameters:
            None

            Returns:
            None
        """
        for i in reversed(range(self.getSize() // 2)):
            self._sink(i)


    def _getHead(self):
        """ Returns the first element and make the heap """
        # Swap first and last element, remove the last one,
        # and sink the first one in order to make it heap again
        self._swap(0, self.getSize() -1)
        retVal = self._keys.pop()
        self._sink(0)
        return retVal 



    def getSize(self):
        """ Returns the size of heap
        """
        return len(self._keys)


    def insert(self, key) -> None:
        """ Inserts new key into PQ

            Parameters:
            key: key to be inserted into priority queue

            Returns:
            None
        """
        # Inserts the key at the end of array and swim the inserted key
        self._keys.append(key)
        self._swim(len(self._keys) - 1)



class MaxPQ(PQ):
    """ Max priority queue implementation """
    def _compare(self, leftKey, rightKey):
        """ Compare keys in order to implement comaprision 
            according to type of heap.

            Returns:
            -1 : if leftKey is less then rightKey
             0 : if leftKey and rightKey are equal
             1 : if leftKey is greater then rightKey
        """
        retVal = 0

        if leftKey < rightKey:
            retVal = -1
        elif leftKey > rightKey:
            retVal = 1
        
        return retVal

    def getMax(self):
        """ Returns max from max priority queue

            Returns: max from queue
        """

        return self._getHead() 



class MinPQ(PQ):
    """ Min priority queue implementation """
    def _compare(self, leftKey, rightKey):
        """ Compare keys in order to implement comaprision 
            according to type of heap.

            Returns:
            -1 : if leftKey is greater then rightKey
             0 : if leftKey and rightKey are equal
             1 : if leftKey is less then rightKey
        """
        retVal = 0

        if leftKey > rightKey:
            retVal = -1
        elif leftKey < rightKey:
            retVal = 1
        
        return retVal


    def getMin(self):
        """ Returns min from max priority queue

            Returns: min from queue
        """

        return self._getHead() 


