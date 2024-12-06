g = []
player = (None, "up")
with open("input.txt") as f:
    for row, file_line in enumerate(f.readlines()):
        line = []
        for col, char in enumerate(file_line.strip()):
            if char == "^":
                player = ((row, col), "up")
                line.append(".")
            else:
                line.append(char)
        g.append(line)

def at(grid, row, col):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        return "n"
    else:
        return grid[row][col]

def in_front(player, g):
    ahead = forward(player)
    return at(g, ahead[0], ahead[1])

def forward(player):
    pos, heading = player
    if heading == "up":
        ahead = (pos[0]-1, pos[1])
    elif heading == "down":
        ahead = (pos[0]+1, pos[1])
    elif heading == "right":
        ahead = (pos[0], pos[1]+1)
    elif heading == "left":
        ahead = (pos[0], pos[1]-1)
    return ahead

def turn(player):
    _, heading = player
    if heading == "up":
        new_heading = "right"
    elif heading == "down":
        new_heading = "left"
    elif heading == "right":
        new_heading = "down"
    elif heading == "left":
        new_heading = "up"
    return new_heading

def scout_obstacle(player, g, visited):
    pos, _ = player
    scout = (pos, turn(player))
    ch = in_front(scout, g)
    found_obstacle = False
    while ch != "n":
        if scout[0] in visited and at(g, forward(scout)[0], forward(scout)[1]) == "#":
            found_obstacle = True
            break
        scout = (forward(scout), scout[1])
        ch = in_front(scout, g)
    return found_obstacle
    
    
visited = set()
loops = set()
ch = in_front(player, g)
visited.add(player[0])
while ch != "n":
    print(player)
    if ch == "#":
        player = (player[0], turn(player))
    else:
        player = (forward(player), player[1])
        if scout_obstacle(player, g, visited):
            print("loop", player[0])
            loops.add(player[0])
        visited.add(player[0])
    ch = in_front(player, g)

print("Part 1", len(visited))
print("Part 2", len(loops))


