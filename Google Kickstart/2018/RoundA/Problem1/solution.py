def solve(tnum, num, do):
    tmp = list(str(num))
    if do == '-':
        for i in range(len(tmp)):
            if not int(tmp[i]) % 2 == 0:
                tmp[i] = str(int(tmp[i]) - 1)
                for j in range(i + 1, len(tmp)):
                    tmp[j] = '8'
        return tnum - int("".join(tmp))
    if do == '+':
        for i in range(len(tmp)):
            if not int(tmp[i]) % 2 == 0:
                if (tmp[i]) == "9":
                    if (i == 0):
                        tmp[i] = str(int(tmp[i]) + 1)
                    else:
                        tmp[i - 1] = str(int(tmp[i - 1]) + 1)
                    return solve(tnum, int(''.join(tmp)), '+')
                else:
                    tmp[i] = str(int(tmp[i]) + 1)
                    for j in range(i + 1, len(tmp)):
                        tmp[j] = '0'

        return int("".join(tmp)) - tnum

if __name__ == '__main__':
    for i in range(int(input())):
        inp = int(input())
        M = solve(inp, inp, '-')
        P = solve(inp, inp, '+')
        result = min(M, P)
        print("Case #{}: {}".format(i+1,result))
