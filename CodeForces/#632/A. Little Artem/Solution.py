def validate(grid, i, j, c):
    if i-1 >= 0:
        if grid[i - 1][j] == c:
            return False
    if j-1 >= 0:
        if grid[i][j - 1] == c:
            return False
    return True


def backtracker(grid, i, j):
    if not grid[i][j][1]:
        return (i,j)
    else:
        if i >= 0:
            return backtracker(grid, i-1, j)
        elif j >= 0:
            return backtracker(grid,len(grid)-1, j-1)
        else:
            return False


def solve(grid,i,j):
    if i < len(grid) and j < len(grid):

        if validate(grid, i, j, "W"):
            grid[i][j] = ("W",1)
            if j < len(grid):
                solve(grid, i+1, j)
            else:
                solve(grid, 0, j+1)
        elif validate(grid, i, j, "B"):
            grid[i][j] = ("B",1)
            if j < len(grid):
                solve(grid, i+1, j)
            else:
                solve(grid, 0, j+1)
        else:
            grid[i][j] = ("B",1)
            backti = backtracker(grid,i,j)
            if backti:
                solve(grid, backti[0], backti[1])
    else:
        return grid


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        r, c = map(int, input().split(" "))
        grid = [[0 for i in range(c)] for j in range(r)]
        print(solve(grid, 0, 0))
