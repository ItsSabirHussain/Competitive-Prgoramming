if __name__ == '__main__':
    for i in range(int(input())):
        xx, yy, zz = map(int, input().split(" "))
        arrx = list(map(int, input().split(" ")))
        arry = list(map(int, input().split(" ")))
        arrz = list(map(int, input().split(" ")))

        xmax = max(arrx)
        ymax = max(arry)
        zmax = max(arrz)

        xmin = min(arrx)
        ymin = min(arry)
        zmin = min(arrz)

        print(min(
            pow(xmax - ymin, 2) + pow(ymin - zmin, 2) + pow(zmin - xmax, 2),
            pow(xmax - ymin, 2) + pow(ymin- zmax, 2) + pow(zmax - xmax, 2),
            pow(xmax - ymax, 2) + pow(ymax - zmax, 2) + pow(zmax - xmax, 2),
            pow(xmin - ymax, 2) + pow(ymax - zmin, 2) + pow(zmin - xmin, 2),
            pow(xmin - ymin, 2) + pow(ymin - zmax, 2) + pow(zmax - xmin, 2),
            pow(xmin - ymax, 2) + pow(ymax - zmin, 2) + pow(zmin - xmin, 2),
            pow(xmin - ymax, 2) + pow(ymax - zmax, 2) + pow(zmax - xmin, 2),
            pow(xmax - ymin, 2) + pow(ymin - zmin, 2) + pow(zmin - xmax, 2)))