from collections import defaultdict
from functools import lru_cache

import utils

input = utils.getInput(10).split("\n")

maxDiff = 3

adaptors = [int(i) for i in input]
myAdaptor = max(adaptors) + 3
adaptors.append(myAdaptor)
adaptors.append(0)
adaptors.sort()

jumps = defaultdict(lambda: 0)

for i in range(len(adaptors) - 1):
    gap = adaptors[i + 1] - adaptors[i]
    jumps[gap] += 1

print(f"part 1: {jumps[1] * jumps[3]}")


@lru_cache
def getPos(i):
    if adaptors[i] == myAdaptor:
        return 1

    tot = 0
    for n in range(i + 1, i + maxDiff + 1):
        try:
            gap = adaptors[n] - adaptors[i]
            if gap <= maxDiff:
                tot += getPos(n)
        except IndexError:
            break

    return tot


pos = getPos(0)
print(f"part 2: {pos}")
