import utils

input = [int(i) for i in utils.getInput(1)]

for f in input:
    for s in input:
        if (f + s) == 2020 and (f != s):
            print(f"Part 1: {f} * {s} = {f * s}")

        for t in input:
            if (f + s + t) == 2020 and f != s and f != t and s != t:
                print(f"Part 2: {f} * {s} * {t} = {f * s * t}")
