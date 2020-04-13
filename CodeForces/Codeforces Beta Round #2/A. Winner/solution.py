if __name__ == '__main__':
    t = int(input())
    dd = {}
    winner = ""
    for i in range(t):
        nm, sc = map(str, input().split(" "))
        if winner == "":
            winner = nm
        if not nm in dd:
            dd.update({nm:int(sc)})
            if dd[winner] < int(sc):
                winner = nm
        else:
            dd[nm] = dd[nm] + int(sc)
            if dd[winner] < int(sc):
                winner = nm
    print(winner)
