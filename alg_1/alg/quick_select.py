""" Implements quick select algorithm based on QuickSearch """

import random


def swap(arr: list, i: int, j: int) -> None:
    """  Swaps two elements in the array

        Parameters:
        arr: list where swap takes place
        i: first index
        j: second index

        Returns:
        None
    """
    arr[i], arr[j] = arr[j], arr[i]



def partition(arr: list, lo: int, hi: int) -> int:
    """ Partition the input array in defined boundaries. 
        Partition key is first element.
        Funtion ensures that partition key is in the place afterwards.
        Duplicate partition keys can be either on the left side or right side from the 
        partiion key.

        Parameters:
        arr: list to be partitioned
        lo: low boundary to be partitioned
        hi: high boundary to be partitioned

        Returns:
        index of partitioned eleemnts
    """    
    i = lo
    j = hi
    k = arr[lo] # partition element

    while True:
        while k >= arr[i] and i < hi:
            i += 1

        while k <= arr[j] and j > lo:
            j -= 1

        if i >= j:
            break
        
        swap(arr, i, j)
            
    # Place partition key
    swap(arr, j, lo)

    return j


def partition_3w(arr: list, lo: int, hi: int) -> tuple:
    """ Partition the input array in defined boundaries by Dikstra's 3 way
        partitioning. Partition key is first element.
        Funtion ensures that partition key is in the place afterwards.
        Duplicate partition keys are placed on the right place.

        Parameters:
        arr: list to be partitioned
        lo: low boundary to be partitioned
        hi: high boundary to be partitioned

        Returns:
        indoces of partitioned eleemnts as tuple of low and high index
    """    
    lt = lo # first index of partition element
    i = lo # current index of the search
    gt = hi # max index to be searched for
    p = arr[lo] # partition element

    if lo >= hi:
        return (None, None)

    while i <= gt:
        if arr[i] < p:
            swap(arr, i, lt)
            i += 1
            lt += 1            
        elif arr[i] > p:
            swap(arr, i, gt)
            gt -= 1
        elif arr[i] == p:
            i += 1
        
    return (lt, gt)




def qsel(arr: list, k: int) -> int:
    """ Selects k-th largest element from the list.
        Take the partiions key and place it in its place in sorted array
         - partition function. compare arr[partiion index] element and
        set the low and high boundaries for next partiotioning accordingly.


        Parameters:
        arr: input list to be searched
        k: index

        Returns:
        k-th largest element from the list (k is zero based index)
    """

    random.shuffle(arr)

    lo = 0
    hi = len(arr) - 1

    while True:
        j = partition(arr, lo, hi)

        # Check where is partitioned eleemnt. 

        if k == j:
            break
        elif k > j:
            lo = j + 1
        else:
            hi = j - 1

    return arr[j]




def qsort(arr: list) -> None:
    """ Quicksort by using 3 way partitioning.


        Parameters:
        arr: input list to be sorted in-place

        Returns:
        None
    """
    # random.shuffle(arr)

    _qsort(arr, 0, len(arr) - 1)


def _qsort(arr: list, lo: int, hi: int) -> None:
    """ Quicksort by using 3 way partitioning.


        Parameters:
        arr: input list to be sorted in-place
        lo: low index of array to be sorted
        hi: high index of array to be sorted

        Returns:
        None
    """

    if lo >= hi:
        return

    # Partition by first eleemnt
    l, h = partition_3w(arr, lo, hi)

    # As partition keys are in place sort recursively other elements
    _qsort(arr, lo, l - 1)
    _qsort(arr, h + 1, hi)




