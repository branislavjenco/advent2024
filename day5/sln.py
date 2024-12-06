from collections import defaultdict

rules_s = ""
updates_s = ""

with open("test_input.txt") as f:
    rules_s, updates_s = f.read().split("\n\n")

rules = [[int(x) for x in rule.split("|")] for rule in rules_s.split("\n")]
updates = [[int(x) for x in update.split(",")] for update in updates_s.strip().split("\n")]
print(rules)
order = defaultdict(list)
order = []

rules2 = rules + [[y,x] for x,y in rules]
print(rules2)

res = 0
for u in updates:
    m = {} 
    for i,n in enumerate(u):
        m[n] = { "before": u[:i], "after": u[i+1:] }
    invalid = False
    for n, _map in m.items():
        for r in rules:
            if (r[0] == n and r[1] in _map["before"]) or (r[1] == n and r[0] in _map["after"]):
                invalid = True
        if invalid:
            break
    if not invalid:
        res += u[len(u)//2]

print("Part 1", res)
        
                
                



