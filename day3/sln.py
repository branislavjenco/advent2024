import re
s = ""
with open("input.txt") as f:
    s = f.read()

res = sum([int(a) * int(b) for a, b in re.findall("mul\((\d{1,3}),(\d{1,3})\)", s)])
print("Part 1", res)


matches = re.finditer("mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)", s)
do = True
res = 0
for match in matches:
    if match.group(0) == "do()":
        do = True
    elif match.group(0) == "don't()":
        do = False
    else:
        if do:
            res += int(match.group(1)) * int(match.group(2))
print("Part 2", res)

