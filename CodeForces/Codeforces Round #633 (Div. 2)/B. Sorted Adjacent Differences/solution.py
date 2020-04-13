if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        alen = int(input())
        arr = list(map(int, input().split(" ")))
        arr.sort()
        for i in range(alen//2):
            if alen%2 == 0:
                print(arr[alen//2-i-1], arr[alen//2+i], end=" ")
            if not alen%2 == 0:
                print(arr[alen//2-i], arr[alen//2+i+1], end=" ")
        if alen%2:
            print(arr[0], end=" ")
        print()







