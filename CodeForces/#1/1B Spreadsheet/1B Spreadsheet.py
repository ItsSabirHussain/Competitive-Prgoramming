t = int(input())
for i in range(t):
    s = str(input())
    type = "EXCEL"
    if s[0] == 'R':
        fdigi = 1
        for j in range(1, len(s)):
            if s[j].isdigit():
                fdigi = j
                break
        for j in range(fdigi, len(s)):
            if s[j] == 'C':
                type = "RXCY"
                break
    if type == "EXCEL":
        clm = ''
        rw = ''
        clmnum = 0

        for j in s:
            if j.isalpha():
                clm = clm + j
            else:
                rw = rw + j

        for j in clm[:len(clm)-1]:
            clmnum = clmnum * (int(ord(j)) - 64)
        clmnum = clmnum + int(ord(clm[len(clm)-1]))

        print("R{}C{}".format(rw, clmnum))

    if type == "RXCY":
        clm = ''
        rw = ''
        tmpind = 0
        for j in range(1, len(s)):
            if s[j] == "C":
                tmpind = j+1
                break
        rw = s[1:tmpind]
        clmnum = int(s[tmpind:])

        while(clmnum > 26 and not clmnum % 26 == 0):
            clm = clm + chr(clmnum%26)
            clmnum = clmnum - clmnum%26
        clm = clm + chr(clmnum%26)

        print("{}{}".format(clm, rw))
    print("Done")








