import re

import utils

input = utils.getInput(2).split("\n")

parsed = [re.findall(r"(\d+)-(\d+)\s(\w):\s(.*)", i) for i in input]

v = 0
for p in parsed:
    p = p[0]
    c = p[3].count(p[2])
    if c >= int(p[0]) and c <= int(p[1]):
        v += 1

print(f"part one: {v}")

v = 0
for p in parsed:
    p = p[0]
    p1 = int(p[0])
    p2 = int(p[1])
    s = p[3]
    o = 0

    if p[2] == s[p1 - 1]:
        o += 1

    if p[2] == s[p2 - 1]:
        o += 1

    if o == 1:
        v += 1

print(f"part two: {v}")
