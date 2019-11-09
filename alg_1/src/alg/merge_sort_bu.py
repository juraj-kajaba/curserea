""" MergeSort Bottom up """
import math


def merge(arr: list, left: int, middle: int, right: int, tmp: list):

    i = left
    j = middle
    k = left

    while i < middle or j < right:

        if arr[i] < arr[j]:
            tmp[k] = arr[i]
            i += 1
            k += 1
        else:
            tmp[k] = arr[j]
            j += 1
            k += 1
        
        # Check if one array is not exhausted. If yes just copy not 
        # exhausted array into result array tnp
        if i == middle:
            while j < right:
                tmp[k] = arr[j]
                j += 1
                k += 1

        if j == right:
            while i < middle:
                tmp[k] = arr[i]
                i += 1
                k += 1

    # Copy sorted elements into original array
    for i in range(left, right):
        arr[i] = tmp[i]


def merge_sort_bu(inArr: list):
    """ Always merge intervals as if count of elements to be sorted is pow(2,k)
        and cap the indices for merge procedure.
        
        Parameters:
        inArrr: input list to be sorted

        Return:
        sorted copy of input array
    """
    arr = inArr.copy()
    n = len(inArr)

    if n == 0:
        return []

    tmp = [0] * n

    iterNum = math.ceil(math.log2(n)) # number of iterations
    maxIndex = math.pow(2, iterNum)

    for i in range(iterNum):
        width = int(math.pow(2, i))
        right = 0
        while right < maxIndex:
            left = right
            middle = min(left + width, n - 1)
            right = min(left + 2*width, n)
            merge(arr, left, middle, right, tmp)

            if right == n:
                break

    return arr



