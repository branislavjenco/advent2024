from collections import defaultdict
import math
import os
import re
import time
robots = []
test_bounds = (7,11)
bounds = (103, 101)
with open("input.txt") as f:
    matches = re.findall(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", f.read())
    for p1, p2, v1, v2 in matches:
        robots.append(((int(p2),int(p1)), (int(v2),int(v1))))

def at(grid, pos):
    row, col = pos
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        return "n"
    else:
        return grid[row][col]

def set(grid, pos, ch):
    row, col = pos
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        return
    grid[row][col] = ch

def add(p, v):
    return (p[0] + v[0], p[1] + v[1])
    
def sub(p, v):
    return (p[0] - v[0], p[1] - v[1])

def mul(p, f):
    return (p[0] * f, p[1] * f)

def mod(p, m):
    return (p[0] % m[0], p[1] % m[1])

def vis(robots, bounds):
    g = []
    for x in range(bounds[0]):
        line = []
        for y in range(bounds[1]):
            line.append(0)
        g.append(line)
    for p, _ in robots:
        n = at(g, p)
        set(g, p, n+1)
    return "\n".join(["".join([str(x) if x != 0 else "." for x in line ]) for line in g])

# print(vis(robots, bounds))
# print("---------------------------------------------------------------------------------------")

def move_robots(robots, bounds, steps=100, backwards=False):
    moved = []
    op = sub if backwards else add
    for p, v in robots:
        p = mod(op(p, mul(v, steps)), bounds)
        moved.append((p, v))
    return moved

def get_quadrant(pos, bounds):
    row, col = pos
    vm_i = bounds[1] // 2
    hm_i = bounds[0] // 2
    # print(row, col, vm_i, hm_i, bounds)
    if row >= 0 and row < hm_i and col >= 0 and col < vm_i: 
        return 0
    if row > hm_i and row < bounds[0] and col >= 0 and col < vm_i: 
        return 1
    if row >= 0 and row < hm_i and col > vm_i and col < bounds[1]: 
        return 2
    if row > hm_i and row < bounds[0] and col > vm_i and col < bounds[1]: 
        return 3
    else:
        return -1

def solve(robots, bounds):
    counts = defaultdict(int)
    for r in robots:
        counts[get_quadrant(r[0], bounds)] += 1
    # print(counts)
    return math.prod([v for k,v in counts.items() if k >= 0 ])


def same(robots1, robots2):
    for i in range(len(robots1)):
        if robots1[i][0] != robots2[i][0]:
            return False
    return True

print(vis(move_robots(robots, bounds), bounds))

print("Part 1", solve(move_robots(robots, bounds), bounds))
# s = ""
# for i in range(1000):
#     print(i)
#     robots = move_robots(robots, bounds, 1, backwards=True)
#     s += vis(robots, bounds)
#     s += "\n=====================================================================================================\n"
#     # time.sleep(0.2)
#     # print('\033[104A\033[2K', end='')
# with open("tree.txt", "w") as f:
#     f.write(s)

    

