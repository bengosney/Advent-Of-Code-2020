import re
from collections import defaultdict

import utils

input = utils.getInput(14).splitlines()

memory = defaultdict(lambda: 0)


def maskValue(value, mask):
    binVal = str(bin(value)[2:]).zfill(len(mask))
    maskedVal = []
    for i, maskBit in enumerate(mask):
        if maskBit == "X":
            maskedVal.append(binVal[i])
        else:
            maskedVal.append(maskBit)

    return int("".join(maskedVal), 2)


mask = None
for line in input:
    cmd, value = line.split(" = ")
    if cmd == "mask":
        mask = value
        continue

    memloc = int(re.search(r"\d+", cmd).group())

    memory[memloc] = maskValue(int(value), mask)


print(f"part 1: {sum(memory.values())}")
