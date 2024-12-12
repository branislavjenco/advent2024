from collections import defaultdict
import sys

g = []

with open("input.txt") as f:
    for row, file_line in enumerate(f.readlines()):
        line = []
        for col, char in enumerate(file_line.strip()):
                line.append(char)
        g.append(line)

def at(grid, pos):
    row, col = pos
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        return "n"
    else:
        return grid[row][col]

def up(pos):
    return (pos[0]-1, pos[1])

def down(pos):
    return (pos[0]+1, pos[1])

def right(pos):
    return (pos[0], pos[1]+1)

def left(pos):
    return (pos[0], pos[1]-1)

def neighbours(pos):
     typ = at(g, pos)
     ns = [up(pos), down(pos), right(pos), left(pos)]
     same = set([n for n in ns if at(g, n) == typ])
     different = set([n for n in ns if at(g, n) != typ])
     return same, different

def is_visited(pos, plots):
    for plot in plots.values():
        if pos in plot:
            return True
    return False

def fill(square, visited):
    if square in visited:
        return set(), set()
    visited.add(square)
    ns, different = neighbours(square)
    ns_not_visited = [n for n in ns if n not in visited]
    edges = set([(square, d) for d in different])
    if not ns_not_visited:
        res = set([square]).union(visited)
        return res, edges
    else:
        res = set()
        for n in ns_not_visited:
            plot, n_edges = fill(n, visited)
            res = res.union(plot)
            edges = edges.union(n_edges)
        return res, edges

def create_plot_and_edge_map(g):
    plot_map = {}
    edge_map = {}
    i = 0
    for row in range(len(g)):
        for col in range(len(g[row])):
            pos = (row, col)
            typ = at(g, pos)
            if not is_visited(pos, plot_map):
                plot, edges = fill(pos, set())
                plot_map[f'{typ}{str(i)}'] = plot
                edge_map[f'{typ}{str(i)}'] = edges
                i += 1
    return plot_map, edge_map

def extents(edges):
    min_row = sys.maxsize
    min_col = sys.maxsize
    max_row = -2
    max_col = -2
    for e in edges:
        side1, side2 = e
        if side1[0] > max_row:
            max_row = side1[0]
        if side1[1] > max_col:
            max_col = side1[1]
        if side1[0] < min_row:
            min_row = side1[0]
        if side1[1] < min_col:
            min_col = side1[1]
        if side2[0] > max_row:
            max_row = side2[0]
        if side2[1] > max_col:
            max_col = side2[1]
        if side2[0] < min_row:
            min_row = side2[0]
        if side2[1] < min_col:
            min_col = side2[1]
    return min_row, max_row, min_col, max_col

def count_groups(l):
    groups = 1
    for p,n in zip(sorted(l), sorted(l)[1:]):
        if n != p + 1:
            groups += 1
    return groups

def sides_from_edges(edges: set):
    if len(edges) == 4:
        return 4
    min_row, max_row, min_col, max_col = extents(edges)
    horizontals = defaultdict(set)
    verticals = defaultdict(set)
    for i in range(min_row, max_row + 1):
        for e in edges:
            l,r = e
            if l[0] == i and r[0] == i+1:
                horizontals[f"{i}{i+1}"].add(e)
            if l[0] == i and r[0] == i-1:
                horizontals[f"{i}{i-1}"].add(e)
    for i in range(min_col, max_col + 1):
        for e in edges:
            l,r = e
            if l[1] == i and r[1] == i+1:
                verticals[f"{i}{i+1}"].add(e)
            if l[1] == i and r[1] == i-1:
                verticals[f"{i}{i-1}"].add(e)
    hc = 0 
    for h in horizontals.values():
        hc += count_groups([e[1][1] for e in h])
    vc = 0
    for v in verticals.values():
        vc += count_groups([e[0][0] for e in v])
    
    return vc + hc

plot_map, edge_map = create_plot_and_edge_map(g)
print("Part 1", sum([len(plot_map[k]) * len(edge_map[k]) for k in edge_map.keys()]))

side_map = {k: sides_from_edges(s) for k, s in edge_map.items()}
print("Part 2", sum([len(plot_map[k]) * side_map[k] for k in side_map.keys()]))
