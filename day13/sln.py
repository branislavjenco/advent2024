data = []
with open("input.txt") as f:
    content = f.read()
    parts = content.split("\n\n")
    for part in parts:
        button_a, button_b, prize = part.split("\n")
        ax, ay = (button_a.split(": ")[1]).split(", ")
        ax = int(ax.replace("X+", ""))
        ay = int(ay.replace("Y+", ""))
        bx, by = (button_b.split(": ")[1]).split(", ")
        bx = int(bx.replace("X+", ""))
        by = int(by.replace("Y+", ""))
        prizex, prizey = (prize.split(": ")[1]).split(", ")
        prizex = int(prizex.replace("X=", ""))
        prizey = int(prizey.replace("Y=", ""))
        data.append([(ax, ay), (bx, by), (prizex, prizey)])

def solve(data):
    s = 0
    for conf in data:
        a, b, prize = conf
        y = (prize[0]*a[1] - prize[1]*a[0]) / (a[1]*b[0] - a[0]*b[1])
        x = (prize[0] - y*b[0])/a[0]
        if abs(round(x) - x) != 0 or abs(round(y) - y) != 0:
            continue
        cost = 3*x + y
        s += int(cost)
    return s

print("Part 1", solve(data))
print("Part 2", solve([[a, b, (prize[0]+10000000000000, prize[1]+10000000000000)] for a,b,prize in data]))
        
'''
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
y = (prizex*ay - prizey*ax) / (ay*bx - ax*by)
this produced numerically instable numbers, this simplified version is better for that
y = (prizex*ay - prizey*ax]) / (ay*bx - ax*by)
'''

