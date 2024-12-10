g = []
trailheads = []
with open("input.txt") as f:
    for row, file_line in enumerate(f.readlines()):
        line = []
        for col, char in enumerate(file_line.strip()):
            if char == "0":
                trailheads.append((row, col))
            line.append(int(char))
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

def valid_next_steps(g, pos):
    val = at(g, pos)
    valid_steps = []
    for next_step in [up(pos), down(pos), left(pos), right(pos)]:
        if val + 1 == at(g, next_step):
            valid_steps.append(next_step)
    return valid_steps
    
def find_trail(g, start):
    def step(g, pos):
        print("step", pos)
        val = at(g, pos)
        if val == 9:
            return pos
        steps = valid_next_steps(g, pos)
        print("next steps", steps)
        if not steps:
            return 
        return [step(g, s) for s in steps]
    return step(g, start)

def flatten(container):
    for i in container:
        if isinstance(i, (list)):
            for j in flatten(i):
                yield j
        else:
            yield i

s = 0
for trailhead in trailheads:
    partial = find_trail(g, trailhead)
    partial = set(flatten(partial))
    partial = [x for x in partial if x is not None] 
    print(partial)
    s += len(partial)

print("Part 1", s)

def find_trail2(g, start):
    def step(g, pos):
        print("step", pos)
        val = at(g, pos)
        if val == 9:
            return 1
        steps = valid_next_steps(g, pos)
        print("next steps", steps)
        if not steps:
            return 0 
        return sum([step(g, s) for s in steps])
    return step(g, start)
s = 0
for trailhead in trailheads:
    n = find_trail2(g, trailhead)
    s += n

print("Part 2", s)