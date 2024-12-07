equations = []
with open("input.txt") as f:
     equations = [ line.strip().split(": ") for line in f.readlines()]
     equations = [[int(value), [int(n) for n in numbers.split(" ")][::-1]] for value, numbers in equations]

def minus(a, b):
    return a - b

def div(a, b):
    return a / b

def split(a, b):
    a = int(a)
    len_b = len(str(b))
    if str(a).endswith(str(b)):
        removed_b = str(a)[:-len_b]
        if len(removed_b) < 1:
            return -1
        else:
            return int(removed_b)
    else:
        return -1


def check(v, numbers, ops):
    def step(ns, partial):
        if partial == 0:
            return True
        if len(ns) == 0 or partial < 0 or not partial.is_integer():
            return False
        head, *tail = ns
        return any([step(tail, op(partial, head)) for op in ops])
    return step(numbers, v) 


print("Part 1", sum([value for value, numbers in equations if check(value, numbers, [div, minus])])) 
print("Part 2", sum([value for value, numbers in equations if check(value, numbers, [div, minus, split])])) 