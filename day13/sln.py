import re


def to_int(tup):
    return (int(tup[0]), int(tup[1]))


machines = []

with open("input.txt") as f:
    content = f.read()
    alist = re.findall(r"Button A\: X\+(\d+), Y\+(\d+)", content)
    blist = re.findall(r"Button B\: X\+(\d+), Y\+(\d+)", content)
    prizelist = re.findall(r"Prize\: X=(\d+), Y=(\d+)", content)
    machines = list(
        [to_int(a), to_int(b), to_int(prize)]
        for a, b, prize in zip(alist, blist, prizelist)
    )


def button_presses(machine):
    a, b, prize = machine
    a_presses = (prize[0] * a[1] - prize[1] * a[0]) / (a[1] * b[0] - a[0] * b[1])
    b_presses = (prize[0] - a_presses * b[0]) / a[0]
    return a_presses, b_presses


def solve(machines):
    return sum(
        [
            int(3 * a_presses + b_presses)
            for a_presses, b_presses in [
                button_presses(machine) for machine in machines
            ]
            if a_presses.is_integer() and b_presses.is_integer()
        ]
    )


print("Part 1", solve(machines))
print(
    "Part 2",
    solve(
        [
            [a, b, (prize[0] + 10000000000000, prize[1] + 10000000000000)]
            for a, b, prize in machines
        ]
    ),
)

"""
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
this produced numerically instable numbers, so this alternate version is better:
y = (prizex*ay - prizey*ax) / (ay*bx - ax*by)
"""
