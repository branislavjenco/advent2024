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

def get_diffsum(line):
    return abs(sum([diff(a, b) for a, b in zip(line, line[1:])]))

def is_line_safe(line):
    return get_diffsum(line) == len(line) - 1

safe_1 = 0 
safe_2 = 0 

for line in lines:
    if is_line_safe(line):
        safe_1 += 1
        safe_2 += 1
    else:
        for i in range(0, len(line)):
            new_line = line[:i] + line[i+1:]
            if is_line_safe(new_line):
                safe_2 += 1
                break


print("Part 1", safe_1)
print("Part 2", safe_2)

