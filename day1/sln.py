from collections import defaultdict

ls = []
rs = []

with open("input.txt") as f:
    for line in f.readlines():
        l, r = line.split("   ")
        ls.append(int(l))
        rs.append(int(r))

ls = sorted(ls)
rs = sorted(rs)

res_1 = sum([abs(l - r) for l,r in zip(ls, rs)])
print("Part 1", res_1)

right_counts = defaultdict(int)
for n in rs:
    right_counts[n] += 1

res_2 = sum([n * right_counts[n] for n in ls])
print("Part 2", res_2)

    





