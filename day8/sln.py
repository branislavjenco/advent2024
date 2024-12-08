from collections import defaultdict
from itertools import combinations

g = []
antennas = defaultdict(set)
with open("input.txt") as f:
    for row, file_line in enumerate(f.readlines()):
        line = []
        for col, char in enumerate(file_line.strip()):
                line.append(char)
                if char != ".":
                    antennas[char].add((row, col))
        g.append(line)

def at(grid, row, col):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        return "n"
    else:
        return grid[row][col]


def minus(a, b):
     return (a[0]-b[0], a[1]-b[1])

def plus(a, b):
     return (a[0]+b[0], a[1]+b[1])

def find_antinodes(antennas, g, harmonics=False):
    antinodes = set()
    for freq, pos in antennas.items():
        cs = list(combinations(pos, 2))
        distances = [minus(c[0], c[1]) for c in cs]
        for i, c in enumerate(cs):
            if harmonics:
                antinodes.add(c[0])
                antinodes.add(c[1])
            pls = plus(c[0], distances[i])
            while at(g, pls[0], pls[1]) != "n":
                antinodes.add(pls)
                if not harmonics:
                    break
                pls = plus(pls, distances[i])
            min = minus(c[1], distances[i])
            while at(g, min[0], min[1]) != "n":
                antinodes.add(min)
                if not harmonics:
                    break
                min = minus(min, distances[i])
    return antinodes

print("Part 1", len(find_antinodes(antennas, g, False)))
print("Part 2", len(find_antinodes(antennas, g, True)))
     