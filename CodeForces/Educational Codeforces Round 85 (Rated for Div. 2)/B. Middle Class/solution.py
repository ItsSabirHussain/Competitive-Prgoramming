def solve(arr, x):
    arr.sort(reverse = True)
    extra = 0
    ans = 0
    for p in arr:
        if p < x:
            if extra + p >= x:
                ans = ans + 1
                extra = (extra - (x-p))
        else:
            ans = ans + 1
            extra = extra + (p - x)
    return ans
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, x = map(int, input().split(" "))
        ppls = list(map(int, input().split(" ")))
        print(solve(ppls, x))
