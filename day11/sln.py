import math

stones = []

with open("input.txt") as f:
    stones = sorted([int(s) for s in f.readline().strip().split(" ")])

print(stones)

cache = {}

def blink(stone, count):
    if count == 0:
        return 1
    if cache.get((stone, count)) is not None:
        return cache[(stone, count)] 
    val = None
    if stone == 0:
        val = blink(1, count - 1)
    else:
        digits = int(math.log10(stone))+1
        if digits % 2 == 0:
            val = blink(int(str(stone)[:(digits//2)]), count - 1) + blink(int(str(stone)[(digits//2):]), count - 1)
        else:
            val = blink(stone * 2024, count - 1)
    cache[(stone, count)] = val
    return val



print("Part 1", sum([blink(stone, 25) for stone in stones]))
print("Part 1", sum([blink(stone, 75) for stone in stones]))


        

"""
                  0
                  1
                2024
        20                24
    2       0         2        4
   4048     1       4048     8096
 40   48   2024   40   48   80   96
4  0 4  8 20  24 4  0 4  8 8  0 9  6
8096 - 8096 16192 - 8096 - 8096 16192
"""
"""
3
6072
60 72
6 0 7 2
12144 1 
"""