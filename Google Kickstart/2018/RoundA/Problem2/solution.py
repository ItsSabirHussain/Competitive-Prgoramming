import random
if __name__ == '__main__':
    for i in range(int(input())):
        N, K = map(int, input().split(" "))
        bag = list(map(int, input().split(" ")))
        value = 0
        for j in range(K):
            tmp = bag[random.randint(0,N-1)]
            if tmp > value:
                value = value + max(tmp,sum(bag)/N)/N
        if value < sum(bag)/N:
            value = sum(bag)/N
        print("Case #{}: {}".format(i+1, value))

