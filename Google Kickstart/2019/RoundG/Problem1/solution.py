if __name__ == '__main__':
    for i in range(int(input())):
        N, M, Q = map(int, input().split(" "))
        tp = set(map(int, input().split(" ")))
        reader = list(map(int, input().split(" ")))
        pages = set({ii + 1 for ii in range(N)})
        ans = 0
        chktp = [False for jj in range(N+1)]
        for jj in tp:
            chktp[jj] = True

        for j in reader:
            tmp = int(N / j)
            tmpm = 0
            for jj in range(j, N, j):
                if chktp[jj]:
                    tmpm = tmpm + 1
            ans = ans + (tmp - tmpm)

        print("Case #{}: {}".format(i + 1, ans))









