def towNumSumByHashTable(array, target):
    res = []
    hashTable = {}
    for num in array:
        hashTable.update({target - num:True})
    for num in array:
        if hashTable[target-num]:
            res.append((target-num, num))
    return res



def towNumSumBySorting(array, target):
    array.sort()
    l = 0
    r = len(array)-1
    while l<r:
        if array[l] + array[r] == target:
            return (array[l], array[r])
        elif array[l] + array[r] > target:
            r -= 1
        else:
            l += 1
    return -1

if __name__ == '__main__':
    print(towNumSumBySorting([3, 5, -4, 8, 11, 1, -1, 6], 10))
