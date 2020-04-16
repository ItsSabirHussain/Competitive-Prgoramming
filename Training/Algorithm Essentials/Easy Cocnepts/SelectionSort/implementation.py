def selectionSort(array):
    currentIdx = 0
    while currentIdx < len(array)-1:
        smallestIdx = currentIdx
        for i in range(currentIdx, len(array)):
            if array[smallestIdx] > array[i]:
                smallestIdx = i
        array[currentIdx], array[smallestIdx] = array[smallestIdx], array[currentIdx]
        currentIdx +=1
    return array

if __name__ == '__main__':
    print(selectionSort([9, 8, 7, 6, 5, 4, 3, 2, 1]))