if __name__ == '__main__':
    for _ in range(int(input())):
        n, a, b = map(int, input().split(" "))
        f = ord("a")
        uniset = ""
        for i in range(b):
            uniset = uniset + chr(f + i)
        tmp = int(n / b)
        tmp2 = int(n % b)
        res = uniset * tmp + uniset[:tmp2]
        print(res)