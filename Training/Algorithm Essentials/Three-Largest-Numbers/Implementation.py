import math


def solver(arr):
    res = [-math.inf, -math.inf, -math.inf]

    for i in arr:

        if res[2] < i:
            res[0] = res[1]
            res[1] = res[2]
            res[2] = i

        elif res[1] < i:
            res[0] = res[1]
            res[1] = i

        elif res[0] < i:
            res[0] = i

    return res


if __name__ == '__main__':
    print(solver([1,2,3,4,5,6,7,8,9]))