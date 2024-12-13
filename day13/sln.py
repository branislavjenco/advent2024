import re

data = []

def to_int(tup):
    return (int(tup[0]), int(tup[1]))
    
with open("input.txt") as f:
    content = f.read()
    alist = re.findall(r"Button A\: X\+(\d+), Y\+(\d+)", content)
    blist = re.findall(r"Button B\: X\+(\d+), Y\+(\d+)", content)
    prizelist = re.findall(r"Prize\: X=(\d+), Y=(\d+)", content)
    data = list([to_int(a), to_int(b), to_int(prize)] for a, b, prize in zip(alist, blist, prizelist))

def solve(data):
    res = 0
    for conf in data:
        a, b, prize = conf
        y = (prize[0]*a[1] - prize[1]*a[0]) / (a[1]*b[0] - a[0]*b[1])
        x = (prize[0] - y*b[0])/a[0]
        if abs(round(x) - x) != 0 or abs(round(y) - y) != 0:
            continue
        cost = 3*x + y
        res += int(cost)
    return res

print("Part 1", solve(data))
print("Part 2", solve([[a, b, (prize[0]+10000000000000, prize[1]+10000000000000)] for a,b,prize in data]))
        
'''
derivation
derivation
x*ax + y*bx = prizex
x*ay + y*by = prizey
----------------------
x*ax + y*bx = prizex
x*ay  = prizey - y*by
----------------------
x*ax + y*bx = prizex
x = (prizey - y*by)/ay
----------------------
x = (prizex - y*bx)/ax
x = (prizey - y*by)/ay
----------------------
(prizex - y*bx)/ax = (prizey - y*by)/ay
y = (prizex/ax - prizey/ay) / (bx/ax - by/ay)
this produced numerically instable numbers, so this simplified version is better for that:
y = (prizex*ay - prizey*ax) / (ay*bx - ax*by)
'''