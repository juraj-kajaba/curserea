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
        Funtion ensures that partition key is in the place.

        Parameters:
        arr: list to be partitioned
        lo: low boundary to be partitioned
        hi: high boundary to be partitioned

        Returns:
        index of partitioned eleemnts
    """    
    i = lo + 1
    j = hi
    k = arr[lo] # partition element

    while True:
        while k >= arr[i] and i < hi:
            i += 1

        while k < arr[j] and j > lo:
            j -= 1

        if i >= j:
            break
        
        swap(arr, i, j)
            
    # Place partition key
    swap(arr, j, lo)

    return j



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





