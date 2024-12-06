g = []
player = (None, "up")
start_pos = None
with open("input.txt") as f:
    for row, file_line in enumerate(f.readlines()):
        line = []
        for col, char in enumerate(file_line.strip()):
            if char == "^":
                start_pos = (row, col) 
                player = (start_pos, "up")
                line.append(".")
            else:
                line.append(char)
        g.append(line)

def at(grid, row, col):
    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
        return "n"
    else:
        return grid[row][col]

def ahead(player, g):
    ahead = forward_of(player)
    return at(g, ahead[0], ahead[1])

def forward_of(player):
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

def right_turn_of(player):
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

def scout_loop(player, g):
    pos, _ = player
    scout = (pos, right_turn_of(player))
    ch = ahead(scout, g)
    found_loop = False
    scout_visited = set()
    scout_visited.add(player)
    while ch != "n":
        if ch == "#":
            scout = (scout[0], right_turn_of(scout))
        else:
            scout = (forward_of(scout), scout[1])
        
        if scout in scout_visited:
            found_loop = True
            break
        scout_visited.add(scout)
        ch = ahead(scout, g)
    return found_loop
    
    
visited = set()
obstructions = set()
ch = ahead(player, g)
visited.add(player[0])
while ch != "n":
    # print(player)
    if forward_of(player) not in visited and scout_loop(player, g):
        obs_pos = forward_of(player)
        if at(g, obs_pos[0], obs_pos[1]) != "n":
            obstructions.add(obs_pos)
    if ch == "#":
        player = (player[0], right_turn_of(player))
    else:
        player = (forward_of(player), player[1])
    visited.add(player[0])
    ch = ahead(player, g)

print("Part 1", len(visited))
print("Part 2", len(obstructions - set(start_pos)))


