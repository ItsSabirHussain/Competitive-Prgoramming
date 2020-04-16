def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j-1]:
            swap(j, j-1, array)
            j-=1
    return array


def swap(i, j, array):
    array[i] , array[j]  = array[j] , array[i]

if __name__ == '__main__':
    print(insertionSort([9,8,7,6,5,4,3,2,1]))