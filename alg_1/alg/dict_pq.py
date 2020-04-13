""" Implementation of priority queue as max heap resp. min heap
    where change priority queue is supported. Input keys in this heap
    consists of tuple (priority, value) where value object can be in 
    heap only once.
"""
from alg import pq as pq


class DictPQ(pq.PQ):

    def __init__(self, keys: list = None) -> None:
        """ Creates priority queue from given keys where keys are 
            tuples of priority and value. There cannot be duplicite values 
            in tuples (otherwise ValueError exception is thrown) because 
            internal dictionary is used to store them.

            Parameters:
            keys: input keys the priority queue is created from. If input
                  parameter is None, empty key array is created. Keys are supposed to be
                  tuples of priority and value (priority, value).
        """
        self._values = {}  # values i.e. second value of key tuple

        if keys is not None:
            for i, v in enumerate(keys):
                self._values[v[1]] = i

        super().__init__(keys)

        # Check for duplicite values in self._values and self._keys
        # If sizes of values dict and keys array are not the same
        # raise the ValueError exception
        if len(self._values) != len(self._keys):
            raise ValueError(
                f"There must be duplicities in values of input keys.")

    def _swap(self, index1, index2) -> None:
        """ Swap two keys and values

            Parameters:
            index1: index of first key to be swapped
            index2: index of second key to be swapped

            Returns:
            None
        """
        v1 = self._keys[index1][1]
        v2 = self._keys[index2][1]
        self._values[v1], self._values[v2] = self._values[v2], self._values[v1]
        super()._swap(index1, index2)

    def _getHead(self):
        """ Returns the first element and make the heap. Deletes
            the value of key from dictionary afterwards.
        """
        retVal = super()._getHead()
        del self._values[retVal[1]]
        return retVal

    def insert(self, key: tuple) -> None:
        """ Inserts new key into PQ

            Parameters:
            key: key to be inserted into priority queue is supposed to
                 consists of key as first element and value as second 
                 element.

            Returns:
            None

            Raise KeyError if key is already in priority queue
        """
        # If value is already in the array raise KeyError exception
        if key[1] in self._values:
            raise KeyError(f"Value {key[1]} is already in dictheap.")
        self._values[key[1]] = self.getSize()  # assumed new size of keys array
        super().insert(key)


    def changePriority(self, changedElem: tuple) -> None:
        """ Change priority of key in the queue. Input parameter is
            tuple consisting of (newPriority, key).

            Parameters:
            key: key whose priority is to be changed
            newPriority: tuple with new priority of (newPriority, key)

            Returns:
            None
        """
        idx = self._values[changedElem[1]]
        self._keys[idx] = changedElem
        self._swim(idx)
        self._sink(idx)


class MaxDictPQ(DictPQ):
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


class MinDictPQ(DictPQ):
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
