import re
from collections import defaultdict
from functools import lru_cache

import utils

input = utils.getInput(14).splitlines()

memoryPart1 = defaultdict(lambda: 0)
memoryPart2 = defaultdict(lambda: 0)


def maskValue(value, mask):
    binVal = str(bin(value)[2:]).zfill(len(mask))
    maskedVal = []
    for i, maskBit in enumerate(mask):
        if maskBit == "X":
            maskedVal.append(binVal[i])
        else:
            maskedVal.append(maskBit)

    return int("".join(maskedVal), 2)


@lru_cache
def getMemLocs(i, mask, loc, val):
    memlocs = []

    if i == len(mask):
        memlocs.append(loc)
    else:
        if mask[i] == "X":
            memlocs += getMemLocs(i + 1, mask, f"{loc}0", val)
            memlocs += getMemLocs(i + 1, mask, f"{loc}1", val)

        if mask[i] == "1":
            memlocs += getMemLocs(i + 1, mask, f"{loc}1", val)

        if mask[i] == "0":
            memlocs += getMemLocs(i + 1, mask, f"{loc}{val[i]}", val)

    return set(memlocs)


mask = None
for line in input:
    cmd, value = line.split(" = ")
    if cmd == "mask":
        mask = value
        continue

    memloc = int(re.search(r"\d+", cmd).group())

    memoryPart1[memloc] = maskValue(int(value), mask)

    maskedMemLocs = getMemLocs(0, mask, "", str(bin(memloc)[2:]).zfill(len(mask)))
    for maskedMemLoc in maskedMemLocs:
        memoryPart2[int(maskedMemLoc, 2)] = int(value)


print(f"part 1: {sum(memoryPart1.values())}")
print(f"part 2: {sum(memoryPart2.values())}")
