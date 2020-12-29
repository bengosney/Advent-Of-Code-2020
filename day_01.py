from itertools import combinations
from math import prod

import utils

input = [int(i) for i in utils.getInput(1).splitlines()]

for i in (1, 2):
    for combo in combinations(input, 1 + i):
        if sum(combo) == 2020:
            print(f"part {i}: {prod(combo)}")
            break
