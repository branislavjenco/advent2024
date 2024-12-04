grid = []
with open("input.txt") as f:
    for line in f.readlines():
        grid.append(list(line.strip()))

def up(row, col):
    return [(row-1,col), (row-2,col), (row-3,col)]
def down(row, col):
    return [(row+1,col), (row+2,col), (row+3,col)]
def right(row, col):
    return [(row,col+1), (row,col+2), (row,col+3)]
def left(row, col):
    return [(row,col-1), (row,col-2), (row,col-3)]
def upright(row, col):
    return [(row-1,col+1), (row-2,col+2), (row-3,col+3)]
def downright(row,col):
    return [(row+1,col+1), (row+2,col+2), (row+3,col+3)]
def downleft(row, col):
    return [(row+1,col-1), (row+2,col-2), (row+3,col-3)]
def upleft(row, col):
    return [(row-1,col-1), (row-2,col-2), (row-3,col-3)]

dirs = [up, upright, right, downright, down, downleft, left, upleft]

def at(grid, row, col):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        return "."
    else:
        return grid[row][col]


def check(grid, positions):
    for i, ch in enumerate("MAS"):
        grid_ch = at(grid, positions[i][0], positions[i][1])
        if grid_ch != ch:
            return False
    return True

def count(grid, row, col):
    res = 0
    if grid[row][col] == "X":
        for d in dirs:
            if check(grid, d(row, col)):
                res += 1
    return res

total = 0
for row in range(len(grid)):
    for col in range(len(grid[row])):
        total += count(grid, row, col)


print("Part 1", total)

def upright(row, col):
    return [(row-1,col+1), (row+1,col-1)]
def downleft(row, col):
    return [(row-1,col-1), (row+1,col+1)]

def check_2(grid, positions):
    pattern = "".join([at(grid, positions[i][0], positions[i][1]) for i in range(len(positions))])
    if pattern == "MS" or pattern == "SM":
        return True
    return False

def count_2(grid, row, col):
    res = 0
    if grid[row][col] == "A":
        if check_2(grid, upright(row, col)) and check_2(grid, downleft(row, col)):
            res += 1
    return res

total = 0
for row in range(len(grid)):
    for col in range(len(grid[row])):
        total += count_2(grid, row, col)

print("Part 2", total)