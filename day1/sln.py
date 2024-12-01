from collections import defaultdict

left = []
right = []

with open("input.txt") as f:
    for line in f.readlines():
        l, r = line.split("   ")
        left.append(int(l))
        right.append(int(r))

left = sorted(left)
right = sorted(right)

res_1 = 0
for l,r in zip(left, right):
    res_1 += abs(l - r)

print("Part 1", res_1)

right_counts = defaultdict(int)
for n in right:
    right_counts[n] += 1

res_2 = 0
for n in left:
    res_2 += n * right_counts[n]

print("Part 2", res_2)

    





