""" Implementation of array which is always sorted """


class SortedArray:

    def __init__(self):
        """ Creates empty array
        """
        self._arr = []

    def _getFirstGreaterElem(self, elem) -> int:
        """ Find the first element greater than input using binary search.

            Parameters:
            elem: input element to be compared

            Returns:
            Index of first element greater then input element. If there is 
            not such element returns None
        """

        retVal = 0
        lo = 0
        hi = len(self._arr) - 1

        if len(self._arr) == 0 or self._arr[hi] < elem:
            return None

        while lo <= hi:
            if lo == hi:
                retVal = lo
                break

            middle = (lo + hi) // 2
            if elem < self._arr[middle]:
                hi = middle
            elif lo == middle:
                lo = hi
            else:
                lo = middle

        return retVal


    def insert(self, elem) -> None:
        """ Inserts element into sorted array on the right 
            place according to its value

            Parameters:
            elem: element to be inserted

            Returns:
            None
        """
        # Find the position of the first greater element them elem
        # and insert it before it

        idx = self._getFirstGreaterElem(elem)
        if idx is None:
            self._arr.append(elem)
        else:
            self._arr.append(elem)  # just to make the place in array
            self._arr[idx + 1:] = self._arr[idx: len(self._arr) - 1]
            self._arr[idx] = elem


a = SortedArray()

l = [3, 1, 2, 4, 1, 5, 2, 4, 4, 4, 4, 8, 7, 4, 5, 1, 0, 0, 1, 2, 1, 0]

for i in l:
    a.insert(i)

print(a._arr)
