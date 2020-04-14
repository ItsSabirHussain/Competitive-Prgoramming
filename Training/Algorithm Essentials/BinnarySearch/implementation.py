def binarySearch(array, targetValue):
    array.sort()
    return helper(array, targetValue, 0, len(array)-1)


def helper(array, targetValue, left, right):
    if left > right:
        return -1

    middleIndex = (right + left) // 2

    middleValue = array[middleIndex]

    if middleValue == targetValue:
        return middleIndex
    elif middleValue < targetValue:
        return helper(array, targetValue, middleIndex+1, right)
    else:
        return helper(array, targetValue, left, middleIndex-1)

if __name__ == '__main__':
    sampleArray = [0, 1, 21, 33, 45, 61, 71, 72, 73]
    print(binarySearch(sampleArray, 33))
