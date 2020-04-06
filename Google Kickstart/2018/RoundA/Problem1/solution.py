def solve(num, do):
    tmp = list(str(num))
    if do == '-':
        for i in range(len(tmp)):
            if not int(tmp[i]) % 2 == 0:
                tmp[i] = str(int(tmp[i]) - 1)
                for j in range(i + 1, len(tmp)):
                    tmp[j] = '8'
        return num - int("".join(tmp))
    if do == '+':
        for i in range(len(tmp)):
            if not int(tmp[i]) % 2 == 0:
                if (tmp[i]) == "9":
                    if (i == 0):
                        tmp[i] = str(int(tmp[i]) + 1)
                    else:
                        tmp[i - 1] = str(int(tmp[i - 1]) + 1)
                    return solve(int(''.join(tmp)), '+')
                else:
                    tmp[i] = str(int(tmp[i]) + 1)
                    for j in range(i + 1, len(tmp)):
                        tmp[j] = '0'
        return int("".join(tmp)) - num


for i in range(int(input())):
    inp = int(input())
    M = solve(inp, '-')
    P = solve(inp, '+')
    print(M)
    print(P)
    result = min(M, P)
    print("Case #", end="")
    print(i + 1, end="")
    print(":", result)