for i in range(int(input())):
    x, n , m = map(int, input().split(" "))
    while x > (int(x/2)+10) and n:
        x = (int(x/2)+10)
        n = n - 1
    while x > 0 and m:
        x = x - 10
        m = m - 1

    if x <= 0:
        print("Yes")
    else:
        print("No")