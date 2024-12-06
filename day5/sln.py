from collections import defaultdict
from functools import cmp_to_key

rules_s = ""
updates_s = ""

with open("input.txt") as f:
    rules_s, updates_s = f.read().split("\n\n")

rules = [tuple([int(x) for x in rule.split("|")]) for rule in rules_s.split("\n")]
updates = [[int(x) for x in update.split(",")] for update in updates_s.strip().split("\n")]

def cmp(a, b):
    if (a,b) in rules:
        return -1
    elif (b,a) in rules:
        return 1
    else:
        return 0

res_1 = 0
res_2 = 0
for u in updates:
    sorted_u = sorted(u, key=cmp_to_key(cmp))
    if tuple(u) == tuple(sorted_u):
        res_1 += u[len(u)//2]
    else:
        res_2 += sorted_u[len(sorted_u)//2]


print("Part 1", res_1)
print("Part 2", res_2)
        
                
                



