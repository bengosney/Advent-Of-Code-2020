import utils

input = [int(i) for i in utils.getInput(1).splitlines()]

p1 = None
p2 = None

for f in input:
    for s in input:
        if (f + s) == 2020 and (f != s):
            p1 = f * s

        for t in input:
            if (f + s + t) == 2020 and f != s and f != t and s != t:
                p2 = f * s * t
                break
        if p1 and p2:
            break
    if p1 and p2:
        break

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")
