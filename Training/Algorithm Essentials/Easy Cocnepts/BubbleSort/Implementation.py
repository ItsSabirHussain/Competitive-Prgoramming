def bubbleSort(array):
    isSorted = False
    counter = 0
    while not isSorted:
        isSorted = True
        for i in range(len(array)-1-counter):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                isSorted = False
    return array

if __name__ == '__main__':
    print(bubbleSort([9,8,7,6,5,4,3,2,1]))
