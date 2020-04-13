if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        if n % 2 == 0:
            print(int((n / 2) - 1))
        else:
            print(int(n / 2))