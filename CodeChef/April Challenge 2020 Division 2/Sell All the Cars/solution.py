if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arrl = int(input())
        arr = list(map(int, input().split(" ")))
        arr.sort(reverse=True)
        print(arr)
        for i in range(len(arr)):
            arr[i] = arr[i] - i
            if arr[i] < 0:
                arr[i] = 0
        print(sum(arr))

