from collections import defaultdict

import utils

input = [int(i) for i in utils.getInput(15).split(",")]

lookup = defaultdict(lambda: [])
for i, m in enumerate(input):
    lookup[m].append(i + 1)

last = input[-1]
for i in range(len(input), 30000000):
    try:
        last = lookup[last][-1] - lookup[last][-2]
    except IndexError:
        last = 0

    lookup[last].append(i + 1)
    if i == 2019:
        print(f"part 1: {last}")

print(f"part 2: {last}")
