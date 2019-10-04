# Courserea: Divide and Conquer, Sorting and Searching, and 
# Randomized Algorithms by Stanford University

def countSplitInv(arrLeft:list, arrRight:list) -> int:
    """
    Counts split inversions where one elements is on left array while 
    the second one is in right array. 
    Sort input arrays before counting inversions and then count them
    with sorted array which if more efficient.

    Returns:
        count of inversions
    """

    invNum = 0

    arrL = sorted(arrLeft)
    arrR = sorted(arrRight)

    leftCount = len(arrL)
    rightCount = len(arrR)

    leftIdx = rightIdx = 0

    while (True):
        if arrL[leftIdx] <= arrR[rightIdx]:
            leftIdx += 1
        elif arrL[leftIdx] > arrR[rightIdx]:
            rightIdx += 1
            invNum += leftCount - leftIdx
        
        if leftIdx == leftCount or rightIdx == rightCount:
            break

    return invNum


def countInversions(arr) -> int:
    """
    Count all inversions with Divide and conquer algorithm.
    Splits array into two arrays and counts inversions in each of them.
    Afterwards counts all inversions where one elements is on left array while 
    the second one is in right array
    """

    l = len(arr)
    invNum = 0

    if l > 1:
        leftArr = arr[:l // 2]
        rightArr = arr[l // 2:]

        invNum += countInversions(leftArr)
        invNum += countInversions(rightArr)
        invNum += countSplitInv(leftArr, rightArr)

    return invNum

a = [36, 1, 3, 5, 7, 9, 2, 4, 6, 10, 11]

print(countInversions(a))
