if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        arrl = int(input())
        arr = list(map(int, input().split(" ")))
        chk = True
        counter = 0
        while(counter<len(arr)):
            if arr[counter] == 1:
                subarr =  arr[counter+1:counter+6]
                tmpc = True
                for k in subarr:
                    if k == 1:
                        tmpc = False
                        break
                if not tmpc:
                    chk = False
                    break
                else:
                    counter = counter + 5
            else:
                counter = counter + 1
        if chk:
            print("YES")
        else:
            print("NO")
