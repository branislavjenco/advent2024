lines = []
with open("input.txt") as f:
    lines = [[int(n) for n in line.split(" ")] for line in f.readlines()]

def diff(a, b):
    if b > a and b < a + 4:
        return 1
    elif a > b and a < b + 4:
        return -1
    else:
        return 0

safe_1 = 0 
safe_2 = 0 

for line in lines:
    diffsum = sum([diff(a, b) for a, b in zip(line, line[1:])])
    if abs(diffsum) == len(line) - 1:
        safe_1 += 1
        safe_2 += 1
    else:
        for i in range(0, len(line)):
            new_line = line[:i] + line[i+1:]
            diffsum = sum([diff(a, b) for a, b in zip(new_line, new_line[1:])])
            if abs(diffsum) == len(new_line) - 1:
                safe_2 += 1
                break


print("Part 1", safe_1)
print("Part 2", safe_2)

